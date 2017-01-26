from slugify import slugify

class Package:
    
    # pass in knack dataset object already transformed
    def __init__(self, dataset):
        
        # instance vars called the params for ckan requests
        # skipped released and modified, no use cases yet
        
        # name doubles as id needed in requests for specific packages
        self.name = slugify(dataset.title)
        self.name_translated_en = dataset.title
        self.btype = dataset.types_list
        self.notes = dataset.desc
        self.notes_translated = dataset.desc
        
        