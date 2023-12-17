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

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain)+1,
            'timestamp': time.time(),
            'proof': proof,
            'previous_hash': previous_hash,
            'transactions': self.transactions
        }
        # Reset for the next block
        self.transactions = []
        self.chain.append(block)
        return block

    def get_previous_block(self,):
        return self.chain[-1]
