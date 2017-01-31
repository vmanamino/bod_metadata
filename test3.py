import ckan_api_library
from dataset import Dataset
from object import Object
from package_whole import PackageWhole
import report_library

# test a patch on source

# test patch batch on source
ids = open('ids.txt')
out = report_library.batch_report('provider')
for ident in ids:
    dataset = Dataset(ident)
    package = PackageWhole(dataset)
    # owner_payload = package.patch_single_owner()
    # print(owner_payload)
    # response = package.knack_package_patch_single_send(owner_payload)
    # out.write('%s\t%s\t%s\n' % (package.name, package.source, response.code))
    response = package.patch_batch_provider_send()
    out.write('%s\t%s\t%s\n' % (package.name, package.provider, response))

# test creating a dataset