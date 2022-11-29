# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# This work is licensed under the Creative Commons Attribution-NonCommercial
# 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to
# Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

"""Minimal script for generating an image using pre-trained StyleGAN generator."""

import os
from pathlib import Path
import numpy as np
import PIL.Image
import config
import time
import fingerprint_enhancer
import cv2 as cv

def main():
    # Initialize TensorFlow.
    enhanced_dir = 'enhanced_images'

    # create folder if not exist
    os.makedirs(enhanced_dir, exist_ok=True)

    pathlist = Path('synthetic_data').glob('*.png')

    for path in pathlist:
        print('file name : ', path)

        img = cv.imread(str(path), 0)

        out = fingerprint_enhancer.enhance_Fingerprint(img)

        # cv.imshow('enhanced image', out)

        new_path = enhanced_dir + '/' + str(path).split('/')[1]

        cv.imwrite(new_path, out)

if __name__ == "__main__":
    main()
