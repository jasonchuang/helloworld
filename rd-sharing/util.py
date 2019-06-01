import googleapiclient.discovery

import base64

from PIL import Image

def predict_json(project, model, instances, version=None):
    # Create the AI Platform service object. # To authenticate set the environment variable
    # GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_file>
    service = googleapiclient.discovery.build('ml', 'v1')
    name = 'projects/{}/models/{}'.format(project, model)

    if version is not None:
        name += '/versions/{}'.format(version)

    if not isinstance(instances, list):
        instances = [instances]

    print name
    response = service.projects().predict(
        name=name,
        body={'instances': instances}
    ).execute()

    if 'error' in response:
        raise RuntimeError(response['error'])

    return response['predictions']

def decode_base64_to_file(file_name, b64_content):
    with open(file_name, "w") as text_file:
        text_file.write(base64.urlsafe_b64decode(str(b64_content)))

def output_grid_image(file_name):
    orig_img = Image.open("%s.jpg" % file_name)
    orig_width, orig_height = orig_img.size
    nldf_img = Image.open("%s.png" % file_name)
    blend_img = Image.blend(orig_img, nldf_img.convert('RGB'), alpha=0.5)

    # paste images and output
    blank_img = Image.new("RGB", (orig_width * 2, orig_height * 2))
    blank_img.paste(orig_img, (0, 0))
    fill_pixels_with_mask(blank_img, orig_img, nldf_img, orig_width, orig_height)
    blank_img.paste(nldf_img, (orig_width, 0))
    blank_img.paste(blend_img, (0, orig_height))
    blank_img.save("%s_grid.jpg" % file_name)

def fill_pixels_with_mask(blank_img, img, mask, width, height):
    pixels = img.load()
    mask_pixels = mask.load()
    for i in range(mask.size[0]):
        for j in range(mask.size[1]):
            if mask_pixels[i, j] > 0:
                pixels[i,j] = (162, 162, 162) # fill with gray
    blank_img.paste(img, (width, height))

def output_double_width_image(file_name):
    orig_img = Image.open("%s.jpg" % file_name)
    orig_width, orig_height = orig_img.size
    half_img = Image.open("%s_half.jpg" % file_name)

    blank_img = Image.new("RGB", (orig_width * 2, orig_height))
    blank_img.paste(orig_img, (0, 0))
    blank_img.paste(half_img, (orig_width, 0))
    blank_img.save("%s_grid.jpg" % file_name)
