import os
from collections import OrderedDict

from PIL import Image

from lavis.datasets.datasets.base_dataset import BaseDataset

import json
import copy

class TaiwanCaptionDatasets(BaseDataset):
    def __init__(self, vis_processor, text_processor, vis_root, ann_paths):
        """
        vis_root (string): Root directory of images (e.g. coco/images/)
        ann_root (string): directory to store the annotation file
        """
        
        self.vis_root = vis_root
        self.images_info = {}
        
        self.annotation = []
        for ann_path in ann_paths:
            images = json.load(open(ann_path, "r", encoding="utf-8"))
            for image in images:
                self.annotation.append(images[image])
                
        self.vis_processor = vis_processor
        self.text_processor = text_processor
        print("annotation:", self.annotation)

    def __getitem__(self, index):
        ann = self.annotation[index]

        image_path = os.path.join(self.vis_root, "ID"+ann["id"]+".jpg")
        image = Image.open(image_path).convert("RGB")

        image = self.vis_processor(image)

        return {
            "image" : image, 
            "image_id" : ann["id"],
            "text_input": ann["introduction"]
        }