
#getpass.getpass(prompt='Password: ', stream=None)
# A simple Python program to demonstrate  
# getpass.getpass() to read password 
import getpass 
  
try: 
    p = getpass.getpass("enterrr pass:") 
except Exception as error: 
    print('ERROR', error) 
else: 
    print('Password entered:', p)
