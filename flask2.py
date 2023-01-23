# -*- coding: utf-8 -*-
"""Untitled50.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KbDprsMj73IQIbD6MMyQKGlnInlmakwK
"""

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)