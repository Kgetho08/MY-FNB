foods=[]
prices=[]
total=0

while True:
    food = input("Enter food item to buy(or 'q' to finish): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter price for {food}: R"))
        foods.append(food)
        prices.append(price)
        
        print("-----your order-----")
        
        for food in foods:
            print(food ,end =" ")
            
        for price in prices:
                total += price
                
                print("\n")
        print(f"Total cost: R{total}")
        print("---------------------")