import argparse
import base64
import json
import os
import util

from PIL import Image

PROJECT_NAME = "ikala-adtech-ml"
MODEL_NAME = "multiply_saved_model"
MODEL_VERSION = "v0001"

parser = argparse.ArgumentParser()
parser.add_argument('--input_float_list', type=str)
args = parser.parse_args()

print args.input_float_list
instances_str = '{"my_input": [%s], "keys":"test_key"}' % (args.input_float_list)

instances = json.loads(instances_str)
predictions = util.predict_json(PROJECT_NAME, MODEL_NAME, instances, version=MODEL_VERSION)
prediction = predictions[0]
print prediction

