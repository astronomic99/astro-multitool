import random 
import string
import json
import colorama
import requests
import time
from colorama import Fore
colorama.init(convert=True)
import os
import sys, aiohttp, asyncio

banner = """╔═══╗╔═══╗╔════╗╔═══╗╔═══╗
║╔═╗║║╔═╗║║╔╗╔╗║║╔═╗║║╔═╗║
║║─║║║╚══╗╚╝║║╚╝║╚═╝║║║─║║
║╚═╝║╚══╗║──║║──║╔╗╔╝║║─║║
║╔═╗║║╚═╝║──║║──║║║╚╗║╚═╝║
╚╝─╚╝╚═══╝──╚╝──╚╝╚═╝╚═══╝"""


class WebhookSpammer:

    def __init__(self, webhook: str, msg: str, tasks: int):
        self.clear = lambda: os.system("cls; clear")
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47"}
        self.webhook = webhook
        self.payload = {"content": msg}
        self.tasks = tasks

    async def webhook_spammer(self, session, webhook, amount):
       while True:
           async with session.post(webhook, json=self.payload) as s:
              if s.status in (200, 201, 204):
                  sys.stdout.write(f"-> Sent webhook to channel with {amount} tasks in its payload.\n\n")
              else:
                  json = await s.json()
                  sys.stdout.write(f"-> Error sending webhook with {amount} tasks in its payload.\n-> Message: {json['message']}\n-> Retry After: {json['retry_after']}\n\n")
  
    async def start(self):
        self.clear()
        async with aiohttp.ClientSession(headers=self.headers) as session:
            tasks = []
            for amount in range(self.tasks):
                tasks.append(asyncio.create_task(self.webhook_spammer(session, self.webhook, amount)))
            await asyncio.gather(*tasks)
            tasks.clear()
            
#It was a few indents that caused the error :/
while True:
  print(banner)
  print("""- 1 : Password Generator | - 2 : IP INFO | - 3 : IP PINGER
  | - 4 : WEBHOOK SPAM""")
  while True:
    try:
      choice = int(input("[+] Choice: "))
    except ValueError:
      print("That's not a number, try again.")
      time.sleep(1)
    else:
      break

  def passwordgen():
    print("Astro | MULTITOOL | Password generator")

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
    os.system("clear")

    
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
    time.sleep(5)
    os.system("clear")

  if choice == 3:
    print("IP PINGER")
    hostname = input("Hostname or IP:")
    response = os.system("ping -c 1 " + hostname)
    #and then check the response...
    if response == 0:
      print (hostname, 'is up!')
    else:
      print (hostname, 'is down!')
      time.sleep(5)
      os.system("clear")
      
      
  if choice == 4:
      print(banner)
      try:
        client = WebhookSpammer(
        webhook = input("-> Webhook URL?: "),
        msg = input("-> Message Content?: "),
        tasks = int(input("-> Tasks?: "))
        )
        start_time = time.time()
        asyncio.get_event_loop().run_until_complete(client.start())
        finish_time = round((time.time() - start_time), 4)
        sys.stdout.write(f"-> Finished executing webhook.\n-> Finished in {finish_time}s.")
      except Exception as error:
          sys.stdout.write(f"-> Event loop has ended or you are being ratelimited or was given invalid roles.\n-> Exception: {error}.\n-> Press enter to exit.\n")
          input("-> ")
          os._exit(0)
          os.system("clear")
      	


