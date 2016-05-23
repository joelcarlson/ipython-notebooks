import numpy as np
from sklearn import datasets
import random
import hashlib


def euclidean_dist(vec, arr):
    '''
    returns np array of euclidean distances
    each row is the distance between the vector
    and the respective row in the array
    '''
    if not vec.shape[0] == arr.shape[1]:
        raise ValueError('Vector and array must have same dimension')
    return np.sqrt(np.sum((vec - arr)**2, axis=1))


class Kmeans(object):

    '''
    Implementation of the Kmeans algorithm

    Usage:
    KmeansModel = Kmeans()
    KmeansModel.fit(data)
    print Kmeans
    predictions = KmeansModel.results
    '''
    def __init__(self, k=10, num_iter=100, dist_func=euclidean_dist, random_state=10, score=False):
        """
        Initialize Kmeans object given k clusters
        Parameters
        -----------
        k: integer
            The number of seeds to choose
        num_iter: integer
            Number of iterations to run the kmeans algorithm
        dist_func: function object
            A distance function which take as it's first positional argument
            a 1D numpy array, and a 2D numpy array as it's second. Should
            return a numpy array of distances between the vector and the array
        random_state: integer
            random state to pass in to random.seed()
        score: boolean
            compute the sum of squared errors at each iteration

        Notes
        -----
        Regardless of num_iter, the algorithm will end if the classes do not change
        between iterations
        """
        self.k = k
        self.num_iter = num_iter
        self.dist_func = dist_func
        self.random_state = random_state
        self.score = score
        self.data = None


    def fit(self, data):
        """
        Run the Kmeans algorithm
        Parameters
        -----------
        data: array or sparse matrix, shape (n_samples, n_features)
            The data to find centroids for

        Notes
        -----
        Selects initial cluster centers by randomly sampling
        k points from the data
        """
        self.data = data
        self.centroids = self._initialize_centroids()
        self.results = np.zeros(len(data))
        self.iterscore = np.zeros(self.num_iter)
        self.iter_converged = len(data)
        #Store hash of results to compare
        hash_before = hashlib.sha1(self.results.view(np.uint8)).hexdigest()

        for iteration in range(self.num_iter):
            if self.score:
                # All remaining iterscores get changed
                # If the algorithm quits before num_iter
                # we dont want the scores to be 0!
                self.iterscore[iteration:] = self._score()
            self._get_nearest_centroids()
            self._update_centroid_locations()

            # Check if classes changed
            hash_after = hashlib.sha1(self.results.view(np.uint8)).hexdigest()
            if hash_before == hash_after:
                self.iter_converged = iteration
                break
            else:
                hash_before = hash_after

    def __repr__(self):
        if self.data is None:
            return "Kmeans model not yet fit"
        return "Kmeans model fit!\
        \n Final SSE: {} \
        \n Converged in: {} iterations".format(round(self._score(),3), self.iter_converged)

    def _initialize_centroids(self):
        random.seed(self.random_state)
        # Randomly sample k centroid locations from the existing data
        centroids = self.data[random.sample(np.arange(0, len(self.data)), self.k )]
        return centroids

    def _get_nearest_centroids(self):
        for row, vec in enumerate(self.data):
            # Update results (classes of observations in data)
            self.results[row] = np.argmin(self.dist_func(vec, self.centroids))

    def _update_centroid_locations(self):
        for cluster in range(self.k):
            # Set centroid to be mean over all observations in that centroids cluster
            self.centroids[cluster] = self.data[self.results == cluster].mean(axis=0)

    def _score(self):
        # This is the distance of each point to its final centroid,
        # squared, and summed over all data points.
        scores = np.zeros(len(self.data))
        for row, vec in enumerate(self.data):
            # euclidean distance
            scores[row] = np.sqrt(np.sum(self.data[row] - self.centroids[int(self.results[row])])**2)
        return np.sum(scores)






if __name__ == "__main__":
    print "Kmeans!"
    data = datasets.load_iris().data
    mod = Kmeans(score=True)
    print mod
    mod.fit(data)
    print mod
