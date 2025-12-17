"""Grasshopper Script"""

# Embodied Carbon Calculator Script - grasshopper port
# wbinder
# 16.12.2025
if qty != None:
    if unit == "m3":
        print(material)
        print(round(qty), unit)
        print(round(float(emission_factors)*float(qty),2), "kgC02e")
        error = ""
    if unit == "kg":
        density_steel = 7850 #for steel... adjust later to be dynamic with excel database
        print(material)
        print(round(qty*density_steel), unit)
        print(round(float(emission_factors)*density_steel*float(qty),2), "kgC02e")
        error = ""

else:
    error = "error in quantity"

# Calculated embodied carbon for each material in kgC02e based on BREP quants