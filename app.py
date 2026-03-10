from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# In-memory store for level (use a DB or file in production)
""" 
level - 0-100 integer representing percentage of full
mode - can be either fill | drain
"""
tank_state = {'level': 0,'mode': "drain"}

# parsing validator (hopefully)
def force_valid_range(value):
    """Validator for 0-100 range."""
    num = int(value)
    if num <= 0:
        num = 0
    elif num > 100:
        num = 100
    return num

class Fill(Resource):
    def get(self):
        """Return the current level value."""
        tank_state['mode'] = 'fill'
        return {'level': tank_state['level'],'mode': tank_state['mode']}
    
    def post(self):
        """Add water to the tank, minimum 1% or integer 1"""
        parser = reqparse.RequestParser()
        parser.add_argument(
            'delta_level', 
            type=force_valid_range,
            required=True, 
            help="delta_level must be an integer between 0 and 100"
            )
        args = parser.parse_args()
        tank_state['mode'] = 'fill'
        tank_state['level'] = force_valid_range(tank_state['level'] + args['delta_level'])
        return {'level': tank_state['level'],'mode': tank_state['mode']}, 201


class Drain(Resource):
    def get(self):
        """Return the current level value."""
        tank_state['mode'] = "drain"
        return {'level': tank_state['level'],'mode': tank_state['mode']}
    
    def post(self):
        """Drain water from the tank, minimum 1% or integer 1"""
        parser = reqparse.RequestParser()
        parser.add_argument(
            'delta_level', 
            type=force_valid_range,
            required=True, 
            help="delta_level must be an integer between 0 and 100"
            )
        args = parser.parse_args()
        tank_state['mode'] = "drain"
        tank_state['level'] = force_valid_range(tank_state['level'] - args['delta_level'])
        return {'level': tank_state['level'],'mode': tank_state['mode']}, 201


class Level(Resource):
    def get(self):
        """Return the current level value."""
        return {'level': tank_state['level'],'mode': tank_state['mode']}

    def post(self):
        """Set the level to an integer value."""
        parser = reqparse.RequestParser()
        parser.add_argument(
            'level', 
            type=force_valid_range,
            required=True, 
            help="level must be an integer between 0 and 100"
            )

        args = parser.parse_args()
        tank_state['level'] = args['level']
        return {'level': tank_state['level'],'mode': tank_state['mode']}, 201


api.add_resource(Level, '/level')
api.add_resource(Fill,'/fill')
api.add_resource(Drain,'/drain')


@app.route('/')
def index():
    """Display the level in an HTML page."""
    return render_template("watertank.html", level=tank_state['level'],mode=tank_state['mode'])


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)
