# File name: apiCollectionFreshPull
# Author: Brian Gracin
# Course: IST 440W
# Professor: Senior Lecturer Joseph Oakes
# Created: 10/19/2015
# Modified: 11/18/2015
# List compiled by Owen Murphy

def getApiUrls():
    # List holding collection name and api url for parsing
    apiUrls = [
        {'name': 'us_w',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_NUS_DPG.W&out=xml'},
        {'name': 'eastCoast_w',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R10_DPG.W&out=xml'},
        {'name': 'newEngland_w',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R1X_DPG.W&out=xml'},
        {'name': 'centralAtlantic_w',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R1Y_DPG.W&out=xml'},
        {'name': 'lowerAtlantic_w',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R1Z_DPG.W&out=xml'},
        {'name': 'midwest_w',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R20_DPG.W&out=xml'},
        {'name': 'gulfCoast_w',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R30_DPG.W&out=xml'},
        {'name': 'rockMountains_w',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R40_DPG.W&out=xml'},
        {'name': 'westCoast_w',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R50_DPG.W&out=xml'},
        {'name': 'us_a',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_NUS_DPG.A&out=xml'},
        {'name': 'eastCoast_a',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R10_DPG.A&out=xml'},
        {'name': 'newEngland_a',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R1X_DPG.A&out=xml'},
        {'name': 'centralAtlantic_a',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R1Y_DPG.A&out=xml'},
        {'name': 'lowerAtlantic_a',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R1Z_DPG.A&out=xml'},
        {'name': 'midwest_a',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R20_DPG.A&out=xml'},
        {'name': 'gulfCoast_a',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R30_DPG.A&out=xml'},
        {'name': 'rockMountains_a',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R40_DPG.A&out=xml'},
        {'name': 'westCoast_a',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R50_DPG.A&out=xml'},
        {'name': 'us_m',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_NUS_DPG.M&out=xml'},
        {'name': 'eastCoast_m',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R10_DPG.M&out=xml'},
        {'name': 'newEngland_m',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R1X_DPG.M&out=xml'},
        {'name': 'centralAtlantic_m',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R1Y_DPG.M&out=xml'},
        {'name': 'lowerAtlantic_m',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R1Z_DPG.M&out=xml'},
        {'name': 'midwest_m',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R20_DPG.M&out=xml'},
        {'name': 'gulfCoast_m',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R30_DPG.M&out=xml'},
        {'name': 'rockMountains_m',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R40_DPG.M&out=xml'},
        {'name': 'westCoast_m',
         'url': 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_R50_DPG.M&out=xml'}]
    return apiUrls
