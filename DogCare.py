food_guess = int(input("Enter your guess for the food: "))

price_per_kg = 5.50

final_food = 0

while True: 
    input_from_user = input("Enter daily food intake (grams): ")
 
    if input_from_user.lower() == 'stop':
        if final_food <= food_guess * 1000:
            leftovers = food_guess * 1000 - final_food
            spent_price = leftovers / 1000 * price_per_kg
            print(f"Food is enough! Leftovers: {leftovers} grams")
            print(f"So you spent {spent_price:.2f} leva for food.")
        else:
            needed_food = final_food - food_guess * 1000
            spent_price = (needed_food / 1000) * price_per_kg
            print(f"Food isn't enough. You need {needed_food} grams")
            print(f"So you need {spent_price:.2f} more leva for food.")
        break
    else:
        final_food += int(input_from_user)