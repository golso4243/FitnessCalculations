
def men_bmr(weight, height, age):
    return 88.362 + (13.397 * (weight * 0.453592)) + (4.799 * (height * 2.54)) - (5.677 * age)

def female_bmr(weight, height, age):
    return 447.593 + (9.247 * (weight * 0.453592)) + (3.098 * (height * 2.54)) - (4.330 * age)

def factor_activity_level(bmr, activity_factor):
    if activity_factor == 1:
        return bmr * 1.2
    elif activity_factor == 2:
        return bmr * 1.375
    elif activity_factor == 3:
        return bmr * 1.55
    elif activity_factor == 4:
        return bmr * 1.725
    elif activity_factor == 5:
        return bmr * 1.9