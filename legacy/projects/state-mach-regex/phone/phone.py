import re # module for processing regular expressions https://docs.python.org/3/library/re.html

# Initial prompt to user
line = input("Enter a phone number to validate or 'exit' when done. ")





while line != "exit":
    phone_ex = r"([0-9]{3}[-][0-9]{3}[-][0-9]{4}|[0-9]{10}|[(][0-9]{3}[)]\s[0-9]{3}[-][0-9]{4}|[0-9]{3}\s[0-9]{3}\s[0-9]{4}|\+..[0-9]{3}[-][0-9]{3}[-][0-9]{4}|\+..[0-9]{10}|\+..[(][0-9]{3}[)]\s[0-9]{3}[-][0-9]{4}|\+..[0-9]{3}\s[0-9]{3}\s[0-9]{4})"

    if re.findall(phone_ex, line):
        num = ''.join(e for e in line if e.isalnum())
        if len(num) == 10:
            area = num[:3]
            prefix = num[3:6]
            suffix = num[6:]
            print('Area Code:', area, '\nPrefix:', prefix, '\nSuffix:', suffix)
        elif len(num) == 12:
            country = num[:2]
            area = num[2:5]
            prefix = num[5:8]
            suffix = num[8:]
            print('Country Code: ', country, '\nArea Code:', area, '\nPrefix:', prefix, '\nSuffix:', suffix)
        else:
            print('No number was found')

    else:
        print('No number was found')
   
    
    
    # As a stretch goal, you can modify your regex to search for country codes
    # too and print that out as well!
    
    
    # Done validating, read in a new line
    line = input("Enter a phone number to validate or 'exit' when done. ")
