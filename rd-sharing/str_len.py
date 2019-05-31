import argparse
import json
import util

from PIL import Image

PROJECT_NAME = "ikala-adtech-ml"
MODEL_NAME = "try_saved_model"
MODEL_VERSION = "v0003"

parser = argparse.ArgumentParser()
parser.add_argument('--input_string', type=str)
args = parser.parse_args()

print args.input_string
instances_str = '{"myInput": "%s"}' % (args.input_string)

instances = json.loads(instances_str)
predictions = util.predict_json(PROJECT_NAME, MODEL_NAME, instances, version=MODEL_VERSION)
prediction = predictions[0]
print prediction

