import ckan_api_library
from dataset import Dataset
from objekt import Objekt
from package_whole import PackageWhole

dataset = Dataset("57e57429e97863da1f8e465d")

package = PackageWhole(dataset)

provider = package.patch_single_provider()

response_dict = package.knack_patch_single_send(provider)

print(response_dict['code'])
print(response_dict['content'])