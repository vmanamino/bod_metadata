# this class to create or update new packages on Boston Open Data Hub
# from datasets inventoried on Knack
# update will exclude certain parameters
# the motivation is to make Knack database authoritative source of metadata/documentation
# look at dir(obj) to identify none eligible params with none values
# http://stackoverflow.com/questions/1398022/looping-over-all-member-variables-of-a-class-in-python

from slugify import slugify
import ckan_presets
import ckan_api_library
import json, os
from package import Package
import urllib2
import urllib

class PackageWhole():
    
    # pass in knack dataset object already transformed
    def __init__(self, dataset):
        # Package.__init__(self)
        
        # instance vars called the params for ckan requests
        # skipped released and modified, no use cases yet
        
        # name doubles as id needed in requests for specific packages
        self.name = slugify(dataset.title)
        self.name_translated_en = dataset.title
        
        # need fixed value
        # none eligible
        self.btype = self.iterate_list(dataset.types_list, ckan_presets.btypes)
        self.notes = dataset.desc
        self.notes_translated = dataset.desc
        
        # provider values come from gov entity choices
        # provider is single, so use display method to access and present value
        # none eligible
        self.provider = ckan_presets.gov_entities(dataset.display(dataset.prov_list))
        
        # source can be multiple values, in a list
        # none eligible
        self.source = self.iterate_list(dataset.sources_list, ckan_presets.sources)
        
        # publisher values come gov entity choices
        # provider is single, so use display method to access and present value
        # none eligible
        self.publisher = ckan_presets.owner_orgs(dataset.display(dataset.pub_list))
        
        # none eligible
        self.classif = ckan_presets.classifications(dataset.display(dataset.classif_list))
        self.isopen = ckan_presets.open_values(dataset.open_status)
        
        # update frequency is single, so ...
        # none eligible
        self.accrual_periodicity = ckan_presets.frequencies(dataset.display(dataset.freq))
        
        # none eligible
        self.temp_from = dataset.time_from
        
        # none eligible
        self.temp_to = dataset.time_to
        
        # none eligible
        self.temp_notes = dataset.time_notes
        
        # none eligible
        self.topics = dataset.topics_list
        
        # none eligible 
        self.location = dataset.location_list
        
        # mandatory and present in Knack for all datasets
        self.contact_point = dataset.contact_point
        
        # mandatory and present in Knack for all datasets
        self.contact_point_email = dataset.contact_email
        
        # none eligible
        self.contact_point_phone = dataset.contact_phone
        
        # none eligible
        self.tags = dataset.keywords_list
        
    # all knack packages will have the following:
    # name
    # description
    # type
    # provider
    # publisher
    # classification
    # open
    # contact point
    def knack_package_create_payload(self):
        # members = [attr for attr in dir(self) 
        #     if not callable(attr) 
        #     and not attr.startswith("__") 
        #     and not attr == 'iterate_list'
        #     and not attr == "knack_package_create"]
        
        # create payload
        if self.contact_point_email == "none":
            payload = {"name": self.name, "title_translated-en": self.name_translated_en, "notes": self.notes 
                        , "notes_translated": {"en": self.notes_translated}, "provider": self.provider
                        , "owner_org": self.publisher, "btype": self.btype, "classification": self.classif, "isopen": self.isopen
                        , "contact_point": self.contact_point, "contact_point_email": "opengov@cityofboston.gov"
                        , "private": True, "license_id": "odc-pddl"
                        
                        
            }
        else:
            if self.contact_point_phone == "none":
                payload = {"name": self.name, "title_translated-en": self.name_translated_en, "notes": self.notes 
                            , "notes_translated": {"en": self.notes_translated}, "provider": self.provider
                            , "owner_org": self.publisher, "btype": self.btype, "classification": self.classif, "isopen": self.isopen
                            , "contact_point": self.contact_point, "contact_point_email": self.contact_point_email
                            , "private": True, "license_id": "odc-pddl"
                            
                            
                }
            else:
                payload = {"name": self.name, "title_translated-en": self.name_translated_en, "notes": self.notes
                            , "notes_translated": {"en": self.notes_translated}, "provider": self.provider
                            , "owner_org": self.publisher, "btype": self.btype, "classification": self.classif, "isopen": self.isopen
                            , "contact_point": self.contact_point, "contact_point_email": self.contact_point_email
                            , "contact_point_phone": self.contact_point_phone
                            , "private": True, "license_id": "odc-pddl"
                            
                }
                
        return payload
        
    def knack_package_create_send(self):
        payload = self.knack_package_create_payload()
        response = ckan_api_library.package_create_request(payload)
        return response
    
    """
    patch by parameter/field
    """
    
    # patch source
    def knack_package_patch_single_source(self):
        payload = {"id": self.name, "source": self.source}
        return payload
    
    def knack_package_patch_temp_from(self):
        pass
    
    # patch in batch
    # if field is none eligible, and if value is indeed none
    # then skip patch request, otherwise proceed
    
    # patch_batch_source(self)
    # self.source
    # batch_check(source)
    
    # batch_check(field)
    # if not none
    # knack_package_patch_single_send
    # write report of response codes
    
    # patch single
    # in this case, certain that field has value in knack and the field
    # needs to be updated on ckan
    @staticmethod
    def knack_package_patch_single_send(payload):
        return ckan_api_library.package_patch_request(payload)
        
    # iterate through list and assign values for each label
    # values correspond to presets in boston ckan schema
    @staticmethod
    def iterate_list(labels, fun):
        values = []
        if not labels == "none":
            for label in labels:
                value = fun(label)
                values.append(value)
            return values
        else:
            return labels
            