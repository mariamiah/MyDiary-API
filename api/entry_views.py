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


@entry.route('/api/v1/entries', methods=['GET'])
def fetch_all():
    """This endpoint fetches all entries"""
    Entries = [entry.toJSON() for entry in entries]
    return jsonify({'Entries': Entries}), 200


@entry.route('/api/v1/entries/<int:entry_id>', methods=['GET'])
def fetch_one(entry_id):
    single_entry = []
    if entry_id == 0 or entry_id > len(entries):
        return jsonify({"message": "Index out of range"}), 400

    if entry_id != 0 and entry_id <= len(entries):
        Entry = entries[entry_id - 1]
        single_entry.append(Entry.toJSON())
        return jsonify({'Order': single_entry, 'status': 'Succeeded'}), 200


@entry.route('/api/v1/entries/<int:entry_id>', methods=['PUT'])
def modify_entry(entry_id):
    if entry_id == 0 or entry_id > len(entries):
        return jsonify({"message": "Index is out of range"})
    data = request.get_json()
    for entry in entries:
        if int(entry.entry_id) == int(entry_id):
            entry.entry_text = data['entry_text']     
    return jsonify({'message': "successfully updated"}), 200
