# Filename: Constants.py
# Author: Osei Seraphin
# Course: IST 440w
# Instructor: Professor Oakes

from enum import Enum


class constantsclass(Enum):

    INCORRECT_PASSWORD = "WRONG PASSWORD"

    WEEKLY_COLLECTIONS = {
        'US': 'us_w',
        'EAST_COAST': 'eastCoast_w',
        'NEW_ENGLAND': 'newEngland_w',
        'CENTRAL_ATLANTIC': 'centralAtlantic_w',
        'LOWER_ATLANTIC': 'lowerAtlantic_w',
        'MIDWEST': 'midwest_w',
        'GULF_COAST': 'gulfCoast_w',
        'ROCK_MOUNTAINS': 'rockMountains_w',
        'WEST_COAST': 'westCoast_w'
    }

    MONTHLY_COLLECTIONS = {
        'US': 'us_m',
        'EAST_COAST': 'eastCoast_m',
        'NEW_ENGLAND': 'newEngland_m',
        'CENTRAL_ATLANTIC': 'centralAtlantic_m',
        'LOWER_ATLANTIC': 'lowerAtlantic_m',
        'MIDWEST': 'midwest_m',
        'GULF_COAST': 'gulfCoast_m',
        'ROCK_MOUNTAINS': 'rockMountains_m',
        'WEST_COAST': 'westCoast_m'
    }

    YEARLY_COLLECTIONS = {
        'US': 'us_a',
        'EAST_COAST': 'eastCoast_a',
        'NEW_ENGLAND': 'newEngland_a',
        'CENTRAL_ATLANTIC': 'centralAtlantic_a',
        'LOWER_ATLANTIC': 'lowerAtlantic_a',
        'MIDWEST': 'midwest_a',
        'GULF_COAST': 'gulfCoast_a',
        'ROCK_MOUNTAINS': 'rockMountains_a',
        'WEST_COAST': 'westCoast_a'
    }

    PREDICTION_TYPES = ['ANNUAL', 'MONTHLY', 'WEEKLY']
    API_UPDATE ='ApiUpdate'
    WEB_SERVICE='WebService'
