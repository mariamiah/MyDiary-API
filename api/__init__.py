from flask import Flask

app = Flask(__name__)

entries = []
known_entry_ids = []
