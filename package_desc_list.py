import ckan_api_library
import report_library
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
    

package_list = report_library.batch_report('package_desc')

dept_innov_tech = '80644104-7cff-4322-b2a3-33466d5e98bb'

test_count = 3
count = 0
line_arr = []
if not packages == "none":
    package_list.write('NAME\tDESC\n')
    for name in packages:
        package = ckan_api_library.package(name)
        if package['content'].has_key('owner_org'):
            if package['content']['owner_org'] == dept_innov_tech:
                fd = ''
                line_arr = package['content']['notes'].split('\n')
                line_count = 0
                for l in line_arr:
                    if line_count > 0:
                        fd += '  '
                    fd += l.strip()
                    count += 1
                
                package_list.write('%s\t%s\n' % (package['content']['name'], fd))
        
else:
    print("no packages")

