#!/usr/bin/python3
#import roboctrl.ctrl as ctrl
import os
import sys
import cv2
import numpy as np
import time
import argparse
import threading as Thread

from tflite_runtime.interpreter import Interpreter
from tflite_runtime.interpreter import load_delegate
