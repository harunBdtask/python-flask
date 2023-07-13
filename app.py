from flask import Flask
from resources.test import test
from resources.stat import stat
app = Flask(__name__)
app.register_blueprint(test, url_prefix='/')
app.register_blueprint(stat, url_prefix='/stat/')
# Example route for returning a plain text response
@app.route('/')
def get_hello():
    return 'Hello Flask!'
if __name__ == '__main__':
    app.run()
