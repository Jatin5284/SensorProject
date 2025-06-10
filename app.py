from flask import flask ,render_template ,jsonify , request ,send_file
from src.exception import CustomException
from src.logger import logging
import os , sys

from src.pipeline.train_pipeline import *
from src.pipeline.predict_pipeline import * 