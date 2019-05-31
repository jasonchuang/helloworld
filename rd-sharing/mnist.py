import argparse
import json
import numpy
import util

from PIL import Image

PROJECT_NAME = "ikala-adtech-ml"
MODEL_NAME = "restore_mnist_saved_model"
MODEL_VERSION = "v0001"
#MODEL_NAME = "MNIST"
#MODEL_VERSION = "v1"

parser = argparse.ArgumentParser()
parser.add_argument('--input_image', type=str)
args = parser.parse_args()

print args.input_image
img = Image.open(args.input_image)
values = numpy.asarray(img) / 255.0
instances_data = {"myInput": values.ravel().tolist()}
instances_str = json.dumps(instances_data)
instances = json.loads(instances_str)

predictions = util.predict_json(PROJECT_NAME, MODEL_NAME, instances, version=MODEL_VERSION)
prediction = predictions[0]
print prediction
