
from app.views.first import first


def init_view(app):
    app.register_blueprint(first)