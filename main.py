from flask import Flask
from config.database import Base, engine
from models import libros_model
from controllers.libros_controller import libros_bp


Base.metadata.create_all(bind=engine)


app = Flask(__name__)


app.register_blueprint(libros_bp)

if __name__ == "__main__":
    app.run(debug=True)
