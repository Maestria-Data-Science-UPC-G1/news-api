from flask import Flask
from flask_cors import CORS
from config import config
import pandas as pd
import os
# Routes
from routes import News

app = Flask(__name__)
CORS(app)

# Cargar el archivo CSV en un dataframe
#df = pd.read_csv('/home/igorov/maestria/redes_complejas/git/news-api/src/data/news.csv', sep='|')

# Obtener la ruta absoluta de la carpeta 'data'
data_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src/data'))

# Leer el archivo CSV en un dataframe
print(f"Reading CSV file from {data_folder}")
df = pd.read_csv(os.path.join(data_folder, 'news.csv'), sep='|')
print("CSV file readed successfully")

def page_not_found(error):
    return '<h1>This page does not exist</h1>', 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(News.main, url_prefix='/api/news', df=df)

    # Error handlers
    app.register_error_handler(404, page_not_found)
    #app.run()
    app.run(host='0.0.0.0', debug=True, port=8080)