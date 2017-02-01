
"""
functions to write reports
"""

def batch_report(param):
    out = open(param+'_batch.txt', 'w')
    return out
    
def exception_report(param):
    out = open(param+'_exceptions.txt', 'w')
    return out
    
def no_key_report(param):
    out = open(param+'_no_key.txt', 'w')
    return out
    

