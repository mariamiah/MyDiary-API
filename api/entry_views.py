from flask import Blueprint, jsonify, request, json
from api.models import Entry
from datetime import datetime


entry = Blueprint('entry', __name__)

entries = []


@entry.route('/api/v1/entries', methods=['POST'])
def create_entry():
    data = request.get_json()

    if data['entry_text'] == "":
        return jsonify({'message': "Enter entry_text"}), 400

    try:
        if isinstance(data['entry_text'], str):
            entry_id = len(entries)
            entry_id += 1
            date_created = datetime.now()
            entry = Entry(entry_id, date_created, data['entry_text'])
            entries.append(entry)
        return jsonify({"Message": "Entry added successfully"}), 201
    except ValueError:
        return jsonify({"Message": "Invalid fields"}), 400
