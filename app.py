from flask import Flask
from api.routes import api
from website.routes import site

app = Flask(__name__)

app.register_blueprint(api)
app.register_blueprint(site)

app.run(debug=True)