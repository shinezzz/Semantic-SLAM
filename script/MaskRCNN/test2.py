import os
import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt
import display
import scipy.io as sio

ROOT_DIR = os.path.abspath("/home/zbf/zhaozhao/Mask_RCNN")

sys.path.append(ROOT_DIR)
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize

sys.path.append(os.path.join(ROOT_DIR,"samples/coco/"))
import coco

MODEL_DIR = os.path.join(ROOT_DIR,"logs")
COCO_MODEL_PATH = os.path.join(ROOT_DIR,"mask_rcnn_coco.h5")

if not os.path.exists(COCO_MODEL_PATH):
    utils.download_trained_weights(COCO_MODEL_PATH)

IMAGE_DIR = os.path.join(ROOT_DIR,"images")

class InferenceConfig(coco.CocoConfig):
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
config = InferenceConfig()
# config.display()

model = modellib.MaskRCNN(mode="inference",model_dir=MODEL_DIR,config=config)
model.load_weights(COCO_MODEL_PATH,by_name=True)

class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
               'bus', 'train', 'truck', 'boat', 'traffic light',
               'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
               'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
               'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
               'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
               'kite', 'baseball bat', 'baseball glove', 'skateboard',
               'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
               'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
               'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
               'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
               'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
               'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
               'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
               'teddy bear', 'hair drier', 'toothbrush']
# file_names = next(os.walk(IMAGE_DIR))[2]

IMAGE_DIR = os.path.abspath("/home/zbf/zhaozhao/data/rgb_png/")
file_names = ['5.png']
image = skimage.io.imread(os.path.join(IMAGE_DIR, random.choice(file_names)))
# for i,img_name in enumerate(file_names):
#     images.append(skimage.io.imread(os.path.join(IMAGE_DIR,img_name)))
# skimage.io.imshow(image)
# skimage.io.show()
#     results.append(model.detect([images[i]],verbose=1))
results = model.detect([image],verbose=1)
r = results[0]
display.display_instances(image, r['rois'], r['masks'], r['class_ids'],class_names, r['scores'],name="test",show_bbox=False)

# MY_IMAGE_DIR = os.path.abspath('/home/zbf/zhaozhao/data/rgb_png/')
# print(MY_IMAGE_DIR)
# for i,f in enumerate(os.listdir(MY_IMAGE_DIR)):

# read the dataset
# for f in os.listdir(MY_IMAGE_DIR):
#     image = skimage.io.imread(os.path.join(MY_IMAGE_DIR, f))
#     results = model.detect([image], verbose=1)
#     r = results[0]
#     # sio.savemat('savedata{}.mat'.format(f), {'rois': r['rois'], 'masks': r['masks'], 'class_ids': r['class_ids'],
#                                  # 'class_names': class_names, 'scores': r['scores'], })
# # # visualize.display_instances(images[0], r['rois'], r['masks'], r['class_ids'],class_names, r['scores'])
#     display.display_instances(image, r['rois'], r['masks'], r['class_ids'],class_names, r['scores'],name=f)

# print(0)
