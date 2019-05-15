from matplotlib import pyplot as plt
from math import sqrt
import glob
from skimage.io import imread
example_file = glob.glob(r"wint_sky.gif")[0]
im = imread(example_file, as_grey=True)
plt.imshow(im)
plt.show()
blobs_log = blob_log(im, max_sigma=30, num_sigma=10, threshold=.1)
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
numrows = len(blobs_log)
print("Number of stars counted : " ,numrows)
fig, ax = plt.subplots(1, 1)
plt.imshow(im)
for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r+5, color='lime', linewidth=2, fill=False)
    ax.add_patch(c)