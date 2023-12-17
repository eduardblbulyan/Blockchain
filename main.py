import hashlib
import time
import json
from flask import Flask, jsonify, request
from urllib.parse import urlparse
import requests


class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof=1, previous_hash='0')
        self.nodes = set()
