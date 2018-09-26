from flask import Flask
from api.entry_views import entry
from api.user_views import user

app = Flask(__name__)
app.register_blueprint(entry)
app.register_blueprint(user)
