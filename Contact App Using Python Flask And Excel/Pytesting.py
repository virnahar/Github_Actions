from app import app


def testmainapp():
    response = app.test_client().get('/')
    assert response.status_code == 200
