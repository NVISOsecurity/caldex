from datetime import datetime

from aiohttp import web

from .navigator import Layer, Technique
from .operations import Operation


class Caldex:

    def __init__(self, services):
        self.services = services
        self.auth_svc = services.get('auth_svc')
        self.data_svc = services.get('data_svc')

    async def export(self, request):
        await self.auth_svc.check_permissions(request)
        raw_operations = await self.data_svc.explode_operation()
        operations = []
        for raw_operation in raw_operations:
            operations.append(Operation(raw_operation))
        layer = Caldex.convert(operations)
        return web.json_response(layer.export())

    @staticmethod
    def convert(operations: list):
        now = datetime.now()
        layer = Layer("Caldera Overview", 'Caldera overview as exported on {:%B %d, %Y}.'.format(now))

        # Get the hosts and check if impacted
        abilities = {}
        techniques = {}
        succeeded = {}
        failed = {}

        # For each operation
        for operation in operations:
            # List all its abilities
            for i, phase in operation.adversary.phases.items():
                for ability in phase:
                    if ability.identifier not in abilities:
                        abilities[ability.identifier] = ability

        # Create the related technique
        for identifier, ability in abilities.items():
            key = ability.technique.tactic + ability.technique.identifier
            if key not in techniques:
                t_id = ability.technique.identifier
                t_tactic = ability.technique.tactic
                techniques[key] = Technique(t_id, t_tactic)
                succeeded[key] = set()
                failed[key] = set()

        # For each operation
        for operation in operations:
            # Check each action
            for action in operation.chain:
                ability = abilities[action.ability]
                key = ability.technique.tactic + ability.technique.identifier
                if action.status is 0:
                    succeeded[key].add(action.hostId)
                else:
                    failed[key].add(action.hostId)

        # Define the maximum expected score
        upper = 0
        for key, technique in techniques.items():
            vulnerable = len(succeeded[key])
            resistant = len([host for host in failed[key] if host not in succeeded[key]])
            total = vulnerable + resistant
            # if total > upper:     # Use to highlight global state
            #     upper = total
            if vulnerable > upper:  # Use to highlight improvement focus state
                upper = vulnerable
            technique.score = vulnerable

        # Report results
        layer.gradient.maxValue = upper
        layer.techniques = techniques.values()

        return layer
