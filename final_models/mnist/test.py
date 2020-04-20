import tensorflow as tf
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist.load_data()

mnist_train, test_dataset = mnist


