"""
See patch_data_contact.py file for testing of this modules
"""

import json, os
import sys
import urllib2
import urllib
# this is where my keys are kept hidden from Github and this where my current modules are
sys.path.append('/home/ubuntu/workspace/code/ckan_boston')
reload(sys)
import keys

# Knack response header:
# Content-Type application/json; charset=utf-8
# I guess from this that character encoding is UTF-8
sys.setdefaultencoding('utf-8')

# CKAN API key
key = os.environ['CKAN_API_KEY'];

# Knack application id and API key
knack_app_id = os.environ['KNACK_APPLICATION_ID']
    
knack_api_key= os.environ['KNACK_API_KEY']

# call to get Knack records.  Knack responses always by page, so only records on a page will be returned in the response.
# Function directly below collects records for each page 
def get_knack_records(obj_num, page="1"):
    
    knack_object = string_knack_obj(obj_num)
    url = 'https://api.knack.com/v1/objects/'+knack_object+'/records?page='+page
    response = req_get(url)
    data = json.loads(response.read())
    return data
    
# special function to page through results in Knack call
def collect_records(obj_num):
    data = get_knack_records(obj_num)
    pages = data['total_pages']
    
    # more than one page
    if pages > 1:
    
        # first page of records
        records = data['records']
        range_end_boundary = pages + 1
    
        # start on second page always
        for i in range(2, range_end_boundary):
            data = get_knack_records(obj_num, str(i))
            records += data['records']
    
    # only one page        
    else:
        records = data['records']
    
    return records
    
    
def record_specs(obj_num):
    
    knack_object = string_knack_obj(obj_num)
    
    url = 'https://api.knack.com/v1/objects/'+knack_object
    
    return req_get(url)
    
def get_knack_dataset(ident):
   
    # will have to prep request to add ID and KEY as headers
    # had problems adding id as payload, should be tacked on at end
    url = 'https://api.knack.com/v1/objects/object_2/records/'+ident
    return req_get(url)

# provide contact object 'field_147_raw' from Knack object_2 record, see get_knack_dataset
# need to make request for Contact object because it contains the Gov Entity id
# which in turn is necessary to retreive phone and email info
def get_contact_object(contact_identifier):
    
    # will have to prep request to add ID and KEY as headers
    url = 'https://api.knack.com/v1/objects/object_36/records/'+contact_identifier
    return req_get(url)
    
    
def create_contact(obj):
    attributes = obj
    
    # contact is only one per dataset in our scheme
    contact_identifier = attributes[0]['id']
    response = get_contact_object(contact_identifier)
    contact = json.loads(response.read())
    
    # currently get_gov_entity_info method call returns email and phone, in that order
    contact_info = gov_entity_info(contact['field_216_raw'][0]['id'])
    
    # insert the contact_point first before email and phone
    contact_info.insert(0, attributes[0]['identifier'])
    return contact_info
    
def get_gov_entity_info(identifier):
    
    # info = []
    
    url = 'https://api.knack.com/v1/objects/object_3/records/'+identifier
    return req_get(url)
    
# prepare gov entity info in list
def gov_entity_info(ident):
    
    info = []
    response = get_gov_entity_info(ident)
    
    response = json.loads(response.read())
        
    if response['field_12_raw']['email']:
        email = response['field_12_raw']['email']
        info.append(email)
    else:
        info.append('none')
    if response['field_13_raw']['formatted']:
        phone = response['field_13_raw']['formatted']
        info.append(phone)
    else:
        info.append('none')
    
    return info
    
    
# string together knack object
def string_knack_obj(obj_num):
    return 'object_'+ str(obj_num)
    
    
# for authorization, authentication
def add_knack_headers(request):
    
    request.add_header('X-Knack-Application-Id', knack_app_id)
    
    request.add_header('X-Knack-REST-API-Key', knack_api_key)
    
    return request
    
def req_get(url):
    
    request = add_knack_headers(urllib2.Request(url)) 
    try:
        return urllib2.urlopen(request)
    except urllib2.HTTPError as err:
        print(err)