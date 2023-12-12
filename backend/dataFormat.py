
# Get the values I want from the API data
def getData(input):

    kelvin = input['main']['temp']
    city = input['name']
    country = input['sys']['country']
    description = input['weather'][0]['description']
    icon = input['weather'][0]['icon']

    celsius = kelvin - 273.15
    full_location = f'{city}, {country}'

    report_data = {}
    report_data['temp'] = celsius
    report_data['location'] = full_location
    report_data['description'] = description
    report_data['icon'] = icon

    return report_data
