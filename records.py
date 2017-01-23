from knack_api_library import collect_records, record_specs

class Records:
    
    def __init__(self, obj_num):
        records = collect_records(obj_num)
        self.total = len(records)
        specs = record_specs(obj_num)
        self.name = specs['name']