import gui, nmap
import multiprocessing

_MAX_ITERATIONS = 1000000000

def thread(num,ip):
    iteration = 0
    while True:
        if iteration >= _MAX_ITERATIONS:
            break

        nm = nmap.PortScanner()
        print("\033[35m[\033[01m"+gui.time()+"] [Thread "+str(num)+"]\033[0m\033[35m Scanning ("+ip+") - Spain\033[0m")
        results = nm.scan(ip)["scan"][ip]

        organization = results["hostnames"][0]["name"]
        open_ports_all = results["tcp"]

        leng=len(open_ports_all)
        open_ports=[]
        print(str(open_ports_all)+" / "+str(leng))
        print("\n"+str(results))

        iteration += 1


if __name__ == '__main__':
    gui.bannerNoAuthor()
    print("\033[35m+---------------------------------------------------------+\033[0m")
    for i in range(1): # cambiar el rango por "multiprocessing.cpu_count()" para activar el multiproceso
        ip="94.210.35.184" #Consulta MYSQL para que cada thread coja una ip diferente y que no trabajen dos en la misma
        multipro = multiprocessing.Process(target=thread, args=(i,ip))
        multipro.start()