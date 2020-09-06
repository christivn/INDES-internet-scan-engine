import os
import connection as connection

cur = connection.mydb.cursor()
cur.execute("select count(ip) from ip")
resultado = cur.fetchall()
total=resultado[0][0]

header="[ "+str(total)+" TOTAL IP ]  \033[01mAuthor: Christian Ramos (christivn)\033[0m"

ban="""\033[36m                   
ooooo ooooo      ooo oooooooooo.   oooooooooooo  .oooooo..o 
`888' `888b.     `8' `888'   `Y8b  `888'     `8 d8P'    `Y8 
 888   8 `88b.    8   888      888  888         Y88bo.      
 888   8   `88b.  8   888      888  888oooo8     `"Y8888o.  
 888   8     `88b.8   888      888  888    "         `"Y88b 
 888   8       `888   888     d88'  888       o oo     .d8P 
o888o o8o        `8  o888bood8P'   o888ooooood8 8""88888P'  
\033[33m"""+header.center(59," ")


def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ban)


def bannerNoAuthor():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ban)


def select():
    print("""\033[35m+---------------------------------------------------------+\033[0m\033[35m
|\033[36m   1.  \033[01mStart SCAN\033[0m\033[36m                                        \033[35m|
|\033[36m   2.  \033[01mGenerate ip from ranges\033[0m\033[36m                           \033[35m|
|\033[36m   3.  \033[01mInfo from scans\033[0m\033[36m                                   \033[35m|
|\033[36m   4.  \033[01mExit\033[0m\033[36m                                              \033[35m|
+---------------------------------------------------------+\033[0m\033[0m""")
    print(">> Select: ", end="")
    return str(input())


def select_scan():
    print("""\033[35m+---------------------------------------------------------+\033[0m\033[35m
|\033[32m                 \033[01m[ Scan devices ]\033[0m\033[36m                 \033[35m|
|\033[36m   1.  \033[01mSelect from country code\033[0m\033[36m                          \033[35m|
|\033[36m   2.  \033[01mRandom scan\033[0m\033[36m                                       \033[35m|
+---------------------------------------------------------+\033[0m\033[0m""")
    print(">> Select: ", end="")
    return str(input())

def select_generate():
    print("""\033[35m+---------------------------------------------------------+\033[0m\033[35m
|\033[32m               \033[01m[ Generate ip from ranges ]\033[0m\033[36m               \033[35m|
|\033[36m   1.  \033[01mSelect from country code\033[0m\033[36m                          \033[35m|
|\033[36m   2.  \033[01mRandom CIDR\033[0m\033[36m                                       \033[35m|
+---------------------------------------------------------+\033[0m\033[0m""")
    print(">> Select: ", end="")
    return str(input())