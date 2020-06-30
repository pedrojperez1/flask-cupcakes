"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'oh-so-secret'

connect_db(app)

@app.route('/api/cupcakes')
def get_all_cupcakes():
    """returns data on all cupcakes"""
    cupcakes = Cupcake.query.all()
    res = [c.serialize() for c in cupcakes]
    return jsonify(cupcakes=res)

@app.route('/api/cupcakes/<int:c_id>')
def get_cupcake_details(c_id):
    """returns data on single cupcake"""
    cupcake = Cupcake.query.get_or_404(c_id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """creates new cupcake and return data on new cupcake"""
    flavor = request.json.get('flavor')
    size = request.json.get('size')
    rating = request.json.get('rating')
    image = request.json['image'] if request.json.get('image') else None
    print(image)
    print(image is None)
    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()
    res = jsonify(cupcake=new_cupcake.serialize())
    return (res, 201)

@app.route('/api/cupcakes/<int:c_id>', methods=['PATCH'])
def update_cupcake(c_id):
    """updates cupcake"""
    cupcake = Cupcake.query.get_or_404(c_id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:c_id>', methods=['DELETE'])
def delete_cupcake(c_id):
    """deleted cupcake"""
    cupcake = Cupcake.query.get_or_404(c_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")

@app.route('/')
def show_index():
    return render_template('index.html')