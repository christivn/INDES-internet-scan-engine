import os, gui
import scan, generate

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
                try:
                    scan.byCountry(country_code)
                except:
                    print("\033[31m[ ERROR ]\033[0m")
        elif(m2=="2"):
            print("\033[35m+---------------------------------------------------------+\033[0m\033[35m")
            while True:
                try:
                    scan.ByRandom()
                except:
                    print("\033[31m[ ERROR ]\033[0m")
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
                try:
                    generate.byCountryCode(country_code)
                except:
                    print("\033[31m[ ERROR ]\033[0m")
        elif(m=="2"):
            print(">> Insert CIDR (ej: 127.0.0.1/24): ", end="")
            cidr=str(input())
            print("\033[35m+---------------------------------------------------------+\033[0m\033[35m")
            generate.byCIDR(cidr)
        elif(m=="3"):
            print("\033[35m+---------------------------------------------------------+\033[0m\033[35m")
            while True:
                try:
                    generate.randomCIDR()
                except:
                    print("\033[31m[ ERROR ]\033[0m")
        else:
            print("\033[0m")
            os._exit(0)

    elif(m=="3"):
        print("\033[0m")
        os._exit(0)

    else:
        print("\033[0m")
        os._exit(0)

