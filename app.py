from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# In-memory store for level (use a DB or file in production)
level_store = {"level": 0}

# parsing validator (hopefully)
def force_valid_range(value):
    """Validator for 0-100 range."""
    num = int(value)
    if num <= 0:
        num = 0
    elif num > 100:
        num = 100
    return num

class Level(Resource):
    def get(self):
        """Return the current level value."""
        return {"level": level_store["level"]}

    def post(self):
        """Set the level to an integer value."""
        parser = reqparse.RequestParser()
        parser.add_argument(
            "level", 
            type=force_valid_range,
            required=True, 
            help="level must be an integer between 0 and 100"
            )

        args = parser.parse_args()
        level_store["level"] = args["level"]
        return {"level": level_store["level"]}, 201


api.add_resource(Level, "/level")


@app.route("/")
def index():
    """Display the level in an HTML page."""
    return render_template("level.html", level=level_store["level"])


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5000)
