from flask import Flask
from routes.routes import krs_bp

app = Flask(__name__)

app.register_blueprint(krs_bp)

if __name__ == "__main__":
    app.run(debug=True)
