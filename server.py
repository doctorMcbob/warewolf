"""
This ones for you mom
"""
import waitress
from pyramid.config import Configurator
from pyramid.response import Response

from jinja2 import Environment, PackageLoader, select_autoescape

templates = Environment(
    loader=PackageLoader("server", "templates"),
    autoescape=select_autoescape(['html', 'xml'])
)

def main(request):
    return Response(templates.get_template("index.html").render())


if __name__ == """__main__""":
    with Configurator() as config:
        config.add_route("main", "/")
        config.add_view(main, route_name="main")

        config.add_static_view(name="/static", path="server:/static/")
        config.add_static_view(name="/static/css", path="server:/static/css/")
        config.add_static_view(name="static/js", path="server:/static/js/")

        config.scan()
        app = config.make_wsgi_app()

    waitress.serve(app, port=8000)
