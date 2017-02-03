import ckan_api_library
from dataset import Dataset
from objekt import Objekt
from package_whole import PackageWhole

dataset = Dataset("57b21c8e67d437161a265671")

package = PackageWhole(dataset)

payload = package.patch_single_desc()

response = package.knack_package_patch_single_send(payload)

print(response['code'])

# print(package.patch_single_desc())

# print(ckan_api_library.package(package.name))