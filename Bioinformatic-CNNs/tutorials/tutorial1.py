# Import statements
import os
from time import time
from IPython.display import Image
from pysster.Data import Data
from pysster.Model import Model
from pysster.Grid_Search import Grid_Search
from pysster import utils

# Generate a folder to hold the output
output_folder = "pysster_output/"

# Check to see if the output directory is in our path.
# If it is not, generate the output folder
if not os.path.isdir(output_folder):
    os.makedirs(output_folder)
    
# Make sure tensorflow is installed and that our gpu is accessible
import tensorflow as tf
print("TensorFlow version: "+ tf.__version__)
print("Current GPU used: "+ tf.test.gpu_device_name())
# This should return something like
# TensorFlow version: 1.12.0
# Current GPU used: /device:GPU:0
# If it returns GPU:0, the Jupyter notebook isn't recognizing your GPU.

# Import the data using the ACGU alphabet for RNA and HIMS for proteins

data = Data(["data/alu.fa.gz",
             "data/rep.fa.gz"], ("ACGU", "HIMS")) 


print(data.get_summary())