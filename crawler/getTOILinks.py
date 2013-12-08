# requisites:
#
# pip install BeautifulSoup
# pip install html5lib

from bs4 import BeautifulSoup
from goose import Goose
import urllib2,re

satabdi_api_key = "7099dd459ad18fb49672e969d398119e3ad519d0"
debamitro_api_key = "cb958ffa80165e692f5aaa2f72f7537b950eb563"
ALCHEMY_PREFIX = 'http://access.alchemyapi.com/calls/url/URLGetText?apikey=' + debamitro_api_key + '&outputMode=json&extractLinks=1&url='

def parseUsingAlchemy(dUrl):
    totalUrl = ALCHEMY_PREFIX + dUrl;
    #return totalUrl
    return urllib2.urlopen(totalUrl).read()

def parseUsingGoose(dUrl):
    return Goose().extract(url=dUrl).cleaned_text

def getLinksFromURL(theURL, linkPattern):
    soup = BeautifulSoup(urllib2.urlopen(theURL).read(),'html5lib')
    matcher = re.compile(linkPattern)
    for link in soup.find_all('a'):
        linkhref = link.get('href')
        if linkhref != None and linkhref != '' and matcher.match(linkhref):
            resData = parseUsingGoose(linkhref)
            print (resData)


import calendar

starttime = 41275
yearToCheck = 2013
TOIlinkPattern = 'http://timesofindia\.indiatimes\.com//.*/articleshow/.*\.cms$'
for mId in range (1, 12):
    nDays = calendar.monthrange (yearToCheck, mId)[1]
    for dId in range (1, nDays):
        dUrl = 'http://timesofindia.indiatimes.com/' + str(yearToCheck) + '/' + str(mId) + '/' + str(dId) + '/archivelist/year-' + str(2013) + ',month-' + str(mId) + ',starttime-' + str(starttime) + '.cms'
        starttime = starttime + 1
        getLinksFromURL (dUrl, TOIlinkPattern)
        
#TOIurl = "http://timesofindia.indiatimes.com/2013/1/9/archivelist/year-2013,month-1,starttime-41283.cms"
#getLinksFromURL (TOIurl, TOIlinkPattern)
