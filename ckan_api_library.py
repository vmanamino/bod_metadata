import json, os
import sys
import urllib2
import urllib
# this is where my keys are kept hidden from Github and this where my current modules are
sys.path.append('/home/ubuntu/workspace/code/ckan_boston')
reload(sys)
import keys

key = os.environ['CKAN_API_KEY']

# these packages i think are set to public, i.e. private = false
def get_public_packages():
    
    url = "http://boston.ogopendata.com/api/3/action/package_list"
    
    request = prep_request(url)
    
    try:
        return urllib2.urlopen(request)
    except urllib2.HTTPError as err:
        return err

def public_packages():
    
    response = get_public_packages()
    return response_dict(response)
   
def package_get_request(name):
    
    payload = {"id": name}
    
    url = 'http://boston.ogopendata.com/api/3/action/package_show'
    
    request = prep_request(url)
    
    return make_request(request, payload)

def package(name):
    response = package_get_request(name)
    return response_dict(response)

def package_create_request(payload):
    
    url = 'http://boston.ogopendata.com/api/3/action/package_create'
    
    request = prep_request(url)
    
    response = make_request(request, payload)
    
    return response_dict(response)

def package_patch_request(payload):
    
    url = 'http://boston.ogopendata.com/api/3/action/package_patch'
    
    request = prep_request(url)
    
    return make_request(request, payload)

def make_request(request, payload):
    
    data_string = urllib.quote(json.dumps(payload))
    
    try:
        return urllib2.urlopen(request, data_string)
    except urllib2.HTTPError as err:
        return err
    
def prep_request(url):
    
    request = urllib2.Request(url)
    request.add_header('Authorization', key)
    
    return request
    
# need to implement this consistently
def response_dict(response):
    code = response.code
    response_dict = {}
    data = json.loads(response.read())
    if response.code == 200:
        response_dict['code'] = code
        response_dict['content'] = data['result']
    else:
        response_dict['code'] = code
        response_dict['content'] = data['error']
    return response_dict
    