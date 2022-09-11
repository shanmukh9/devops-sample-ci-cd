from app import app
<<<<<<< HEAD
=======


>>>>>>> 2b4009cc9831c21e7337eb13559c171298159dff
def test_hello():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Hello world!!! from Shanmukh'
