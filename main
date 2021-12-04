import random 
import string
import json
import colorama
import requests
import time
from colorama import Fore
colorama.init(convert=True)
import os

banner = """░░▄█▀▄─▒▄█▀▀█▒█▀█▀█▒▐█▀▀▄▒▐█▀▀█▌
░▐█▄▄▐█▒▀▀█▄▄░░▒█░░▒▐█▒▐█▒▐█▄▒█▌
░▐█─░▐█▒█▄▄█▀░▒▄█▄░▒▐█▀▄▄▒▐██▄█"""



print("""░░▄█▀▄─▒▄█▀▀█▒█▀█▀█▒▐█▀▀▄▒▐█▀▀█▌
░▐█▄▄▐█▒▀▀█▄▄░░▒█░░▒▐█▒▐█▒▐█▄▒█▌
░▐█─░▐█▒█▄▄█▀░▒▄█▄░▒▐█▀▄▄▒▐██▄█""")

print("""- 1 : Password Generator | - 2 : IP INFO | - 3 : IP PINGER""")
#It was a few indents that caused the error :/
while True:
  while True:
    try:
      choice = int(input("[+] Choice: "))
    except ValueError:
      print("That's not a number, try again.")
      time.sleep(1)
    else:
      break

  def passwordgen():
    print("Astro | MULTITOOL | password generator")

    #password length
    length = int(input('- Enter the length of password: '))

    # DATA

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols

    # DATA

    temp = random.sample(all,length)
    password = "".join(temp)

    all = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(all,length))

    print("YOUR GENERATED PASS IS:"   + password)
    time.sleep(1)

    
  if choice == 1:
    passwordgen()
    
  if choice == 2:
    print("IP LOOKUP")
    class whois:
        def __init__(self):
            print(f"{banner}")
            print(f"Astro | MULTITOOL | IP Lookup")
            self.ipadd = (input(Fore.WHITE + "[+] Input IP:")).strip()

            if self.ipadd.startswith("127") or self.ipadd.startswith("192"):
                print(
                    f"The Input Address is  local host",
                    f"This is not Valid IP Address",
                )
                exit()

        def print_fetched(self):
            response = requests.get(f"http://ip-api.com/json/{self.ipadd}")
            json_response = json.loads(response.text)
            for key, value in json_response.items():
                if value:
                    print(
                        Fore.LIGHTWHITE_EX
                        + f"{key.title()}: {Fore.WHITE} {str(value).strip()}"
                    )


    obj = whois()
    obj.print_fetched()

  if choice == 3:
    print("IP PINGER")
    hostname = input("Hostname or IP:")
    response = os.system("ping -c 1 " + hostname)
    #and then check the response...
    if response == 0:
      print (hostname, 'is up!')
    else:
      print (hostname, 'is down!')
      time.sleep(1)
              
