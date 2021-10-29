import os
import json

from rmgpy.molecule.molecule import *
from rmgpy.species import *
from rmgpy.data.rmg import RMGDatabase
from rmgpy.species import Species
from rmgpy import settings


database = RMGDatabase()

database.load(path=settings['database.directory'],
              thermo_libraries=['Klippenstein_Glarborg2016', 'BurkeH2O2', 'thermo_DFT_CCSDTF12_BAC',
                                'DFT_QCI_thermo', 'primaryThermoLibrary', 'primaryNS', 'NitrogenCurran',
                                'NOx2018', 'FFCM1(-)', 'SulfurLibrary', 'SulfurGlarborgH2S', 'SABIC_aromatics'],
              transport_libraries=[],
              reaction_libraries=[],
              seed_mechanisms=[],  # ['BurkeH2O2inN2','ERC-FoundationFuelv0.9'],
              kinetics_families=[family_name],
              kinetics_depositories=['training'],
              depository=False,  # Don't bother loading the depository information, as we don't use it
              )
