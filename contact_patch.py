import ckan_api_library
from dataset import Dataset
from objekt import Objekt
from package_whole import PackageWhole

dataset = Dataset("57b21c8e67d437161a265671")

package = PackageWhole(dataset)

contact = package.patch_single_contact()

print(contact)

