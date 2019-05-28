from aiohttp.web import get
from .views import handle_view


def setup_routes(app):
    app.add_routes([
        get('/', handle_view),
        get('/{name}', handle_view)
    ])