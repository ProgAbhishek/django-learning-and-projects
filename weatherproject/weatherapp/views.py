from django.shortcuts import render
import requests
import datetime

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Kathmandu'  # Default city if not provided

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c7e9f203fc4b1f83f6b0aaa335839d04'
    PARAMS ={'units': 'metric'}

    data = requests.get(url, params=PARAMS).json()

    weather_list = data.get('weather')
    if isinstance(weather_list, list) and weather_list:
        description = weather_list[0].get('description', 'Weather data unavailable')
        icon = weather_list[0].get('icon', '01d')
    else:
        description = data.get('message', 'Weather data unavailable')
        icon = '01d'

    main_block = data.get('main') if isinstance(data.get('main'), dict) else {}
    temp = main_block.get('temp', '--')

    day = datetime.date.today()

    return render(
        request,
        'weatherapp/index.html',
        {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
        },
    )
