from linkedin_python import User
from mock_api import MockAPI

"""Basically we just test that the code runs by calling our MockAPI class
"""

def test_user():
    api = MockAPI("fake_token")
    user = User(api)
    info = user.info()
    assert 'id' in info 
    post = user.create_post("foo")
    post = user.create_post("foo", images=[("baa/foo.png", "image description")])
