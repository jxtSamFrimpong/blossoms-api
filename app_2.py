from flask import Flask, request
import resource, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
db.create_all()

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description= db.Column(db.String(200))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/')

def index():
    return 'Hello!'

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()

    output = []
    for drink in drinks:
        data = {
            'name':drink.name,
            'description':drink.description
        }
        output.append(data)


    return {
        'drinks':output
    }

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)

    return {
        'name': drink.name,
        'description': drink.description
    }

@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(
        name = request.json['name'],
        desription=request.json['description']
    )
    db.session.add(drink)
    db.commit()

    return {
        'id':drink.id
    }

if __name__=='__main__':
    app.run(debug=True)