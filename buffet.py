food_in_restra = ('chai' , 'rota' , 'rice','makhan','pappad')
for food in food_in_restra:
    print(food.title())
print(food_in_restra)

food_in_restra_list = list(food_in_restra)
food_in_restra_list[0] = ('kheer')
food_in_restra_list[1] = ('pani')
food_in_restra = tuple(food_in_restra_list)
for food in food_in_restra:
    print(food.title())
print(food_in_restra)



