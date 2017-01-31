
"""
functions to write reports
"""

def batch_report(param, data, code):
    out = open(param+'.txt', 'w')
    out.write('%s\t%s' % (data, code))
    

