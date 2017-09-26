import cookielib
import urllib2
import mechanize


# Browser
br = mechanize.Browser()

# Enable cookie support for urllib2
cookiejar = cookielib.LWPCookieJar()
br.set_cookiejar( cookiejar )

# Broser options
br.set_handle_equiv( True )
br.set_handle_gzip( True )
br.set_handle_redirect( True )
br.set_handle_referer( True )
br.set_handle_robots( False )

# ??
br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 )

br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]

# authenticate
br.open("http://210.212.85.155/accounts/login/")
br.select_form(nr = 0)
# these two come from the code you posted
# where you would normally put in your username and password
br[ "login" ] = #######
br[ "password" ] = ####
res = br.submit()

print "Success!\n"
logincheck = res.read()
#print logincheck

from bs4 import BeautifulSoup

soup = BeautifulSoup(logincheck,"html5lib")

t=soup.findAll('div',{'class':'post_head col sm-col sm-col-8'})


for res in t:
    print res.text
