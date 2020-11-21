def make_cars(manufacturer,model_name,**options):
    """Printing the car information."""
    car_info = {}
    car_info['manufacture'] = manufacturer
    car_info['model'] = model_name
    for option , value in options.items():
        car_info[option] = value
    return car_info

my_car = make_cars('honda','jji',color = 'yellow')
print(my_car)

