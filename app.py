from flask import Flask, app
from api.routes import get_routes
from threading import Thread

app = Flask(__name__)


get_routes(app)
 
if __name__ == '__main__':
    app.run(debug=True)
