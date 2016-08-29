from pyramid.view import view_config
import os

HERE = os.path.dirname(__file__)

ENTRIES = [
    {"title": "LJ - Day 10", "creation_date": "Aug 19, 2016", "id": 10, "body": "Sample body text."},
    {"title": "LJ - Day 11", "creation_date": "Aug 22, 2016", "id": 11, "body": "Sample body text."},
    {"title": "LJ - Day 12", "creation_date": "Aug 23, 2016", "id": 12, "body": "Sample body text."},
]

@view_config(route_name='home', renderer='templates/index.jinja2')
def list_view(request):
    return {'title': 'Home',
            "entries": ENTRIES
            }


@view_config(route_name='create', renderer='templates/new_entry.jinja2')
def create(request):
    return {'title': 'New Entry'}


@view_config(route_name='detail', renderer='templates/single_entry.jinja2')
def detail_view(request):
    return {"title": "LJ - Day 10", 
            "creation_date": "Aug 19, 2016", 
            "id": 10, 
            "body": "Sample body text."}


@view_config(route_name='edit', renderer='templates/edit_entry.jinja2')
def edit_view(request):
    return {'title': 'Edit Entry'}


# def includeme(config):
#     config.add_view(list_view, route_name='home')
#     config.add_view(create, route_name='create')
#     config.add_view(detail_view, route_name='detail')
#     config.add_view(edit_view, route_name='edit')
