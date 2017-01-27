# -*- coding: utf-8 -*-
# library of functions to get preset values, usually out of a Knack object/dataset list

import sys
print sys.getdefaultencoding()



def btypes(label):
    value = ""
    if label == "Audio":
        value = "audio"
    elif label == "Image":
        value = "image"
    elif label == "Charts":
        value = "charts"
    elif label == "Map":
        value = "map"
    elif label == "Calendar":
        value = "calendar"
    elif label == "Forms":
        value = "forms"
    elif label == "External":
        value = "external"
    elif label == "Files and documents":
        value = "files_and_documents"
    elif label == "Tabular":
        value = "tabular"
    else:
        value = "none"
    return value

def gov_entities(label):
    value = "none"
    if not label == "none":
        
        # these labels are different from their values
        if label == "Administration & Finance":
            value = "Administration and Finance"
        elif label == "Arts & Culture":
            value = "Arts and Culture"
        elif label == "Boston Planning & Development Agency":
            value = "Boston Planning and Development Agency"
        elif label == "Consumer Affairs & Licensing Department":
            value = "Consumer Affairs and Licensing Department"
        elif label == "Director of Tax Policy & Communications":
            value = "Director of Tax Policy and Communications"
        elif label == "DoIT Data & Analytics":
            value = "DoIT Data and Analytics"
        elif label == "Fair Housing & Equity":
            value = "Fair Housing and Equity"
        elif label == "Housing & Neighborhood Development":
            value = "Housing and Neighborhood Development"
        elif label == "Office of Arts & Culture":
            value = "Office of Arts and Culture"
            
        # all cases where label is same as value
        else:
            value = label
            
    return value
    
def sources(label):
    value = "none"
    if not label == "none":
        
        # these labels are different from their values
        if label == "BPDA (Boston Planning & Development Agency) contract compliance database":
            value = "BPDA contract compliance database"
      
        elif label == "City Constituent Relationship Management (CRM) System":
            value = "City Constituent Relationship Management System"
      
        elif label == "City of Boston Voice over IP (VOIP) System":
            value = "City of Boston Voice over IP System"
      
        elif label == "Computer aided dispatch system (CAD)":
            value = "Computer aided dispatch system"
      
        elif label == "ENERGY STAR Portfolio Manager®":
            value = "ENERGY STAR Portfolio Manager"
      
        elif label == "IPS Data Management System (DMS)":
            value = "IPS Data Management System"
      
        elif label == "Labor Market Information, The Official Website of the Executive Office of Labor and Workforce Development (EOLWD)":
            value = "Labor Market Information, Executive Office of Labor and Workforce Development"
            
        elif label == "Massachusetts Artifact Tracking System (MATS)":
            value = "Massachusetts Artifact Tracking System"
        
        # all cases where label is same as value
        else:
            value = label
    
    return value
    
def classifications(label):
    value = ""
    if not label == "none":
        if label == "Exempt Record":
            value = "exempt"
        elif label == "Public Record":
            value = "public"
    else:
        value = "exempt"
    return value
        
    
    