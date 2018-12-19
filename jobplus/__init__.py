from flask import Flask, render_template
from .config import configs
from flask_migrate import Migrate
from .models import db


def register_blueprints(app):
    from .handlers import front, admin, company, job, user
    app.register_blueprint(front)
    app.register_blueprint(admin)
    app.register_blueprint(company)
    app.register_blueprint(job)
    app.register_blueprint(user)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])
#    configs[config_name].init_app(app)
    db.init_app(app)
    Migrate(app=app, db=db)
    register_blueprints(app)
    return app


# 错误处理
def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

