import os, gui, nmap
from generate import byCountryCode, randomCIDR, byCIDR
import scan

while True:
    gui.banner()
    m=gui.select()

    if(m=="1"):
        gui.bannerNoAuthor()
        m2=gui.select_scan()
        if(m2=="1"):
            print(">> Insert country code: ", end="")
            country_code=str(input())
            print("\033[35m+---------------------------------------------------------+\033[0m\033[35m")
            while True:
                scan.byCountry(country_code)
        elif(m=="2"):
            print("\033[35m+---------------------------------------------------------+\033[0m\033[35m")
            while True:
                scan.ByRandom()
        else:
            print("\033[0m")
            os._exit(0)

    elif(m=="2"):
        gui.bannerNoAuthor()
        m2=gui.select_generate()
        if(m2=="1"):
            print(">> Insert country code: ", end="")
            country_code=str(input())
            print("\033[35m+---------------------------------------------------------+\033[0m\033[35m")
            while True:
                byCountryCode(country_code)
        elif(m=="2"):
            print(">> Insert CIDR (ej: 127.0.0.1/24): ", end="")
            cidr=str(input())
            print("\033[35m+---------------------------------------------------------+\033[0m\033[35m")
            byCIDR(cidr)
        elif(m=="3"):
            print("\033[35m+---------------------------------------------------------+\033[0m\033[35m")
            while True:
                randomCIDR()
        else:
            print("\033[0m")
            os._exit(0)

    elif(m=="3"):
        gui.bannerNoAuthor()
        os.system("info.py 1")

    else:
        print("\033[0m")
        os._exit(0)

