import argparse
import base64
import json
import os
import sys
import util

from PIL import Image

PROJECT_NAME = "ikala-adtech-ml"
MODEL_NAME = "nldf_saved_model"
MODEL_VERSION = "v00018"

parser = argparse.ArgumentParser()
parser.add_argument('--input_image', type=str)
args = parser.parse_args()

def resize_nldf_image(orig_file_name, nldf_file_name):
    orig_img = Image.open(orig_file_name)
    orig_width, orig_height = orig_img.size

    img = Image.open(nldf_file_name)
    img = img.resize((orig_width, orig_height), Image.ANTIALIAS)
    img.save(nldf_file_name)

print args.input_image
filename = os.path.splitext(args.input_image)[0]
img_b64 = base64.b64encode(open(args.input_image, "rb").read())
instances_str = '{"keys": "%s", "input_string": {"b64":"%s"}}' % (filename, img_b64)

instances = json.loads(instances_str)
predictions = util.predict_json(PROJECT_NAME, MODEL_NAME, instances, version=MODEL_VERSION)
prediction = predictions[0]

img_output_path = "%s.png" % prediction['keys']
util.decode_base64_to_file(img_output_path, prediction['b64_output'])

# resize manually to target image size
resize_nldf_image(args.input_image, img_output_path)

# combine into grid
util.output_grid_image(filename)
