import json
from knack_api_library import get_knack_dataset, get_contact_object

class Knack:
    
    # get all objects in json for easy assignment
    # using static methods because not using or assigning anything to properties
    # of the class
    @staticmethod
    def get_in_json(ident):
        res = get_knack_dataset(ident)
        return json.loads(res.read())
        
    # function to create multiple values in case relation of object to 
    # dataset is 'many'.
    @staticmethod
    def list_values(list_obj):
        count = len(list_obj)
        value_list = []
        
        # assumes that with first element empty, no values at all
        if count and list_obj[0]['identifier']:
            if count > 1:
                for obj in list_obj:
                    value_list.append(str(obj['identifier']))
            else:
                value_list.append(str(list_obj[0]['identifier']))
            return_obj = value_list
        else:
            return_obj = "none"
        return return_obj
        
    # add function to separate list values with pipe
    @staticmethod
    def display(list_obj):
        if not list_obj == "none":
            return '|'.join(list_obj)
        else:
            return list_obj
        
    @staticmethod
    def value_none(val):
        value = ''
        if not val:
            value = 'none'
        else:
            value = val
        return value
        