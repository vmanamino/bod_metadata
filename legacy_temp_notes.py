import ckan_api_library
import report_library
import json, os
import sys
import urllib2
import urllib
reload(sys)
sys.setdefaultencoding('utf-8')



def get_sheet():
    request = os.environ['GOOGLE_SHEET_API']
    try:
        return urllib2.urlopen(request)
    except urllib2.HTTPError as err:
        return err

response = get_sheet()
count = 0
if response.code == 200:
    report = report_library.batch_report("legacy_temp_notes")
    error = report_library.error_report("legacy_temp_notes")
    data = json.loads(response.read())
    for title in data:
        if title['Temporal Status'] == "Ready for upload":
            # print(title['NAME'])
            # print(title['TEMPORAL NOTES'])
            eyedee = title['NAME']
            temp_notes = title['TEMPORAL NOTES']
            # new_desc = title['NEW DESC']
            payload = {"id": eyedee, "temporal_notes": {"en": temp_notes}}
            print(payload)
            response = ckan_api_library.package_patch_request(payload)
            if response['code'] == 200:
                print(response['code'])
                print(title['NAME'])
                count += 1
                report.write("%s\n" % (title['NAME']))
            else:
                print(response['code'])
                print(title['NAME'])
                error.write("%s\n" % (title['NAME']))
    report.write("%s datasets updated with temporal notes\n" % count)
