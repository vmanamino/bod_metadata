from contact import Contact
from knack import Knack
from knack_api_library import create_contact
import time

class Dataset(Knack):
    datasets = 0
    def __init__(self, ident):
        self.ident = ident
        self.json = self.get_in_json(ident)
        self.title = self.json['field_5_raw'].strip()
        self.types_list = self.list_values(self.json, 'field_152_raw')
        self.desc = self.json['field_6_raw']
        self.prov_list = self.list_values(self.json, 'field_186_raw')
        self.sources_list = self.list_values(self.json, 'field_164_raw')
        self.pub_list = self.list_values(self.json, 'field_205_raw')
        self.classif_list = self.list_values(self.json, 'field_155_raw')
        self.open_status = self.value_none(self.json['field_308_raw'])
        self.freq = self.list_values(self.json, 'field_139_raw')
        self.time_from = self.get_date_str(self.json['field_121_raw'])
        self.time_to = self.get_date_str(self.json['field_122_raw'])
        self.time_notes = self.value_none(self.json['field_159_raw'])
        self.topics_list = self.list_values(self.json, 'field_146_raw')
        self.location_list = self.list_values(self.json, 'field_136_raw')
        self.keywords_list = self.list_values(self.json, 'field_321_raw')
        
        # all datasets in Knack have a contact 
        contact_obj = self.contact(self.json['field_147_raw'])
        self.contact_point = contact_obj.fn
        self.contact_email = contact_obj.email
        self.contact_phone = contact_obj.phone
        Dataset.datasets += 1
        
    # instance values for contact
    @staticmethod
    def contact(obj):
        contact_info = create_contact(obj)
        return Contact(contact_info[0], contact_info[1], contact_info[2])
    
    @staticmethod
    def get_date_str(time_obj):
        if time_obj:
            stamp = time_obj['unix_timestamp']
            return time.strftime('%Y-%m-%d', time.gmtime(stamp/1000.)) 
        else:
            return 'none'

