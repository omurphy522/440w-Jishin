from enum import Enum

class constantsclass(Enum):

    AUTHENTICATED = "authusr"

    WEEKLY_COLLECTIONS = {
        'US': 'us_all_w',
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
        'US': 'usAll_m',
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
        'US': 'us_all_a',
        'EAST_COAST': 'eastCoast_a',
        'NEW_ENGLAND': 'newEngland_a',
        'CENTRAL_ATLANTIC': 'centralAtlantic_a',
        'LOWER_ATLANTIC': 'lowerAtlantic_a',
        'MIDWEST': 'midwest_a',
        'GULF_COAST': 'gulfCoast_a',
        'ROCK_MOUNTAINS': 'rockMountains_a',
        'WEST_COAST': 'westCoast_a'
    }

    PREDICTION_TYPES = ['ANNUAL, MONTHLY, WEEKLY']

MENU = {
    '1: ': 'Predict average price in United States for a specific year.',
    '2: ': 'Predict average price in United States for a specific month.',
    '3: ': 'Predict average price in United States for a specific week.',
    '4: ': 'Predict average price in a region for a specific year.',
    '5: ': 'Predict average price in a region for a specific month.',
    '6: ': 'Predict average price in a region for a specific week.',
    '7: ': 'Exit'

}
