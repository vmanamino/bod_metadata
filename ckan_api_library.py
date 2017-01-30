import json, os
import sys
import urllib2
import urllib
# this is where my keys are kept hidden from Github and this where my current modules are
sys.path.append('/home/ubuntu/workspace/code/ckan_boston')
reload(sys)
import keys

key = os.environ['CKAN_API_KEY']

def package_create_request(payload):
    
    data_string = urllib.quote(json.dumps(payload))
    
    url = 'http://boston.ogopendata.com/api/3/action/package_create'
    
    request = urllib2.Request(url)
    request.add_header('Authorization', key)
    
    # print(request)
    
    try:
        return urllib2.urlopen(request, data_string)
    except urllib2.HTTPError as err:
        return err
    
def prep_request(url, key):
    
    request = urllib2.Request(url)
    request.add_header('Authorization', key)
    
    return request
    