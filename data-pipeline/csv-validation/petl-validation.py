import petl as etl
headers = ('State', 'Jurisdiction', 'County', 'Abbreviated District Name', 'Full District Name', 'District Mapped', 'District Mapped But Extinct', 'Overlay', 'Type of Zoning District', 'Affordable Housing District', 'Elderly Housing District', '1-Family Treatment', '2-Family Treatment', '3-Family Treatment', '4+-Family Treatment',  '1-Family Min. Lot (ACRES)', '1-Family Front Setback (# of feet)', '1-Family Side Setback (# of feet)', '1-Family Rear Setback (# of feet)', '1-Family Max. Lot Coverage - Buildings (%)', '1-Family Max. Lot Coverage - Buildings & Impervious Surface (%)', '1-Family Min. # Parking Spaces', '1-Family Max. Height (# of stories)', '1-Family Max. Height (# of feet)', '1-Family Floor to Area Ratio', '1-Family Min. Unit Size (SF)', '2-Family Affordable Housing Only', '2-Family Elderly Housing Only', '2-Family Min. Lot (ACRES)', '2-Family Max. Density (UNITS/ACRE)', '2-Family Front Setback (# of feet)', '2-Family Side Setback (# of feet)', '2-Family Rear Setback (# of feet)', '2-Family Max. Lot Coverage - Buildings (%)', '2-Family Max. Lot Coverage - Buildings & Impervious Surface (%)', '2-Family Min. # Parking Spaces Per Studio or 1BR', '2-Family Min. # Parking Spaces Per 2+ BR', '2-Family Max. Height (# of stories)', '2-Family Max. Height (# of feet)', '2-Family Floor to Area Ratio', '2-Family Min. Unit Size (SF)', '3-Family Affordable Housing Only', '3-Family Elderly Housing Only', '3-Family Min. Lot (ACRES)', '3-Family Max. Density (UNITS/ACRE)', '3-Family Front Setback (# of feet)', '3-Family Side Setback (# of feet)', '3-Family Rear Setback (# of feet)', '3-Family Max. Lot Coverage - Buildings (%)', '3-Family Max. Lot Coverage - Buildings & Impervious Surface (%)', '3-Family Min. # Parking Spaces Per Studio or 1BR', '3-Family Min. # Parking Spaces Per 2+ BR', '3-Family Connection to Sewer and/or Water Required', '3-Family Connection or Proximity to Public Transit Required', '3-Family Max. Height (# of stories)', '3-Family Max. Height (# of feet)', '3-Family Floor to Area Ratio', '3-Family Min. Unit Size (SF)', '3-Family Max. # Bedrooms Per Unit', '4+-Family Affordable Housing Only', '4+-Family Elderly Housing Only', '4+-Family Min. Lot (ACRES)', '4+-Family Max. Density (UNITS/ACRE)', '4+-Family Front Setback (# of feet)', '4+-Family Side Setback (# of feet)', '4+-Family Rear Setback (# of feet)', '4+-Family Max. Lot Coverage - Buildings (%)', '4+-Family Max. Lot Coverage - Buildings & Impervious Surface (%)', '4+-Family Min. # Parking Spaces Per Studio or 1BR', '4+-Family Min. # Parking Spaces Per 2+ BR', '4+-Family Connection to Sewer and/or Water Required', '4+-Family Connection or Proximity to Public Transit Required', '4+-Family Max. Height (# of stories)', '4+-Family Max. Height (# of feet)', '4+-Family Floor to Area Ratio', '4+-Family Min. Unit Size (SF)', '4+-Family Max. # Bedrooms Per Unit', '4+-Family Max. # Units Per Building', 'Affordable Housing (AH) Treatment', 'AH - Definition', 'AH - Elderly Housing Only', 'AH Min. Lot (ACRES)', 'AH Max. Density (UNITS/ACRE)', 'AH Min. # Parking Spaces Per Studio or 1BR', 'AH Min. # Parking Spaces Per 2+ BR', 'AH Connection to Sewer and/or Water Required', 'AH Connection or Proximity to Public Transit Required', 'AH Min. Unit Size (SF)', 'AH Max. # Bedrooms Per Unit', 'AH Max. # Units Per  Building', 'Accessory Dwelling Unit (ADU) Treatment', 'ADU Employee or Family Occupancy Required', 'ADU Renter Occupancy Prohibited', 'ADU Owner Occupancy Required', 'ADU Elderly Housing Only', 'ADU Min. Lot (acres)', 'ADU Min. # Parking Spaces (Additional to Main Unit)', '"ADU Restricted to Only Primary Structure (i.e., No Outbuildings like Garages)"', 'ADU Max. Size (% of Main Unit)', 'ADU Max. Size (SF)', 'ADU Max. # Bedrooms Per Unit', 'Planned Residential Development (PRD) Treatment', 'Mobile or Manufactured Home Park (Y/N)', 'PRD Min. Lot (Acres)', 'PRD Max. Density (Units/Acre)', 'PRD Max. # Units Per Development', 'Special Notes', 'Tooltip Notes')

# Exception Classes
class InvalidStateException(Exception):
  pass
class InvalidJurisdictionException(Exception):
  pass

class InvalidCountyException(Exception):
  pass

# Validators 
def validate_state(val):
  if val != "HI":
    raise InvalidStateException

# TODO: Verify jurisdiction based on the file passed in
# TODO: Account for okinas in Hawaii? 
def validate_jurisdiction(val):
  jurisdictions = ["Hawaii", "Kauaʻi", "Maui", "Honolulu"]
  if val not in jurisdictions:
    raise InvalidJurisdictionException

# TODO: Verify jurisdiction based on the file passed in
# TODO: Account for okinas in Hawaii? 
def validate_county(val):
  counties = ["Hawaii", "Kauaʻi", "Maui", "Honolulu"]
  if val not in counties:
    raise InvalidCountyException

# TODO: Determine constraints for abbreviated district names
# TODO: Verify that abbreviated district names can't be only numbers
def validate_abbr_district_name(val):
  if not isinstance(val,str) or val.isnumeric():
    raise ValueError

constraints = [
    dict(name='state_test', field='State', test=validate_state),
    dict(name='jurisdiction_test', field='Jurisdiction', test=validate_jurisdiction),
    dict(name='county_test', field='County', test=validate_county),
    dict(name='abbr_district_name_test', field='Abbreviated District Name', test=validate_abbr_district_name),
]

table_full = etl.fromcsv('honolulu.csv')
table = etl.tail(table_full, table_full.len() - 2)
problems = etl.validate(table, constraints=constraints, header=headers)
print(problems.lookall())