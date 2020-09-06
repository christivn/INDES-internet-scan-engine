import os, gui, nmap
from generate import byCountryCode, randomCIDR

while True:
    gui.banner()
    m=gui.select()

    if(m=="1"):
        gui.bannerNoAuthor()
        while True:
            os.system("scan.py 1")

    elif(m=="2"):
        gui.bannerNoAuthor()
        m2=gui.select_generate()
        if(m2=="1"):
            print(">> Insert country code: ", end="")
            country_code=str(input())
            byCountryCode(country_code)
        elif(m=="2"):
            randomCIDR()
        else:
            print("\033[0m")
            os._exit(0)

    elif(m=="3"):
        gui.bannerNoAuthor()
        os.system("search.py 1")

    else:
        print("\033[0m")
        os._exit(0)

