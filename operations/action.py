class Action:
    def __init__(self, raw_result: dict):
        if "ability" in raw_result:
            self.ability = raw_result["ability"]
        if "status" in raw_result:
            self.status = raw_result["status"]
        if "host_id" in raw_result:
            self.hostId = raw_result["host_id"]
