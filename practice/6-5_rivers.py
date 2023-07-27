# make a dictionary containing three major rivers and its countries

country_rivers = {'nile': 'egypt', 'yellow river': 'china', 'pasig river': 'philippines',}

for river, country in country_rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
    
    
for river in country_rivers.keys():
    print(f"All rivers included in the library are {river.title()}.")
    
for country in country_rivers.values():
    print(f"All countries included in the library are {country.title()}.")