import ckan_api_library
import report_library
import json
import sys
import urllib2
import urllib
reload(sys)
sys.setdefaultencoding('utf-8')



def get_sheet():
    request = "https://sheetsu.com/apis/v1.0/ab719a3ecb64"
    try:
        return urllib2.urlopen(request)
    except urllib2.HTTPError as err:
        return err

response = get_sheet()

if response.code == 200:
    data = json.loads(response.read())
    for title in data:
        print(title['NAME'])


