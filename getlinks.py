import urllib2
import re

#connect to a URL
website = urllib2.urlopen(url)

#read html code
html = website.read()

#re.findall get all the links in the page
links = re.findall('"((http|ftp)s?://.*?)"', html)
print links
