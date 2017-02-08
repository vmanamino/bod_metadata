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

new_owner = "innovation-and-technology"

updates = report_library.batch_report('owner_org')
errors = report_library.error_report('owner_org')
exceptions = report_library.exception_report('owner_org')
no_keys = report_library.no_key_report('owner_org')

test_count = 3
count = 0
if not packages == "none":
    items = 0
    for name in packages:
        exception = False
        data = ckan_api_library.package(name)
        if data['content'].has_key('owner_org'):
            for owner in owner_exceptions:
                if data['content']['owner_org'] == owner:
                    exception = True
                    exceptions.write('%s\t%s\n' % (name, data['content']['owner_org']))
                    items += 1
                    break
            if not exception:
                payload = {"id": name, "owner_org": new_owner}
                response = ckan_api_library.package_patch_request(payload)
                if response['code'] == 200:
                    updates.write('%s\t%s\t%s\n' % (name, data['content']['owner_org'], response['code']))
                    items += 1
                else:
                    errors.write('%s\t%s\n' % (name, response['code']))
        else:
            no_keys.write('%s\n' % (name))
            items += 1
          
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




