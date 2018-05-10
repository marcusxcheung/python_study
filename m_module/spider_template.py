
'''
This is the Python Spider file for Marcus development used.
Lastest update: 2018.5.10
Development Python Environment : 3.6.3

Navigation

1. Get current weather
'''



# Import Required Module
import sys
import chardet
from bs4 import BeautifulSoup
import urllib.request





class m_Spider:
    def __init__(self, target_url, self_headers):
        self.target_url = target_url
        self.self_headers = self_headers

    def get_Page(self):
        # Setup the parameter
        target_url = self.target_url
        self_headers = self.self_headers

        # Main function
        request = urllib.request.Request(url=target_url, headers=self_headers)
        response = urllib.request.urlopen(request)
        html = response.read()
        charset = chardet.detect(html)
        html_encoding = charset['encoding']
        html = html.decode(html_encoding)

        return html

        # For testing
        # print(html)

    def test_Page(self, html_content):
        html_content = html_content
        print(html_content)


    #  Get current weather
    def get_Weather(self, html_content):
        final = []
        bs = BeautifulSoup(html_content, 'html.parser') # Create BeautifulSoup Object

        body = bs.body # Get body content
        data = body.find('div', {'id' : '7d'}) # Find the div which id = '7d'
        ul = data.find('ul')
        li = ul.find_all('li')

        for day in li: # Go through all the content in li
            temp = []
            date = day.find('h1').string # Find the date
            temp.append(date)
            p_tag = day.find_all('p')
            temp.append(p_tag[0].string,)
            if p_tag[1].find('span') is None:
                temperature_highest = None
            else:
                temperature_highest = p_tag[1].find('span').string  # Find the highest temperature
                temperature_highest = temperature_highest.replace('℃','')
            temperature_lowest = p_tag[1].find('i').string  # Find the lowest temperature
            temperature_lowest = temperature_lowest.replace('℃', '')
            temp.append(temperature_highest)  # Add the highest temperature
            temp.append(temperature_lowest)  # Add the lowest temperature
            final.append(temp)  # Add the result to final

        print(final)







# ===============================================================
# Code Running Here

# Setup the required data
target_url = 'http://www.weather.com.cn/weather/101280601.shtml'
self_headers = {'Upgrade-Insecure-Requests':'1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

# -------------
# Get html content function
target_obj = m_Spider(target_url, self_headers)
target_obj_htmlcontent = target_obj.get_Page()
# -------------



# -------------
# Get current weather function here
# target_obj.get_Weather(target_obj_htmlcontent)
# -------------


