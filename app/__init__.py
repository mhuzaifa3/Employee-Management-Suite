from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "dev"),
        SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL", f"sqlite:///{os.path.join(app.instance_path, 'employees.db')}"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config:
        app.config.update(test_config)

    # Ensure instance folder exists (for SQLite file)
    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)

    from .models import Employee  # noqa

    with app.app_context():
        db.create_all()

    from .employees import bp as employees_bp
    app.register_blueprint(employees_bp, url_prefix="/employees")

    @app.get("/")
    def root():
        from flask import redirect, url_for
        return redirect(url_for("employees.index"))

    return app
