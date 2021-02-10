from flask import Flask, jsonify, request
from functools import wraps
import re



def check_for_token(func):
    pass