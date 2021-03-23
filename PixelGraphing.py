try:
    y=0
    import os
    import webbrowser
    from os import path, system
    import pyautogui
    import time
    from matplotlib import pyplot as plt
    import numpy as np
    from PIL import Image
    import sys
    import time
    from colorama import init, Fore, Back, Style
    import logging
    import datetime
    import getpass
    import socket
    from selenium import webdriver
    import itertools
    import threading
    import playsound
except ImportError:
    print("Trying to install the required modules! THIS MAY DISPLAY LARGE ERRORS!\nPlease try to run this script again once all of the modules have been successfully installed.\n\n")
    input("press enter to start installing... ")
    system("py -m pip install -r requirements.txt")
    system("python -m pip install -r requirements.txt")
    system("python3 -m pip install -r requirements.txt")
    input("\n\ndone installing modules! please restart the script now. Press enter to continue... ")
    quit()

init()


print('Launching "Everest"...')
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading... ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(2)
done = True
print(' Starting...')
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['}', '.', '[', '\\']):
        if done:
            break
        sys.stdout.write('\rloading... ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(3)
done = True
cls = lambda: system('cls')
Sound=input('  Do you want to play music y/n: ')

if Sound=="y":
    
    path = './Music'

    files = os.listdir(path)

    for f in files:
        print(f)
    PickaMusic=input('  What music would you like to play:')
    playsound.playsound(PickaMusic, False)

if Sound == "n":
    system('cls')

system('cls')
print(Fore.GREEN + "           ┌─────────────────────────────────┐")
time.sleep(0.3)
print(Fore.GREEN + "           |___                          _   |")
time.sleep(0.3)
print(Fore.GREEN + "           || __|__ __ ___  _ _  ___  ___| |_|")
time.sleep(0.3)
print(Fore.GREEN + "           || _| \ V // -_)| '_|/ -_)(_-/|  _|")
time.sleep(0.3)
print(Fore.GREEN+ "           ||___| \_/ \___||_|  \___|/__/ \__|")
time.sleep(0.3)
print(Fore.GREEN + "           └─────────────────────────────────┘")
(Fore.MAGENTA + "Date: %s" % time.ctime())
time.sleep(0.3)
string = 'Follow me on Twitter! @LaiBranden...'
substr = ""

for char in string:
    substr += char
    print(substr, end="\r")
    time.sleep(0.03)
print('Welcome to Everest..., '+getpass.getuser()+"!")
print(Fore.WHITE + socket.gethostname() + Fore.WHITE + '!')
string ='Welcome to Everest..., '+getpass.getuser()+"!"
substr = ""

for char in string:
    substr += char
    print(substr, end="\r")
    time.sleep(0.03)
print('Welcome')
name = str(input(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.GREEN+'> What is your Username?: '))
x=name
print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +"Hello" + " "+name + "!")

if name == 'Branden Lai':
  print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.GREEN + 'Ethernet adapter Radmin VPN: Connection-specific DNS Suffix Disconnected... Ip:192.432.432 Connected... Connection Radmin Unistalled...Ethernet adapter VirtualBox Host-Only Network...Ip Grabbed Successful...Media disconnected...Wireless LAN adapter Wi-Fi Disconnected...Tunnel adapter Teredo Tunneling Pseudo-Interface Connected...Port:2138 Tunneled...Ip Grabbed...Requirement already satisfied:...Requirement already satisfied:...Requirement already satisfied:...Requirement already satisfied: Path:C:/Users/Lib/Desktop/Image Project/697033-32983.jpg Installed...Requirement already satisfied...Requirement already satisfied...Requirement already satisfied...Requirement already satisfied...Requirement already satisfied... GET HACKED KID :D ')
  system("pip3 install aiohttp")
  system("ipconfig")
  print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.BLUE + "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO...https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO...https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO...https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO...https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO...https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO...https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO...https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO...https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO...https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO...https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO...https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO...https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO...https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO...https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO...")
  pyautogui.click(x=310, y=618)

  pyautogui.click(x=310, y=218)
  pyautogui.click(x=310, y=218)
  pyautogui.click(x=310, y=618)
  pyautogui.click(x=310, y=418)
  pyautogui.click(x=310, y=418)
  pyautogui.click(x=310, y=418)
  system(Fore.MAGENTA+"ipconfig")
  system(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +"prompt Branden Lai Is OP get Rick ROlled")
  time.sleep(2)

  system("ipconfig")
  pyautogui.click(x=310, y=218)
  system("ipconfig")
  pyautogui.click(x=310, y=218)
  system("ipconfig")
  system("ipconfig")
  pyautogui.click(x=310, y=218)
  system("ipconfig")
  pyautogui.click(x=310, y=218)
  system("ipconfig")
  pyautogui.click(x=310, y=218)
  system("pip3 install asyncio")
  system("tree")
  system("pip install beautifulsoup4")
  system("ipconfig")
  pyautogui.click(x=310, y=218)
  system("ipconfig")
  pyautogui.click(x=310, y=218)
  system("ipconfig")
  system("tree")
  system("tree")
  pyautogui.click(x=310, y=218)
  system("tree")
  system("tree")
  pyautogui.click(x=310, y=218)
  system("title MY COMPUTER NOW")
  print("Look at your cmd title :>")
  system("tree")
  pyautogui.click(x=310, y=218)
  pyautogui.click(x=310, y=218)
  pyautogui.click(x=310, y=218)
  pyautogui.click(x=310, y=218)
  system("tree")
  pyautogui.click(x=310, y=218)
  system("tree")
  pyautogui.click(x=310, y=218)
  pyautogui.click(x=310, y=218)
  pyautogui.click(x=310, y=218)
  pyautogui.click(x=310, y=218)
  system("tree")
  pyautogui.click(x=310, y=218)
  pyautogui.click(x=310, y=218)
  pyautogui.click(x=310, y=218)
  pyautogui.click(x=310, y=218)
  pyautogui.click(x=310, y=218)
  pyautogui.click(x=310, y=218)
  pyautogui.click(x=310, y=218)


  print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +"I Told you Not to enter my Name :)")

  print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +"Ip grabbed :) Get Rick Rolled Kid :D https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO...https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO...")
  time.sleep(2)
  print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.CYAN + 'Ok BYE BYE :>')
  pyautogui.click(x=310, y=218)
  print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.CYAN + 'I told you not to enter my name KID Listen :) Byeeee')
  system("tree")
  print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.CYAN + 'I told you not to enter my name KID Listen :) Byeeee')
  pyautogui.click(x=310, y=218)
  print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.CYAN + 'I told you not to enter my name KID Listen :) Byeeee')
  system("ipconfig | clip")
  pyautogui.click(x=310, y=3218)
  print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.CYAN + 'I told you not to enter my name KID Listen :) Byeeee')
  print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.CYAN + 'I told you not to enter my name KID Listen :) Byeeee')
  pyautogui.click(x=310, y=218)
  system("ipconfig/all")
  system("ipconfig | clip")
  pyautogui.click(x=310, y=3218)
  system("nslookup google.com")
  system("ipconfig | clip")
  system("tree")
  system("ipconfig | clip")
  pyautogui.click(x=310, y=218)
  system("ipconfig | clip")
  pyautogui.click(x=310, y=218)

  system("ipconfig | clip")
  system("wmic product get name")
  system("tree")
  system("RUNDLL32.EXE powrprof.dll,SetSuspendState 0,1,0")
  exit()
else:

        if name == 'Jason Choe':
            print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.BLUE + "You are my Best friend Forever! Thanks for everything you have done!!! Thanks for the cakes!")
            exit()
        else:
            if name == 'Benjamin King':
                print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.RED + "Thanks for Being my Best friend! I owe you big time!")
                exit()
            else:
                if name == 'Danny Kim':
                    print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.GREEN + "We will Miss you in korea!!! Make sure to keep in contact with us.")
                    exit()
                else:
                    if name == 'Sriram Sivakumar':
                        print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.GREEN + 'Thanks for teaching me coding and using your own time for me! Please keep teaching me and Thanks so much!!!')

                    else:
                        if name == 'Everest':
                            print(Fore.RED + '[Admin]')

Age = int(input(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.CYAN + '> What is your age?: '))
if Age >= 12:
    print('')
else:
    print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.CYAN + 'Sorry! You are too young. Come back when your 12 and older!')
    exit()
option = int(input(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +'[1]: Pixel!:, [2]:Discord(DM)!:, [3]:HandSniperBot(Minecraft):, [4]:IpLoggerLink:   '))


if option == 1:

    MainPage = input(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.MAGENTA + '> Do you want to print your image? y/n:')
    if MainPage == "y":
        print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +'Mainpage')
    else:

        print(f"your path is {path}")
    path = "C:/Users/Branden/Desktop/Image Project/697033-bigthumbnail.jpg"
    matrix = [[[255, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]],
              [[0, 0, 0], [0, 0, 0]]]
    i = Image.open(path).resize((250, 150)).convert("L")
    plt.imshow(i)
    i = np.array(i)
    plt.show()
    for row in i:
        RowString = ""
        for pixel in row:
            if pixel > 112.5:
                RowString = RowString + "#"
            if pixel < 112.5:
                RowString = RowString + " "
        print(RowString)




#Discord(DM)
if option == 2:
    print('Hello World')



#Minecraft HandSniperBot
if option == 3:
    print('Hello World')


#IpLoggerLink
if option ==4:
    print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.YELLOW+"[AI]+Opening 000webhost Free...")
    time.sleep(3)
    print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.YELLOW+"[AI]"+ webbrowser.open('https://000webhost.com/'))

    print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.YELLOW+"[Steps]"+Fore.GREEN+ "Please click Sign In!")
    print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" +Fore.YELLOW+"[Steps]"+Fore.GREEN+"Press Enter to continue:")
    print(Fore.RED + "[" + Fore.BLUE + getpass.getuser() + Fore.RED + "@"+Fore.BLUE+"Everest" + Fore.RED + "]" + Fore.YELLOW +"[Bot]")
    webbrowser.open("https://000webhost.com/")
    driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://000webhost.com/")
    driver.refresh()
    driver.find_element_by_link_text("LOG IN WITH GOOGLE").click()
    driver.close()




