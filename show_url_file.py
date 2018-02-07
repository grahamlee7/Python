"""
 Show URLs in a packet capture file
 Written Aug 2013 by Graham Lee
 Reference code: SANS
 A Taxonomy of Python Libraries Helpful for Forensic Analysis
 Converted to python3 Feb 2018
"""
import sys, string
# Get Filename
if (len(sys.argv) == 1):
 print ("Usage: show_url filename | sort -f | uniq ")
else:  # good to go
    print ("Checking URLs in " + str(sys.argv[1]) + ".")
    print (" ")
    # Open textfile
    textfile = open(sys.argv[1],'rb')	# binary option needed by python3
    lines = textfile.readlines()
    # Search file
    url_word = 0
    ssl_word = 0
    xml_word = 0
    pki_word = 0
    pki_thawte = False
    pki_verisign = False
    ssl_dict = ['.rsa', '.crl', '.ssl', 'pki.', 'thawte', 'verisign']
    for line in lines:
        Words=line.split()
        for eachWord in Words:
                isPKI = False
                eachWord = str.lower(str(eachWord))		# python3 does not like bytes 
                if len(eachWord) >=74: # truncate
                  eachWord = eachWord[0:70] + "..." 
                i = 0
                while i < len(ssl_dict): # check for PKI
                   if ssl_dict[i] in eachWord:
                      if(eachWord != ssl_dict[i]): # ignore single keywords
                         pki_word = pki_word + 1
                         # print "  PKI " + eachWord
                         isPKI = True
                         if ssl_dict[i] == 'thawte':
                           pki_thawte = True
                         if ssl_dict[i] == 'verisign':
                           pki_verisign = True
                   i = i+1				
                if not isPKI:				   
                  if "https://" in eachWord:
                      ssl_word = ssl_word + 1
                      print ("  SSL " + eachWord)
                  elif (("xml" in eachWord) \
                    or ("w3.org" in eachWord)):
                    xml_word = xml_word + 1
                    # print ("  XML " + eachWord)
                  elif (("http://" in eachWord) or (".com" in eachWord) \
                    or ("www." in eachWord)):
                    url_word = url_word + 1
                    print ("  URL " + eachWord)
    if (url_word):
      print (str(url_word) + " URLs,",)
    if (pki_word):
      print (str(pki_word) + " PKI",)
      if pki_thawte: print (" Thawte",)
      if pki_verisign: print(" Verisign",)
    print (" ")
	
