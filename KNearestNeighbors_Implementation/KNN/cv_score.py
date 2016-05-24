# Ad-hoc cross validation function
from random import shuffle, seed
import numpy as np

def cv_score(model, X, y, n_folds=5, random_state=10):
    scores = []
    seed(random_state)

    # Get indices for each fold
    indices = range(len(X))
    step_size = len(indices)/n_folds
    shuffle(indices)
    folds = np.array_split(np.array(indices), n_folds)

    # Run n_fold cross validation
    for idx, fold in enumerate(folds):
        testing = fold
        training = np.hstack(np.delete(folds, idx))

        model.fit(X[training], y[training])
        preds = model.predict(X[testing])
        scores.append(np.sum(preds == y[testing])/float(len(fold)))

    return scores
