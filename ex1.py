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
    open(out_fname, 'w').close() # todo maybe delete
    # open centroids file
    with open(centroids_fname) as file:
        centroids = file.readlines()
        centroids = [line.rstrip().split(" ") for line in centroids]
    file.close()

    # each cluster contains the points of the centroids
    clusters = []
    for centroid in centroids:
        cluster = []
        clusters.append(cluster)

    isChanged = True
    iterations = 0
    lossPerIteration = []
    while(isChanged and iterations < 20):
        loss = 0 # TODO
        # nullify the clusters
        for cluster in clusters:
            #cluster = []
            cluster.clear()
        isChanged = False
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
            loss += (min * min)
        loss /= len(pixels)
        loss = round(loss, 7)
        lossPerIteration.append(loss)
        print(loss)
        #
        # compute new location for each centroid
        for i in range(len(clusters)):
            if (len(clusters[i]) == 0):
                continue
            newValues = []
            for j in range(len(pixels[0])):
                average = 0
                for pixel in clusters[i]:
                  average += float(pixel[j])
                #if (len(clusters[i]) != 0):
                average /= len(clusters[i])
                newValues.append(round(average, 4))
                #
            for k in range(len(newValues)):
                currentCentroid = centroids[i]
                if (currentCentroid[k] != newValues[k]):
                    isChanged = True
                    centroids[i] = newValues
        # create the string to write to the output file
        outputLine = "[iter " + str(iterations) + "]:"
        for centroid in centroids:
            v = "["
            for value in centroid:
                v += str(value) + " "
            v = v[:-1]
            v += "],"
            outputLine += v
        outputLine = outputLine[:-1]
        outputLine += "\n"
        out = open(out_fname, "a")
        out.write(outputLine)
        out.close()
        iterations += 1
    numbers = []
    for i in range(iterations):
        numbers.append(i)
    plt.plot(numbers, lossPerIteration)
    plt.xlabel("iterations")
    plt.ylabel("Avg Loss")
    plt.title("K = " + str(len(centroids)))
    plt.show()



if __name__ == "__main__":
    main()


