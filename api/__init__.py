from flask import Flask
from api.entry_views import entry
from api.user_views import user
from api.diary_views import diary

app = Flask(__name__)
app.register_blueprint(entry)
app.register_blueprint(user)
app.register_blueprint(diary)
