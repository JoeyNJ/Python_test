# cites dictionary with keys and values about that city

cities = {
    'manila': {
        'country': 'philippines',
        'population': 1800000,
        'fact': " is the world's most densely populated city with 111,002 people per square mile",
    },
    'tokyo': {
        'country': 'japan',
        'population': 14000000,
        'fact': " is the world's largest city by urban area and metropolitan area",
    },
    'shanghai': {
        'country': 'china',
        'population': 27000000,
        'fact': " is the country's biggest city and a global financial hub",
    },
}

for city, info in cities.items():
    print(f"{city.title()}'s country is the {info['country'].title()} with population of {info['population']}, fun fact {info['fact']}.")