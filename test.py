import ckan_api_library
from dataset import Dataset
from objekt import Objekt
from package_whole import PackageWhole


dataset = Dataset('588f960178f426c7469921c4')
print(dataset.display(dataset.keywords_list))
print(dataset.contact_point)
print(Dataset.datasets)
records = Objekt(2)
print(records.total)
print(records.name)
print(dataset.title)
print(dataset.display(dataset.types_list))
print(dataset.display(dataset.classif_list))

package = PackageWhole(dataset)

print('provided by:')
print(package.provider)
print('dataset types')
print(package.btype)
print('source')
print(package.source)
print('published by')
print(package.publisher)
print('visibility')
print(package.isopen)
print('frequency')
print(package.accrual_periodicity)
print('time from')
print(package.temp_from)
print('temp notes:')
print(package.temp_notes)

members = [attr for attr in dir(package) 
            if not callable(attr) 
            and not attr.startswith("__") 
            and not attr == 'iterate_list'
            and not attr == "knack_package_create_payload"
            and not attr == "knack_package_create_send"
            and not attr == "patch_schema_presets"
            and not attr == "knack_package_patch_single_source"
            and not attr == "patch_temp_from"
            and not attr == "patch_single_contact"
            and not attr == "patch_single_desc"
            and not attr == "patch_single_provider"
            and not attr == "patch_single_owner"
            and not attr == "patch_single_source"
            and not attr == "patch_batch_provider_send"
            and not attr == "knack_patch_single_send"
            and not attr == "patch_batch_source_send"
            and not attr == "batch_check"]

print(members)
attrs = package.__dict__

for member in members:
    print(member)
    if attrs[member] == "none":
        print("this member has no value: "+member)
    else:
        value = attrs[member]
        print(value)
        
# source = package.knack_package_patch_single_source()
# print(source)
# print(package.knack_package_patch_single_send(source).code)
# print('payload to send')
# print(package.knack_package_create_payload())
# print(package.knack_package_create_send()['code'])
# print(package.knack_package_create_send()['content'])





