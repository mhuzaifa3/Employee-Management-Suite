from app import create_app, db


def setup_app():
    return create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite://",
        "WTF_CSRF_ENABLED": False
    })


def test_index_200():
    app = setup_app()
    with app.app_context():
        db.create_all()
    client = app.test_client()
    r = client.get("/employees/")
    assert r.status_code == 200


def test_create_flow():
    app = setup_app()
    with app.app_context():
        db.create_all()
    client = app.test_client()
    r = client.post("/employees/", data={"name": "Ada", "salary": "12345"})
    assert r.status_code in (302, 303)
    r = client.get("/employees/")
    assert b"Ada" in r.data
