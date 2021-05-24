import requests
import datetime


def getCovidData(pincode):
    date=datetime.datetime.now()
    datenow=date.date().strftime("%d-%m-%Y")
    url=f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={datenow}"
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
    response=requests.get(url=url,headers=headers)
    return (response.json())