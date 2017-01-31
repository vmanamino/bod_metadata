from object import Object

# test getting dataset records from knack, datasets are object 2

dataset = Object(2)
print(dataset.name)

for record in dataset.records:
    print(record['id'])
    
print(dataset.total)
