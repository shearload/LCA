# Embodied Carbon Calculator Script
# wbinder
# 16.12.2025

def calculate_embodied_carbon():
    # Define emission factors in kgCO2e per unit based on Ökobaudat 2021-1 
    emission_factors = {
        "concrete": {  # kgCO2e per m3 for concrete grades. No cememnt designation per ökobaudat
            "C25/30": 197,
            "C30/37": 219,
            "C45/55": 286,
            "C50/60": 300
        },
        "steel": {  # kgCO2e per kg for steel types
            "rebar": 0.6834,
            "hot_rolled": 1.125,
            "plate": 1.125,
            "galvanised_sheet": 2.676,
            "intumescent_paint": 1.813
        },
        "timber": {  # kgCO2e per m3 for timber types (Excluding carbon sequestration!)
            "softwood": 57.9,
            "glulam": 153.1,
            "CLT": 134.5,
            "formwork": 296.2 #plywood
        }
    }

    # V.10 with Input fields for proof of concept and testing - run V2 inside Rhino IronPython or process on the CSV file directly
    
    # Input quantities for concrete and concrete grade
    concrete_quantity = float(input("Enter concrete quantity (m3): "))
    concrete_grade = input("Enter concrete grade (C25/30, C30/37, C40/50, C50/60): ")
    
    # Input quantities for steel and steel type
    steel_quantity = float(input("Enter steel quantity (kg): "))
    steel_type = input("Enter steel type (rebar, hot_rolled, plate, galvanised_sheet, intumescent_paint): ")
    
    # Input quantities for timber and timber type
    timber_quantity = float(input("Enter timber quantity (m3): "))
    timber_type = input("Enter timber type (softwood, glulam, CLT, formwork): ")
    
    # Calculate embodied carbon for each material
    concrete_carbon = (emission_factors["concrete"].get(concrete_grade, 0) * concrete_quantity)
    steel_carbon = (emission_factors["steel"].get(steel_type, 0) * steel_quantity)
    timber_carbon = (emission_factors["timber"].get(timber_type, 0) * timber_quantity)
    
    # Total embodied carbon
    total_embodied_carbon = concrete_carbon + steel_carbon + timber_carbon
    
    # Output the results
    print("\n Results")
    print(f"Concrete: {concrete_carbon:.2f} kgCO2e")
    print(f"Steel: {steel_carbon:.2f} kgCO2e")
    print(f"Timber: {timber_carbon:.2f} kgCO2e")
    print(f"\nTotal Embodied Carbon: {total_embodied_carbon:.2f} kgCO2e")
    print("\n")

# Run the embodied carbon calculator
calculate_embodied_carbon()