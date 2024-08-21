import numpy as np
import pandas as pd

# import CSV
file = 'Parameters.csv'

# Read CSV file, assign column title
Gear = pd.read_csv(file, names=['Name', 'Values', 'Comments'])

# Gear Parameters

# Input Loop
for row in range(0, 3):
    Gear.loc[row, 'Values'] = input(f'Input the value of the {Gear.loc[row, 'Comments']},{Gear.loc[row, 'Name']}: ')

# Parameter Formulas
Gear.loc[:, 'Values'] = pd.to_numeric(Gear.loc[:, 'Values'], errors='coerce')
Gear.loc[3, 'Values'] = 1 / Gear.loc[0, 'Values']  # Addendum
Gear.loc[4, 'Values'] = 1.25 / Gear.loc[0, 'Values']  # Dedendum
Gear.loc[5, 'Values'] = Gear.loc[4, 'Values'] - Gear.loc[3, 'Values']  # Clearance
Gear.loc[6, 'Values'] = Gear.loc[1, 'Values'] / Gear.loc[0, 'Values']  # Pitch circle diameter
Gear.loc[7, 'Values'] = Gear.loc[6, 'Values'] * np.cos(np.deg2rad(Gear.loc[2, 'Values']))  # Base circle diameter
Gear.loc[8, 'Values'] = Gear.loc[6, 'Values'] + 2 * Gear.loc[3, 'Values']  # Addendum circle diameter
Gear.loc[9, 'Values'] = Gear.loc[6, 'Values'] - 2 * Gear.loc[4, 'Values']  # Dedendum circle diameter
Gear.loc[10, 'Values'] = np.rad2deg(
    np.sqrt(Gear.loc[6, 'Values'] ** 2 - Gear.loc[7, 'Values'] ** 2) / Gear.loc[7, 'Values']) - Gear.loc[
                             2, 'Values']  # Alpha
Gear.loc[11, 'Values'] = 360 / (4 * Gear.loc[1, 'Values']) - Gear.loc[10, 'Values']  # angle btw buttom of teeth and centerline
Gear.loc[12, 'Values'] = (360 / (4 * Gear.loc[1, 'Values']) - Gear.loc[10, 'Values']) * 2   # beta

print()

# Print output
for row in Gear.index:
    print(f'{Gear.loc[row, 'Comments']},{Gear.loc[row, 'Name']} = {Gear.loc[row, 'Values']}')

# Write to text file
with open('Data.txt'  'w') as fileID:
    for row in Gear.index:
        # Conditional statement for columns whose values are in degrees (For Solidworks)
        if row in [2, 7, 10, 11]:
            fileID.write(f'"{Gear.loc[row, 'Comments']},{Gear.loc[row, 'Name']}" = {Gear.loc[row, 'Values']}deg\n')
        else:
            fileID.write(f'"{Gear.loc[row, 'Comments']},{Gear.loc[row, 'Name']}" = {Gear.loc[row, 'Values']}\n')

fileID.close()