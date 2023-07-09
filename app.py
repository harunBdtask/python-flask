from flask import Flask
from resources.test import test
app = Flask(__name__)
app.register_blueprint(test, url_prefix='/')
# Example route for returning a plain text response
@app.route('/')
def get_hello():
    return 'Hello!'
if __name__ == '__main__':
    app.run()
