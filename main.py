import sys
import argparse
import utilities as ut

import numpy as np

import methods
import pylab as pl
from io import BytesIO


def run_main(method, fs_functions,  score_name, n_clfs=5, dataset_name="ant"):

    print("\nDATASET: %s\nMETHOD: %s\n" % (dataset_name, method))
    np.random.seed(1)

    ##### 1. ------ GET DATASET
    X, y, ft_names = ut.read_dataset("datasets/", dataset_name=dataset_name)
    ##### 2. ------- RUN TRANING METHOD
    methods.run_method(method, X, y, n_clfs=n_clfs,
                       fs_functions=fs_functions,
                       score_name=score_name)
    pl.title(dataset_name)
    pl.ylabel(score_name)

    pl.legend(loc="best")
    img = BytesIO()
    pl.savefig(img)
    img.seek(0)
    return img

