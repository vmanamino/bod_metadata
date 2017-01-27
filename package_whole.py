# this class to create or update new packages on Boston Open Data Hub
# from datasets inventoried on Knack
# update will exclude certain parameters
# the motivation is to make Knack database authoritative source of metadata/documentation
# look at dir(obj) to identify none eligible params with none values
# http://stackoverflow.com/questions/1398022/looping-over-all-member-variables-of-a-class-in-python

from slugify import slugify
import ckan_presets
from package import Package

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
        self.publisher = ckan_presets.gov_entities(dataset.display(dataset.pub_list))
        
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
            