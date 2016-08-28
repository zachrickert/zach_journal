from pyramid.view import view_config
from pyramid.response import Response


# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def my_view(request):
#     return {'project': 'MyProject'}

import os

HERE = os.path.dirname(__file__)

def list_view(request):
    imported_text = open(os.path.join(HERE, 'templates/index.html')).read()
    return Response(imported_text)

def create(request):
    imported_text = open(os.path.join(HERE, 'templates/new_entry.html')).read()
    return Response(imported_text)

def detail_view(request):
    imported_text = open(os.path.join(HERE, 'templates/single_entry.html')).read()
    return Response(imported_text)


def edit_view(request):
    imported_text = open(os.path.join(HERE, 'templates/edit_entry.html')).read()
    return Response(imported_text)


def includeme(config):
    config.add_view(list_view, route_name='home')
    config.add_view(create, route_name='create')
    config.add_view(detail_view, route_name='detail')
    config.add_view(edit_view, route_name='edit')
