#Name: apiCollectionFreshPull
#Author: Brian Gracin
#Course: IST 440W
#Professor: Senior Lecturer Joseph Oakes
#Created: 10/19/2015
#Modified: 11/2/2015
#List compiled by Owen Murphy

def getApiUrls():
    #List holding collection name and api url for parsing
    apiUrls = [
    {'name':'us_all_w', 'url':'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_NUS_DPG.W&out=xml'},
    {'name':'east_coast_all_w', 'url':'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R10_DPG.W&out=xml'},
    {'name':'new_england_all_w', 'url':'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R1X_DPG.W&out=xml'},
    {'name':'central_atlantic_all_w', 'url':'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R1Y_DPG.W&out=xml'},
    {'name':'lower_atlantic_all_w', 'url':'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R1Z_DPG.W&out=xml'},
    {'name':'midwest_all_w', 'url':'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R20_DPG.W&out=xml'},
    {'name':'gulf_coast_all_w', 'url':'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R30_DPG.W&out=xml'},
    {'name':'rock_mountains_all_w', 'url':'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R40_DPG.W&out=xml'},
    {'name':'west_coast_all_w', 'url':'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R50_DPG.W&out=xml'},
    {'name':'west_coast_no_cali_all_w', 'url':'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R5XCA_DPG.W&out=xml'},
    {'name':'us_all_a', 'url':'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_NUS_DPG.A&out=xml'},
    {'name':'us_all_m', 'url':'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_NUS_DP&out=xml'}]
    return apiUrls
