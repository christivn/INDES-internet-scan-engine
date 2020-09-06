from os import cpu_count
import gui, nmap
import threading

class Thread(threading.Thread):
    def run(self):
        ip="204.90.53.119"
        country_code="es"

        nm = nmap.PortScanner()
        print("\033[35m[\033[01m"+gui.time()+"] ["+self.getName()+"]\033[0m\033[35m Scanning ("+ip+") - country: "+country_code+"\033[0m")
        results = nm.scan(ip)["scan"][ip]

        organization = results["hostnames"][0]["name"]
        open_ports_all = results["tcp"]

        leng=len(open_ports_all)
        open_ports=[]
        
        print("\n"+str(results))

for i in range(cpu_count()):
    t = Thread()
    t.start()