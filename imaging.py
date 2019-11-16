import types
from enum import Enum

from google.cloud import vision
import io

def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

def text_detector(path):
    """Returns raw file"""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    return texts

def text_words(path):
    """Detects words in the file."""
    texts = text_detector(path)

    ingredients = False

    words = []

    # for text in texts:
    #     words.append(text.description)

    for text in texts:
        if text.description.lower() == 'ingredients' or text.description.lower() == 'ingredients:':
            ingredients = True
        if ingredients:
            words.append(text.description)

    return words

