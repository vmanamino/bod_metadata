import ckan_api_library
import report_library
import json

data = ckan_api_library.public_packages()

if data['code'] == 200:
    packages = data['content']
else:
    packages = "none"
    
bostonMaps = "f8d82bea-34ab-4328-8adf-a5b1c331b50c"
bwsc = "f3e0e3f4-ab68-4223-aa31-284b62d1df5d"
assessing = "767c92cc-8a1f-468d-bf07-e46f2c3a7b0e"

owner_exceptions = [bostonMaps, bwsc, assessing]

new_owner = "innovation-and-technology"

updates = report_library.batch_report('package')
exceptions = report_library.exception_report('owner_org')
no_keys = report_library.no_key_report('owner_org')


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
                
                updates.write('%s\t%s\n' % (name, data['content']['owner_org']))
                items += 1
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




