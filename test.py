from knack_api_library import collect_records
from dataset import Dataset
from records import Records


print(collect_records(2)[0]['id'])

dataset = Dataset('57b21c8e67d437161a265671')
print(dataset.display(dataset.keywords_list))
print(dataset.contact_point)
print(Dataset.datasets)
records = Records(2)
print(records.total)
print(records.name)
print(dataset.title)
print(dataset.display(dataset.types_list))

