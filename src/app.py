from flask import Flask
from flask_cors import CORS
from config import config

# Routes
from routes import News

app = Flask(__name__)
CORS(app)

def page_not_found(error):
    return '<h1>This page does not exist</h1>', 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(News.main, url_prefix='/api/news')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    #app.run()
    app.run(host='0.0.0.0', debug=True, port=8080)