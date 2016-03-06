#!/usr/bin/env python #coding=utf-8
import httplib
import json

httpClient = None
try:
    httpClient = httplib.HTTPConnection('api.map.baidu.com', 80, timeout=30)
    httpClient.request('GET', '/telematics/v3/weather?location=%E5%B9%BF%E5%B7%9E&output=json&ak=KPGX6sBfBZvz8NlDN5mXDNBF&callback=')

    response = httpClient.getresponse()
    s = json.loads(response.read());
    print(s["results"][0]["currentCity"])
    print(s["results"][0]["weather_data"][0]["date"])
    print(s["results"][0]["weather_data"][0]["weather"])
    print(s["results"][0]["weather_data"][0]["wind"])
    print(s["results"][0]["weather_data"][0]["temperature"])

except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()
