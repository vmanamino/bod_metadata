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
    # print('function called')
    # print(label)
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
    # print('value selected:')
    # print(value)
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
        
def open_values(label):
    value = "open"
    if label == "no" or label == "none":
        value = "closed"
    return value
    
def frequencies(label):
    value = ""
    if not label == "none":
        if label == "Continuously updated":
            value = "R/PT1S"
        if label == "Daily":
            value = "R/P1D"
        if label == "Three times a week":
            value = "R/P0.33W"
        if label == "Semiweekly":
            value = "R/P3.5D"
        if label == "Weekly":
            value = "R/P1W"
        if label == "Three times a month":
            value = "R/P0.33M"
        if label == "Biweekly":
            value = "R/P2W"
        if label == "Semimonthly":
            value = "R/P0.5M"
        if label == "Monthly":
            value = "R/P1M"
        if label == "Bimonthly":
            value = "R/P2M"
        if label == "Quarterly":
            value = "R/P3M"
        if label == "Three times a year":
            value = "R/P4M"
        if label == "Semiannual":
            value = "R/P6M"
        if label == "Annual":
            value = "R/P1Y"
        if label == "Biennial":
            value = "R/P2Y"
        if label == "Triennial":
            value = "R/P3Y"
    else:
        value = "none"
    return value
    
# aka owner_org
# complete this
def owner_orgs(label):
    value = ""
    if label == "Department of Innovation and Technology":
        value = "innovation-and-technology"
    elif label == "Boston Water and Sewer Commission":
        value = "water-and-sewer-commission"
    elif label == "Boston EMS":
        value = "emergency-medical-services-org"
    elif label == "Archives and Records Management":
        value = "archives-and-record-management-org"
    elif label == "Assessing Department":
        value = "assessing-department-org"
    elif label == "Boston 311":
        value = "boston-311-org"
    elif label == "Boston Centers for Youth and Families":
        value = "boston-centers-for-youth-families-org"
    
    # "boston-maps",
    
    elif label == "Boston Planning & Development Agency":
        value = "boston-planning-development-agency-org"
    elif label == "Boston Police Department":
        value = "boston-police-department-org"
    elif label == "Boston Public Library":
        value = "boston-public-library-org"
    elif label == "Boston Transportation Department":
        value = "boston-transportation-department-org"
    elif label == "Boston Water and Sewer Commission":
        value = "boston-water-and-sewer-commission-org"
    elif label == "City of Boston Archaeology Program":
        value = "city-of-boston-archaeology-program-org"
    elif label == "Consumer Affairs & Licensing Department":
        value = "consumer-affairs-and-licensing-department-org"
    elif label == "DoIT Data & Analytics":
        value = "doit-data-analytics-org"
    elif label == "Department of Neighborhood Development":
        value = "department-of-neighborhood-development-org"
    elif label == "Environment Department":
        value = "environment-department-org"
    elif label == "Fair Housing & Equity":
        value = "fair-housing-and-equity-org"
    elif label == "GIS Team":
        value = "gis-team-org"
    elif label == "Inspectional Services Department":
        value = "inspectional-services-department-org"
    elif label == "Intergovernmental Relations":
        value = "intergovernmental-relations-org"
    elif label == "Mayor's Office for Immigrant Advancement":
        value = "mayor-s-office-for-immigrant-advancement-org"
    elif label == "Mayor's Office of Emergency Management Services":
        value = "mayor-s-office-of-emergency-management-services-org"
    elif label == "Neighborhood Services":
        value = "neighborhood-services-org"
    elif label == "Office of Arts & Culture":
        value = "office-of-arts-culture-org"
    elif label == "Office of Budget Management":
        value = "office-of-budget-management-org"
    elif label == "Office of Economic Development":
        value = "office-of-economic-development-org"
    elif label == "Office of Human Resources":
        value = "office-of-human-resources-org"
    elif label == "Office of the Parking Clerk":
        value = "office-of-the-parking-clerk-org"
    elif label == "Property Management":
        value = "property-management-org"
    elif label == "Public Works Department":
        value = "public-works-department-org"
    elif label == "Purchasing Division":
        value = "purchasing-division-org"
    elif label == "Veterans Services":
        value = "veterans-services-org"
    else:
        value = "department-of-innovation-and-technology-org"
    return value