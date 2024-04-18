import functions
import ui 

while True:
    ui.main_menu()
    selection = input(">> ")

    match selection:
        case "1":
            print("\n------------------------------------------------")
            print("           Basal Metabolic Rate (BMR)           ")
            print("------------------------------------------------\n")

            weight = int(input("Weight in lbs: "))
            height = int(input("Height in Inches:"))
            age = int(input("Age in years: "))
            gender = input("Male or Female (M/F):").upper()

            if gender == "M":
                bmr = functions.men_bmr(weight, height, age)
                print(f"\n BMR: {bmr:.2f}")
            elif gender == "F":
                bmr = functions.female_bmr(weight, height, age)
                print(f"\n BMR: {bmr:.2f}")

        case "2":
            print("\n------------------------------------------------")
            print("      Total Daily Energy Expenditure (TDEE)     ")
            print("------------------------------------------------\n")
            
            bmr = int(input("BMR: "))
            
            ui.activity_factor_menu()
            activity_factor = int(input("\nActivity Factor: "))
            tdee = functions.factor_activity_level(bmr, activity_factor)

            print(f"\n TDEE: {tdee}")