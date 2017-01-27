# this class to create new packages on Boston Open Data Hub
# from datasets inventoried on Knack

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
        self.btype = self.iterate_list(dataset.types_list, ckan_presets.btypes)
        self.notes = dataset.desc
        self.notes_translated = dataset.desc
        
        # provider values come from gov entity choices
        # provider is single, so use display method to access and present value
        self.provider = ckan_presets.gov_entities(dataset.display(dataset.prov_list))
        
        # source can be multiple values, in a list
        self.source = self.iterate_list(dataset.sources_list, ckan_presets.sources)
        
        # publisher values come gov entity choices
        # provider is single, so use display method to access and present value
        self.publisher = ckan_presets.gov_entities(dataset.display(dataset.pub_list))
        self.classif = ckan_presets.classifications(dataset.display(dataset.classif_list))
        
        
    @staticmethod
    def iterate_list(labels, fun):
        values = []
        for label in labels:
            value = fun(label)
            values.append(value)
        return values
            