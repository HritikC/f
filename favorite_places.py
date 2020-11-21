favorite_places = { 
                'hritik' : ['yavatmal','home'],
                'anurag' : ['puna'],
                'arpit' : ['home', 'concert','mumbai'],
                   }

for name,places in favorite_places.items():
    print("\n" +  name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())