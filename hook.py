from plugins.caldex.app.caldex_api import CaldexApi

name = 'Caldex'
description = 'Export the Caldera reports to a MITRE ATT&CK Navigator Layer.'
address = 'caldex'


async def initialize(app, services):
    caldex_api = CaldexApi(services)
    app.router.add_route('GET', '/caldex', caldex_api.export)
    app.router.add_route('GET', r'/caldex/{operation:\d+}', caldex_api.export)
