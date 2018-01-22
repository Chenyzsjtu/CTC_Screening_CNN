from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
class PARAMETERS:
    MOVING_AVERAGE = 0.999
    INITIAL_LEARNING_RATE = 0.0001  #1e-4
    TYPEA = 0
    TYPEB = 0.001
    #TRUE_SAMPLE_RATIO = 1
    IF_CONTINUE = 1

    LOG_FREQUENCY = 20
    LOG_DEVICE_PLACEMENT = False
    MAX_STEPS = 10000
    SESS_FIRST_STEPS = 1000
    BATCH_SIZE = 16
    ROTATE_GPU = 1
    NUM_GPUS = 2
Parameters = PARAMETERS()

import sys
import os
sys.path.append(os.path.join(os.getcwd(),".."))
import tensorflow as tf
from dataDirectory import DataDirectory
from screen_cnn import inference
from ctc_screen_train_multi_gpu import train as screen_train
from model_train import getloss

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--fold", type=int, help='which cross validation fold')
FLAGS = parser.parse_args()




def main(argv=None):  # pylint: disable=unused-argument
    dataDirectory = DataDirectory()
    dataDirectory.cross_index = FLAGS.fold
    train_dir = os.path.join(dataDirectory.get_current_model_dir(), dataDirectory.checkpoint_fold)
    database_dir = dataDirectory.data_base_dir()
    record_file_dir = dataDirectory.get_current_train_record_dir()

    IF_CONTINUE_TRAIN = Parameters.IF_CONTINUE == 1
    if (not IF_CONTINUE_TRAIN) and tf.gfile.Exists(train_dir):
        tf.gfile.DeleteRecursively(train_dir)
    tf.gfile.MakeDirs(train_dir)
    print(train_dir)
    print(record_file_dir)
    print(database_dir)
    screen_train(train_dir, record_file_dir, database_dir, inference, getloss, Parameters)

if __name__ == '__main__':
    tf.app.run()

