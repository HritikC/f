cities = {
    'mumbai' : {
         'country' : 'india',
         'population': '1.84 crores',
         'facts' : 'Mumbai is the most populous city in India.',
           },
 
'moscow' : {
         'country' : 'russia',
         'population': '1.19 crores (2012)',
         'facts' : 'The Moscow Kremlin is the world’s largest medieval fortress.',
        },
'Islamabad' : {
         'country' : 'pakistan',
         'population': '10.1 lakhs (2017)',
         'facts' : 'Islamabad is the ninth largest city in Pakistan.',
         },
}

for city_names, city_info in cities.items():
    print("\n   \t* " + city_names.title())
    countries = city_info['country']
    population_n = city_info['population']
    fact_s = city_info['facts']

    print("\t  -Country: " + countries.title()) 
    print("\t  -Population: " + population_n.title()) 
    print("\t  -Facts: " + fact_s.title()) 
    