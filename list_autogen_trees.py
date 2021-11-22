import os
import json

from rmgpy.molecule.molecule import *
from rmgpy.species import *
from rmgpy.data.rmg import RMGDatabase
from rmgpy.species import Species
from rmgpy import settings


def save_sensitivity(family):
    """
    Function to compute partial sensitivities once 
    """
    templateRxnMap = family.get_reaction_matches(
        thermo_database=database.thermo,
        remove_degeneracy=True,
        get_reverse=True,
        exact_matches_only=False,
        fix_labels=True
    )
    family.compute_sensitivities(templateRxnMap)
    family.check_tree()
    family.save(os.path.join(settings['database.directory'], 'kinetics', 'families', family_name))


database = RMGDatabase()

database.load(
    path=settings['database.directory'],
    thermo_libraries=['primaryThermoLibrary'],
    transport_libraries=[],
    reaction_libraries=[],
    seed_mechanisms=[],
    kinetics_depositories=['training'],
    kinetics_families='all',
    depository=False,
)

auto_generated_families = []
for family_name in database.kinetics.families.keys():
    if database.kinetics.families[family_name].auto_generated:
        auto_generated_families.append(family_name)

for i, family_name in enumerate(auto_generated_families):
    print(f'Computing sensitivity for {family_name}\t {i}/{len(auto_generated_families)}')
    save_sensitivity(database.kinetics.families[family_name])



# print('\nThese families are auto-generated')
# for family_name in database.kinetics.families.keys():
#     try:
#         if database.kinetics.families[family_name].auto_generated
#     except NameError:
#         pass
# ['1+2_Cycloaddition']