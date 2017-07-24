from flask import Flask, request, jsonify, abort, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# -- Create app ---------------------------------------------------------------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# -- Create models ------------------------------------------------------------
db = SQLAlchemy(app)

class Attendee(db.Model):
    __tablename__ = 'attendees'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return 'Attendee(first_name={}, last_name={})'.format(
            self.first_name,
            self.last_name
        )

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

db.create_all()


# -- Setup routes -------------------------------------------------------------
@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('all_attendees'))


@app.route('/attendees', methods=['GET'])
def all_attendees():
    attendees = Attendee.query.all()
    return jsonify({'attendees': [attendee.to_dict() for attendee in attendees]})


@app.route('/attendees', methods=['POST'])
def create_attendee():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')

    if not (first_name and last_name):
        return jsonify({'error': 'first_name and last_name are required'}), 400
 
    attendee = Attendee(first_name=first_name, last_name=last_name)
    db.session.add(attendee)
    db.session.commit()

    return jsonify({'attendee': attendee.to_dict()}), 201


@app.route('/attendees/<int:attendee_id>', methods=['PUT'])
def update_attendee(attendee_id):
    attendee = Attendee.query.get_or_404(attendee_id)

    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')

    if not (first_name and last_name):
        return jsonify({'error': 'first_name and last_name are required'}), 400
 
    attendee.first_name = first_name
    attendee.last_name = last_name

    db.session.add(attendee)
    db.session.commit()

    return jsonify({'attendee': attendee.to_dict()}), 200


@app.route('/attendees/<int:attendee_id>', methods=['DELETE'])
def delete_attendee(attendee_id):
    attendee = Attendee.query.get_or_404(attendee_id)
    db.session.delete(attendee)
    db.session.commit()

    return '', 204


# -- Light 'er up -------------------------------------------------------------
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

