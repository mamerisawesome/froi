from flask import Flask
from froi import Froi, __version__


def test_version():
    assert __version__ == '0.4.4'

def test_simple_app():
    class SomeRoute(Froi):
        def __init__(self, app):
            super().__init__(app, 'SomeRoute', '/api')

        def get(self):
            return 'Test on GET'

        def post(self):
            return 'Test on POST'

    app = Flask('app')
    some_route = SomeRoute(app)
    assert some_route.getmethods() == ['GET', 'POST']

def test_install():
    try:
        class SomeComponent(Froi):
            def __init__(self, app):
                super().__init__(app, 'SomeComponent', '/api')

            def install(self):
                self.setget().route(func=lambda x: x)
                self.setpost().route('/post', func=lambda x: x)

    except Exception as e:
        assert False
        return e
    finally:
        assert True
