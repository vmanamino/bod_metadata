import ckan_api_library
from dataset import Dataset
from objekt import Objekt
from package_whole import PackageWhole

dataset = Dataset("577d6602238f7dac4d88b8ea")

package = PackageWhole(dataset)

payload = package.patch_single_desc()

# print(payload)

response = package.knack_patch_single_send(payload)

print(response['content'])

# print(package.patch_single_desc())

# print(ckan_api_library.package(package.name))