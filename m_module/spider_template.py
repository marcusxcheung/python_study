
'''
This is the Python Spider file for Marcus development used.
Lastest update: 2018.5.10
'''

import urllib2
import urllib
import re

class M_SPIDER:
    def __init__(self, target_url):
        self.target_url = target_url

    def getPage(self):
        try:
            url = self.target_url
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print response.read()
            return response
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"reason", e.reason
                return None

# ===============================================================
# Code Running Here

# Target Url
target_url = 'https://www.google.com.hk/'
self_headers = {}




target_obj = M_SPIDER(target_url)
target_obj.getPage()
