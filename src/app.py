"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from datastructures import FamilyStructure
# from models import Person

app = Flask(__name__)

jackson_family = FamilyStructure('Jackson')

# Miembros iniciales de la familia
jackson_family.add_member({'first_name': 'John', 'age': 33, 'lucky_numbers': [7, 13, 22]})
jackson_family.add_member({'first_name': 'Jane', 'age': 35, 'lucky_numbers': [10, 14, 3]})
jackson_family.add_member({'first_name': 'Jimmy', 'age': 5, 'lucky_numbers': [1]})

@app.route('/members', methods=['GET'])
def get_all_members():
    return jsonify(jackson_family.get_all_members())

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member)
    else:
        return jsonify({'error': 'Miembro no encontrado'}), 404

@app.route('/members', methods=['POST'])
def add_member():
    member = request.json
    if 'first_name' in member and 'age' in member and 'lucky_numbers' in member:
        jackson_family.add_member(member)
        return jsonify(member), 200
    else:
        return jsonify({'error': 'Datos inválidos'}), 400

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    if jackson_family.delete_member(member_id):
        return jsonify({'done': True})
    else:
        return jsonify({'error': 'Miembro no encontrado'}), 404



# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)

   

