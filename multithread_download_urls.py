import csv
import urllib.request

from multiprocessing import Pool
from parse import parse
from tqdm import tqdm
from tqdm import trange

def download_image(row):
    r = parse("{url},{file_path}", row)
    try:
        urllib.request.urlretrieve(r['url'], r['file_path'])
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        print('file_path:{} with exception:{}'.format(r['file_path'], e))

OUTPUT_CSV_ROW_CUSTOM_ID = 0
OUTPUT_CSV_ROW_OUTPUT_URL = 1
def download_images(download_csv, output_dir):
    rows = []
    with open(download_csv) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for line in reader:
            rows.append('{},{}/{}.jpg'.format(line[OUTPUT_CSV_ROW_OUTPUT_URL], output_dir, line[OUTPUT_CSV_ROW_CUSTOM_ID]))

    with Pool(processes=8) as p:
        with tqdm(rows, 'Downloadins images', leave=True) as bar:
            for i, _ in tqdm(enumerate(p.imap_unordered(download_image, rows))):
                r = parse("{},{}/{uid}.jpg", rows[i])
                bar.update()
                bar.set_description('Downloading image id {}'.format(r['uid']))
#            return len(rows)

download_images('2.csv', 'tmp')

