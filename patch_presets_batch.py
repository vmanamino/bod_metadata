import ckan_api_library
from dataset import Dataset
from objekt import Objekt
from package_whole import PackageWhole
from objekt import Objekt

objekt = Objekt(2)

count = 0
counter = 5

for i in range(5):
    dataset = Dataset(objekt.records[i]['id'])
    package = PackageWhole(dataset)
    print(package.patch_schema_presets())
        