import os, gui, nmap
import multiprocessing

while True:
    gui.banner()
    m=gui.select()

    if(m=="1"):
        os.system("scan.py 1")
    elif(m=="2"):
        os.system("generate.py 1")
    elif(m=="3"):
        os.system("generate.py 1")
    else:
        print("\033[0m")
        os._exit(0)

