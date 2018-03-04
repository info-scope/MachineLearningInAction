import numpy as np


class BatchGenerator(object):
    """ Construct a Data generator. The input X, y should be ndarray or list like type.

    Example:
        >>> Data_train = BatchGenerator(X=X_train_all, y=y_train_all, shuffle=True)
        >>> Data_test = BatchGenerator(X=X_test_all, y=y_test_all, shuffle=False)
        >>> X = Data_train.X
        >>> y = Data_train.y
        or:
        >>> X_batch, y_batch = Data_train.next_batch(batch_size)
     """

    # noinspection PyPep8Naming
    def __init__(self, X: np.ndarray, y: np.ndarray, shuffle=False):
        self._X = X
        self._y = y
        self._epochs_completed = 0
        self._index_in_epoch = 0
        self._number_examples = self._X.shape[0]
        self._shuffle = shuffle
        if self._shuffle:
            new_index = np.random.permutation(self._number_examples)
            self._X = self._X[new_index]
            self._y = self._y[new_index]

    @property
    def X(self):
        return self._X

    @property
    def y(self):
        return self._y

    @property
    def num_examples(self):
        return self._number_examples

    @property
    def epochs_completed(self):
        return self._epochs_completed

    def next_batch(self, batch_size):
        """ Return the next 'batch_size' examples from this data set."""
        start = self._index_in_epoch
        self._index_in_epoch += batch_size
        if self._index_in_epoch > self._number_examples:
            # finished epoch
            self._epochs_completed += 1
            # Shuffle the data
            if self._shuffle:
                new_index = np.random.permutation(self._number_examples)
                self._X = self._X[new_index]
                self._y = self._y[new_index]
            start = 0
            self._index_in_epoch = batch_size
            assert batch_size <= self._number_examples
        end = self._index_in_epoch
        return self._X[start:end], self._y[start:end]
