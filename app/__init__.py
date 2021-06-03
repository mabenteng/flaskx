from flask import Flask
from app.ext import init_ext
from app.views import init_view
from app.settings import envs

def create_app(env):
    app=Flask(__name__)
    app.config.from_object(envs.get(env))
    init_ext(app)
    init_view(app)
    return app