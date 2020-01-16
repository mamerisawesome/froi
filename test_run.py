from flask import Flask
from froi import Froi

def run1():
    return 'run1'

def run2():
    return 'run2'

class SomeComponent(Froi):
    def __init__(self, app):
        super().__init__(app, 'SomeComponent', '/api')

    def install(self):
        self.setget().route(func=run1)
        self.setpost().route('/post', func=run2)

app = Flask('app')
some_component = SomeComponent(app)
some_component.install()
app.run()
