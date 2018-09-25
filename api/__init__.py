from flask import Flask
from api.entry_views import entry

app = Flask(__name__)
app.register_blueprint(entry)
