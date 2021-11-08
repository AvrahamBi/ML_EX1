# Avraham Bar Ilan 205937949

import sys
import matplotlib.pyplot as plt
import numpy as np

# dist = distance3D(pixels[0], pixels[1])
def distance3D(a, b):
    a = np.array([float(a[0]), float(a[1]), float(a[2])])
    b = np.array([float(b[0]), float(b[1]), float(b[2])])
    return np.linalg.norm(a - b)

def main():
    # python ex1.py <image path> <centroids init path> <output>
    image_fname, centroids_fname, out_fname = sys.argv[1], sys.argv[2], sys.argv[3]
    z = np.loadtxt(centroids_fname)  # load centroids
    orig_pixels = plt.imread(image_fname)
    pixels = orig_pixels.astype(float) / 255.
    # Reshape the image(128x128x3) into an Nx3 matrix where N = number of pixels.
    pixels = pixels.reshape(-1, 3)

    # open centroids file
    with open(centroids_fname) as file:
        centroids = file.readlines()
        centroids = [line.rstrip().split(" ") for line in centroids]
    file.close()

    # dist = distance3D(pixels[0], pixels[1])
    # each cluster contains the points of the centroids
    clusters = []
    for centroid in centroids:
        cluster = []
        clusters.append(cluster)

    #print(dist)
    isChanged = True
    iterations = 0
    while(isChanged and iterations < 20):
       # iterations += 1
        iterations += 99                                                                             # TODO delete
       # divide the pixels to clusters
        for pixel in pixels:
            min = distance3D(centroids[0], pixel)
            closestCentroidIndex = 0
            x = 0
            for centroid in centroids:
                dist = distance3D(centroid, pixel)
                if (dist < min):
                    min = dist
                    closestCentroidIndex = x
                x += 1
            clusters[closestCentroidIndex].append(pixel)
        # compute new location for each centroid














if __name__ == "__main__":
    main()


