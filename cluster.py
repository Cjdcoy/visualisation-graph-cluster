#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def main(MONTH=1, YEAR=2017):
    #here we load the dataset
    print("loading graph" + './graphs/' + str(MONTH) + '-' + str(YEAR) + '.csv ...')
    dataset = pd.read_csv('./graphs/' + str(MONTH) + '-' + str(YEAR) + '.csv')

    X = dataset.values
    D= []
    # always assume the max number of cluster would be 10
    print("computing best nb cluster with elbow method...")
    for i in range(1, 10):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
        kmeans.fit(X)
        D.append(kmeans.inertia_) # Inertia: Sum of distances of samples to their closest cluster center

    # Display the ELBOW method to get the optimal value of K
    print("elbow method accomplished, close window to proceed to cluster computation.")
    plt.plot(range(1, 10), D)
    plt.title('Elbow method')
    plt.xlabel('nb of clusters')
    plt.ylabel('distortion')
    plt.savefig('./figs/' + str(MONTH) + '-' + str(YEAR) + '-elbow.pdf')
    plt.show()

    print("computing clusters...")
    # If you zoom out this curve then you will see that last elbow comes at k=

    # build model
    model = KMeans(n_clusters=5, init='k-means++', random_state=0)
    yKmeans = model.fit_predict(X)

    plt.scatter(X[yKmeans == 0, 0], X[yKmeans == 0, 1], s=2, c='black')
    plt.scatter(X[yKmeans == 1, 0], X[yKmeans == 1, 1], s=2, c='blue')
    plt.scatter(X[yKmeans == 2, 0], X[yKmeans == 2, 1], s=2, c='cyan')
    plt.scatter(X[yKmeans == 3, 0], X[yKmeans == 3, 1], s=2, c='green')
    plt.scatter(X[yKmeans == 4, 0], X[yKmeans == 4, 1], s=2, c='red')

    # clusters to csv
    df = pd.DataFrame(X, yKmeans)
    df.to_csv('./clusters/' + str(MONTH) + '-' + str(YEAR) + '.csv', index_label="cluster_nb, longitude, latitude")

    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=50, c='yellow', label='Centroids')
    plt.title('Crimes in vancouver (date: ' + str(MONTH) + '/' + str(YEAR) + ', number: ' + str(len(X)) + ')')
    plt.xlabel('latitude')
    plt.ylabel('longitude')
    plt.legend()
    plt.savefig('./figs/' + str(MONTH) + '-' + str(YEAR) + '-clusters.pdf')
    print("Wrote clusters into " + './clusters/' + str(MONTH) + '-' + str(YEAR) + '.csv')
    plt.show()

    return 0


if __name__ == "__main__":
    #MIN DATE (MM/YY): 01/2003
    #MAX DATE (MM/YY): 06/2017
    YEAR = 2003
    MONTH = 1
    main(MONTH, YEAR)
