import json
from knack_api_library import collect_records, object_metadata

"""
Knack Objects should be referenced using a numeric ID,  this is to ensure 
unique and easy reference regardless of title changes
"""

class Object:
    
    def __init__(self, obj_num):
        self.records = collect_records(obj_num)
        self.total = len(self.records)
        self.name = object_metadata(obj_num)['name']