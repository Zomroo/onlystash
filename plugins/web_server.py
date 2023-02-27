from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = f"Hello, {name}!"
    return web.Response(text=text)

async def web_server():
    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)])
    return app
