from pyramid.view import view_config
from pyramid.response import Response


# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def my_view(request):
#     return {'project': 'MyProject'}

import os

HERE = os.path.dirname(__file__)

# def home_page(request):
#     imported_text = open(os.path.join(HERE, 'templates/index.html')).read()
#     return Response(imported_text)

def list_view(request):
    imported_text = open(os.path.join(HERE, 'templates/index.html')).read()
    return Response(imported_text)

def includeme(config):
    config.add_view(list_view, route_name='home')
