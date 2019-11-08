import base64
import csv
import glob
import googleapiclient.discovery as discovery
import json
import os
import urllib.request

from bisect import bisect_left
from googleapiclient import errors
from multiprocessing import Pool
from parse import parse
from tqdm import tqdm

def download_image(row):
    r = parse("{url},{file_path}", row)
    try:
        urllib.request.urlretrieve(r['url'], r['file_path'])
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
        print('file_path:{} with exception:{}'.format(r['file_path'], e))

def download_images_to_folder(input_csv, output_folder):
    rows = []
    with open(input_csv) as csv_file:
        has_header = csv.Sniffer().has_header(csv_file.read(1024))
        csv_file.seek(0)

        reader = csv.reader(csv_file, delimiter=',')
        print('csv file has_header:{}'.format(has_header))
        if has_header:
            next(reader)

        for line in reader:
            rows.append('{},{}/{}.jpg'.format(line[1], output_folder, line[0]))

    print(len(rows))
    with Pool(processes=16) as p:
        with tqdm(rows, 'Downloadins images', leave=True) as bar:
            for i, _ in tqdm(enumerate(p.imap_unordered(download_image, rows))):
                r = parse("{},{}/{uid}.jpg", rows[i])
                bar.update()
                bar.set_description('Downloading image id {} into folder {}'.format(r['uid'], output_folder))

def decode_base64_to_file(file_name, b64_content):
    with open(file_name, "wb") as img_file:
        img_file.write(base64.b64decode(b64_content))

def encode_base64(img_path):
    return str(base64.b64encode(open(img_path, "rb").read()), "utf-8")

def convert_images_to_b64(input_dir, output_dir):
    file_count = 0
    for img in os.listdir(input_dir):
        img_path = os.path.join(input_dir, img)
        name = os.path.splitext(img)[0]
        content = '{"key":"%s", "image_bytes": {"b64": "%s"}}' % (name, encode_base64(img_path))
#        content = '{"key":"{}", "image_bytes": {"b64": "{}"}}'.format(name, encode_base64(img_path))

        file_index = "{:06d}".format(file_count)
        output_path = os.path.join(output_dir, "request_{}.json".format(file_index))
        with open(output_path, 'w') as json_file:
            json_file.write(content)
            file_count += 1

#OUTPUT_IMAGE_PREFIX ='etmall_picaas_20190826_'
OUTPUT_IMAGE_PREFIX =''
def convert_b64_to_images(input_dir, output_dir, is_multiple_job=False):
    for json_file in glob.glob(input_dir + "/prediction.results*"):
    #for json_file in glob.glob(input_dir + "/*/prediction.results*"):
        with open(json_file, 'r') as fp:
            for line in fp.readlines():
                request = json.loads(line)
                print(request['key'])
                img_output_path = os.path.join(output_dir, "{}{}.jpg".format(OUTPUT_IMAGE_PREFIX, request['key']))
                decode_base64_to_file(img_output_path, request['output_image_bytes']['b64'])

# for mlengine below
# 1. credential: export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"
# 2. job_id Error: A name should start with a letter and contain only letters, numbers and underscores

PROJECT_NAME = "ikala-adtech-ml"
REGION = "us-east1"
PROJECT_FULL_PATH = 'projects/{}'.format(PROJECT_NAME)

def make_job_body(job_id, input_paths, output_path, model_name, model_version, data_format='TEXT'):
    # Start building the request dictionary with required information.
    versionName = '{}/models/{}/versions/{}'.format(PROJECT_FULL_PATH, model_name, model_version)
    body = {'jobId': job_id,
            'predictionInput': {
                'dataFormat': data_format,
                'inputPaths': '{}{}_b64/request*'.format(input_paths, job_id),
                'outputPath': '{}output_{}_b64/'.format(output_path, job_id),
                "maxWorkerCount":"70",
                'region': REGION}}

    # Use the version if present, the model (its default version) if not.
    model_id = '{}/models/{}'.format(PROJECT_FULL_PATH, model_name)
    body['predictionInput']['versionName'] = versionName
    print(body)
    return body

def make_mlengine_job_request(job_id, input_paths, output_path, model_name, model_version):
    print('job_id:{}'.format(job_id))
    ml = discovery.build('ml', 'v1')
    request = ml.projects().jobs().create(parent=PROJECT_FULL_PATH,
            body=make_job_body(job_id, input_paths, output_path, model_name, model_version))
    response = None
    print('Job submitted.')
    try:
        response = request.execute()
        print('Job requested.')
        print('state : {}'.format(response['state']))
    except errors.HttpError as err:
        print(err)


def sort_list(a):
    return sorted(a)

# make sure your list 'a' is sorted!!!
def binary_search(a, x):
    # Locate the insertion point for x in a to maintain sorted order.
    # If x is already present in a, the insertion point will be before (to the left of) any existing entries
    index = bisect_left(a, x)
    if index < len(a) and a[index] == x:
        return True, index

    return False, index

