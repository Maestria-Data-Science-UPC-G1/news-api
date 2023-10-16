from flask import Blueprint, request
import services.news_service as service

main = Blueprint('news_blueprint', __name__)

@main.route('/')
def get_news():
    query = request.args.get('query')
    return service.generate_graph(query)