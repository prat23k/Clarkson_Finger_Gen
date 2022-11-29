import matplotlib.pyplot as plt
import os
import glob
import PIL.Image
import numpy as np

# print('Loading images from "%s"' % image_dir)
image_filenames = sorted(glob.glob(os.path.join('./stylegan_K1/datasets/', '*.png')))
if len(image_filenames) == 0:
    error('No input images found')

img = PIL.Image.open(image_filenames[5]).convert('RGB')

img.show(title='rgb image')
# img.show()
img = np.asarray(img)
img = img/255.
print(img[:25, :25, 2])
# plt.imshow(img)
# plt.show()
