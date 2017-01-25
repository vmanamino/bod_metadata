import json
from knack_api_library import collect_records, record_specs

class Records:
    
    def __init__(self, obj_num):
        records = collect_records(obj_num)
        self.total = len(records)
        response = record_specs(obj_num)
        specs = json.loads(response.read())['object']
        self.name = specs['name']