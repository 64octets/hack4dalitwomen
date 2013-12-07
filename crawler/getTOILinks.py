# requisites:
#
# pip install BeautifulSoup
# pip install html5lib

from bs4 import BeautifulSoup
import urllib2,re

def getLinksFromURL(theURL, linkPattern):
    req = urllib2.Request(theURL)
    resp = urllib2.urlopen(req)
    thePage = resp.read()
    soup = BeautifulSoup(thePage,'html5lib')
    matcher = re.compile(linkPattern)
    for link in soup.find_all('a'):
        linkhref = link.get('href')
        if linkhref != None and linkhref != '' and matcher.match(linkhref):
            print (linkhref)

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
