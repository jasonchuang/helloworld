import argparse
import base64
import json
import os
import util

from PIL import Image

PROJECT_NAME = "ikala-adtech-ml"
MODEL_NAME = "try_saved_model"
MODEL_VERSION = "v0004"

parser = argparse.ArgumentParser()
parser.add_argument('--input_image', type=str)
args = parser.parse_args()

orig_filename = os.path.splitext(args.input_image)[0]
img_b64 = base64.b64encode(open(args.input_image, "rb").read())
instances_str = '{"myInput": {"b64":"%s"}}' % (img_b64)

instances = json.loads(instances_str)
predictions = util.predict_json(PROJECT_NAME, MODEL_NAME, instances, version=MODEL_VERSION)
prediction = predictions[0]
#print prediction

img_output_path = "%s_half.jpg" % orig_filename
util.decode_base64_to_file(img_output_path, prediction['myOutput'])

util.output_double_width_image(orig_filename)
