def describe_city(name, country='Japan'):
    """Print a simple message about the country."""
    print(f"The city {name} is in {country}")
    
describe_city('Kyoto')
describe_city('Tokyo')
describe_city('Manila', 'Philippines')