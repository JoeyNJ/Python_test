def city_country(city_name, country_name):
    city_names = f"{city_name}, {country_name}"
    return city_names.title()


manila = city_country('manila', 'philippines')
print(manila)

tokyo = city_country('tokyo', 'japan')
print(tokyo)

kyoto = city_country('kyoto', 'japan')
print(kyoto)