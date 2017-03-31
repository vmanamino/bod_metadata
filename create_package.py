import ckan_api_library
from dataset import Dataset
from objekt import Objekt
from package_whole import PackageWhole

dataset = Dataset('58cc3ecbbc0fe8309c117d10')

package = PackageWhole(dataset)

print(package.knack_package_create_send())

# if data['code'] == 200:
#     packages = data['content']
# else:
#     packages = "none"