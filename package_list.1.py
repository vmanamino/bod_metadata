import ckan_api_library
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

data = ckan_api_library.public_packages()
pack_list = open('package_list.2.txt', 'w')
if data['code'] == 200:
    packages = data['content']
else:
    packages = "none"
    
if not packages == "none":
    pack_list.write("List of packages\n")
    for pack in packages:
        pack_list.write("%s\n" % (pack))

