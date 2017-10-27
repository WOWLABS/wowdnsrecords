#This program is written in Python 3.6.3

#The dnsPtr function has the user enter an IP address and hostname,
#then the dnsReord is created using the input from the user and add domain(as12083.net) to the end of the hostname.
#Last the prgram will loop until the user is finished entering their information then print
#a list of all that was entered.


dnsPtr = []
while True:
    print('Enter an IP address or nothing to stop:')
    userdnsIP = input()
    if userdnsIP == '':
        break
    print('Enter a hostname to be associated with the IP address: or exit to stop')
    dnsHostname = input()
    if dnsHostname == '':
        break
    dnsRecord = userdnsIP + ' ' + 'IN' + ' ' + 'PTR' + ' ' + dnsHostname + '.as12083.net.'
    dnsPtr = dnsPtr + [dnsRecord]

#This will loop for all user input and print them out as a list    
print('Your PTR records are:')
for i in dnsPtr:    
    print(' ' + i)
