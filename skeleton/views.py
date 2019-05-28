from aiohttp.web import Response

async def handle_view(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name + request.app['config'].get('site_name')
    return Response(text=text)