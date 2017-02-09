import ckan_api_library
import report_library
import json

"""
This script is to patch all owner_org/publishers for all
public packages
"""

data = ckan_api_library.public_packages()
# packages = open('packages_test.txt')
if data['code'] == 200:
    packages = data['content']
else:
    packages = "none"
    
bostonMaps = "f8d82bea-34ab-4328-8adf-a5b1c331b50c"
bwsc = "f3e0e3f4-ab68-4223-aa31-284b62d1df5d"
assessing = "767c92cc-8a1f-468d-bf07-e46f2c3a7b0e"

owner_exceptions = [bostonMaps, bwsc, assessing]

new_owner = "department-of-innovation-and-technology-org"



updates = report_library.batch_report('publisher')
errors = report_library.error_report('publisher')
exceptions = report_library.exception_report('publisher')

test_count = 3
count = 0
if not packages == "none":
    items = 0
    updates.write('name\tcontact email\tprovider\n')
    exceptions.write('name\tprovider\tcontact email\n')
    for name in packages:
        data = ckan_api_library.package(name)
        if data['content'].has_key('contact_point_email'):
            if not data['content']['contact_point_email'] == "EGIS_Team@boston.gov":
                payload = {"id": name, "publisher": "Department of Innovation and Technology"}
                response = ckan_api_library.package_patch_request(payload)
                if response['code'] == 200:
                    updates.write('%s\t%s\t%s\n' % (name, data['content']['owner_org'], response['code']))
                    items += 1
                else:
                    errors.write('%s\t%s\n' % (name, response['code']))
                
            else:
                exceptions.write('%s\t%s\n' % (data['content']['name']
                    , data['content']['owner_org']))
        else:
            if data['content'].has_key('owner_org'):
                payload = {"id": name, "publisher": "Department of Innovation and Technology"}
                response = ckan_api_library.package_patch_request(payload)
                if response['code'] == 200:
                    updates.write('%s\t%s\t%s\n' % (name, data['content']['owner_org'], response['code']))
                    items += 1
                else:
                    errors.write('%s\t%s\n' % (name, response['code']))
            else:
                exceptions.write('%s\tnone\tnone\n' % (data['content']['name']))
                
        
    if len(packages) == items:
        print('job done')
    else:
        if len(packages) > items:
            difference = len(packages) - items
            print("This is the difference between the packages and those checked/patched:")
            print(difference)
        elif items > len(packages):
            print('something is screwy!')
else:
    print("no packages")

