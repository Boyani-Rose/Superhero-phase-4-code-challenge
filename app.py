from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return '<h1>Superheroes API</h1>'


@app.route('/heroes')
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name
    } for hero in heroes])


@app.route('/heroes/<int:id>')
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "hero_powers": [
            {
                "id": hp.id,
                "hero_id": hp.hero_id,
                "power_id": hp.power_id,
                "strength": hp.strength,
                "power": {
                    "id": hp.power.id,
                    "name": hp.power.name,
                    "description": hp.power.description
                }
            } for hp in hero.hero_powers
        ]
    })


@app.route('/powers')
def get_powers():
    powers = Power.query.all()
    return jsonify([{
        "id": power.id,
        "name": power.name,
        "description": power.description
    } for power in powers])


@app.route('/powers/<int:id>')
def get_power_by_id(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    return jsonify({
        "id": power.id,
        "name": power.name,
        "description": power.description
    })


@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    description = data.get("description")

    if not description or len(description) < 20:
        return jsonify({"errors": ["validation errors"]}), 400

    power.description = description
    db.session.commit()

    return jsonify({
        "id": power.id,
        "name": power.name,
        "description": power.description
    })


@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    strength = data.get("strength")
    hero_id = data.get("hero_id")
    power_id = data.get("power_id")

    if strength not in ["Strong", "Weak", "Average"]:
        return jsonify({"errors": ["validation errors"]}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return jsonify({"errors": ["validation errors"]}), 400

    hero_power = HeroPower(strength=strength, hero=hero, power=power)
    db.session.add(hero_power)
    db.session.commit()

    return jsonify({
        "id": hero_power.id,
        "hero_id": hero_power.hero_id,
        "power_id": hero_power.power_id,
        "strength": hero_power.strength,
        "hero": {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        },
        "power": {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
    }), 201

if __name__ == '__main__':
    app.run(port=5555, debug=True)