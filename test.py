import ckan_api_library
from knack_api_library import collect_records
from dataset import Dataset
from records import Records
from package_whole import PackageWhole


print(collect_records(2)[0]['id'])

dataset = Dataset('588f960178f426c7469921c4')
print(dataset.display(dataset.keywords_list))
print(dataset.contact_point)
print(Dataset.datasets)
records = Records(2)
print(records.total)
print(records.name)
print(dataset.title)
print(dataset.display(dataset.types_list))
print(dataset.display(dataset.classif_list))

package = PackageWhole(dataset)

print(package.provider)
print(package.btype)
print(package.source)
print('published by')
print(package.publisher)
print(package.isopen)
print(package.accrual_periodicity)
print('time from')
print(package.temp_from)
print(package.temp_notes)

members = [attr for attr in dir(package) 
            if not callable(attr) 
            and not attr.startswith("__") 
            and not attr == 'iterate_list'
            and not attr == "knack_package_create_payload"
            and not attr == "knack_package_create_send"]

print(members)
attrs = package.__dict__

for member in members:
    print(member)
    if attrs[member] == "none":
        print("this member has no value: "+member)
    else:
        value = attrs[member]
        print(value)
        
print(package.knack_package_create_payload())
print(package.knack_package_create_send().code)





