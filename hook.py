from .caldex import Caldex

name = 'Caldex'
description = 'A sample plugin for demonstration purposes'
address = 'export'


async def initialize(app, services):
    caldex = Caldex(services)
    app.router.add_route('*', '/export', caldex.export)
