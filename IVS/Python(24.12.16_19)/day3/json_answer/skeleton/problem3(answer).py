import requests
from pprint import pprint

def get_weather():
    api_key ='9fa589f18669c246b5a87a3d5040e178'
    city = "Seoul,KR"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.

    # 전체 url
    # http://api.openweathermap.org/data/2.5/weather?q=Seoul,KR&appid=9fa589f18669c246b5a87a3d5040e178
    response = requests.get(url).json()
    
    temperature = response['main']['temp']
    print(f'캘빈 온도 : {temperature}K')

    temperature_celsius = temperature - 273.15
    # 부동 소수점
    # a = 2.1 - 1.0
    # 1.10000000000002
    print(f'섭씨 온도 : {temperature_celsius:.2f}C')
    return response


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':

    result = get_weather()
    # pprint(result)
