rivers = {
    'nile': 'egypt',
    'ganga':'india',
    'yamuna':'india',
}

for river,country in rivers.items():
    print("The " + river.title() + " runs through " + country.title())

print("\nThe name of each river:")
for river in rivers.keys():
    print("-" + river.title())

print("\nThe name of each country:")
for country in rivers.values():
    print("-" + country.title())
    