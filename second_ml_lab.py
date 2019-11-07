import stdiomask 
  
try: 
    p = stdiomask.getpass("enterrr pass:") 
except Exception as error: 
    print('ERROR', error) 
else: 
    print('Password entered:', p)
    input("prompt: ")
