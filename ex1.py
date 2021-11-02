# Avraham Bar Ilan 205937949

import sys
import matplotlib.pyplot as plt
import numpy as np




def main():
    # python ex1.py <image path> <centroids init path> <output>
    image_fname, centroids_fname, out_fname = sys.argv[1], sys.argv[2], sys.argv[3]
    z = np.loadtxt(centroids_fname)  # load centroids
    orig_pixels = plt.imread(image_fname)
    pixels = orig_pixels.astype(float) / 255.
    # Reshape the image(128x128x3) into an Nx3 matrix where N = number of pixels.
    pixels = pixels.reshape(-1, 3)










if __name__ == "__main__":
    main()


