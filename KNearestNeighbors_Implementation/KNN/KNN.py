import pandas as pd
import numpy as np
from scipy import stats


class KNearestNeighbors(object):

    def __init__(self, k, distance):
        self.k = k
        self.distance = distance

    def fit(self, X, y):
        '''fit: Saves the data for making predictions

        Input
        ------
        X np.array
          Feature matrix
        y np.array
          Class labels

        Output
        ------
        None
        '''
        self.old_X = X
        self.old_y = y

    def predict(self, X):
        '''predict: Calculate predictions for each data point

        Input
        ------
        X np.array
          New feature matrix to make predictions on

        Output
        ------
        1d np.array of predictions

        Method:
            for every point in the dataset:
                calculate the distance between the point and x
                sort the distances in increasing order
                take the k items with the smallest distances to x
            return the majority class among these items
        '''
        self.predictions = np.zeros(X.shape[0])
        i=0
        for row in X:
            #For each row, calc distance to each point in data
            dists = np.apply_along_axis(func1d = self.distance,
                                axis = 1,
                                arr = self.old_X, B=row)
            #append classes
            dists = np.array((dists, self.old_y)).T

            #sort by distance, keep mode of top k values
            self.predictions[i] = stats.mode(dists[dists[:,0].argsort(), 1][0:self.k]).mode
            i+=1
        return self.predictions

    def score(self, y, preds):
        scores = pd.DataFrame(y,preds).reset_index().rename(columns={'index':'y', 0:'preds'})
        #sens  = TP / TP+FN
        TP = float(scores[(scores.y == 1) & (scores.preds == 1)].count()[0])
        FN = scores[(scores.y == 1) & (scores.preds == 0)].count()[0]
        self.sensitivity = TP / (TP+FN)

        #spec = TN / TN + FP
        TN = float(scores[(scores.y == 0) & (scores.preds == 0)].count()[0])
        FP = scores[(scores.y == 0) & (scores.preds == 1)].count()[0]
        self.specificity = TN / (TN + FP)

        return self.sensitivity, self.specificity


def euclidean_dist(A,B):
    '''Compute euclidean distance

    Input
    ------
    A np.array
    B np.array

    Output
    ------
    float
    '''

    return np.sqrt(np.sum((A - B)**2))

if __name__ == "__main__":

    knn = KNearestNeighbors(1, euclidean_distance)
    knn.fit(X[0:50],y[0:50])
    preds = knn.predict(X[51:])
    knn.score(y[51:], preds)
