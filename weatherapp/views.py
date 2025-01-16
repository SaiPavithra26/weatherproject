from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


# Create your views here.
def home(request):
    if 'city' in request.POST:
        print("HELLO")
        city = request.POST['city']
    else:
        print("HI")
        city = 'indore'

    url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=04d2a2eeaddfe6f3fa19940a79e45a76'
    PARAMS = {'units':'metric'}

    API_KEY = 'AIzaSyCCxrZymcwbVq65vTKddzP3BWdoLm4Viik'

    SEARCH_ENGINE_ID = 'd73d8ac18bc254411'

    query = city+" 1920x1080"

    page = 1
    start = (page-1) * 10 + 1
    searchType = 'image'
    city_url= f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data= requests.get(city_url).json()
    count=1
    search_items=data.get("items")
    image_url = search_items[1]['link']

    try:
        data = requests.get(url,params=PARAMS).json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        day = datetime.date.today()
        return render(request,'index.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city , 'exception_occurred':False ,'image_url':image_url})
    
    
    except KeyError:
        exception_occured=True
        messages.error(request,'entered data is not availabile')
        day=datetime.date.today()
        return render(request,'index.html',{'description':'clear sky','icon':'01d','temp':'25','day':day,'city':'indore','exception_occured':True})