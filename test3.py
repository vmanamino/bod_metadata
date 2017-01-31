import ckan_api_library
from dataset import Dataset
from object import Object
from package_whole import PackageWhole

# test a patch on source

# test patch batch on source
ids = open('ids.txt')
for ident in ids:
    dataset = Dataset(ident)
    package = PackageWhole(dataset)
    package.patch_batch_source_send()


# test creating a dataset