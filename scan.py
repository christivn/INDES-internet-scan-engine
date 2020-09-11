from os import cpu_count, _exit
from datetime import datetime
import connection as connection
import gui, nmap


def scan(ip, country_code, cidr):
    try:
        now = datetime.now()
        last_scan=now.strftime("%Y/%m/%d %H:%M:%S")
        cur = connection.mydb.cursor()
        cur.execute("UPDATE ip SET last_scan='"+last_scan+"' WHERE ip='"+ip+"'")
        connection.mydb.commit()
        cur.close()

        nm = nmap.PortScanner()
        print("\033[33m[\033[01m"+gui.time()+"] \033[0m\033[33m Scanning ("+ip+")\033[0m - \033[36mcountry: "+country_code+"\033[0m")
        results = nm.scan(ip)
        rleng = len(results["scan"])

        if(rleng!=0):
            results = results["scan"][ip]["tcp"]
            for port in results.keys():
                if(str(results[port]["state"])=="open"):
                    cur = connection.mydb.cursor()
                    cur.execute("INSERT INTO openports (ip,product,version,name,extrainfo,cpe,port,cidr) VALUES ('"+ip.strip()+"','"+str(results[port]["product"]).strip()+"','"+str(results[port]["version"]).strip()+"','"+str(results[port]["name"]).strip()+"','"+str(results[port]["extrainfo"]).strip()+"','"+str(results[port]["cpe"]).strip()+"','"+str(port).strip()+"', '"+str(cidr).strip()+"')")
                    connection.mydb.commit()
                    cur.close()
    except:
        print("\033[31m[ ERROR ]\033[0m")
        _exit(0)


def ByRandom():
    try:
        cur = connection.mydb.cursor()
        cur.execute("select ip.ip,cidr.country_code,cidr.cidr from ip inner join cidr on cidr.cidr=ip.cidr where cidr.scanning=0 and ip.last_scan='0000-00-00 00:00:00' ORDER BY RAND() LIMIT 1")
        resultado = cur.fetchall()
        cur.close()

        ip=resultado[0][0].strip() 
        country_code=resultado[0][1].strip()
        cidr=resultado[0][2].strip()

        cur = connection.mydb.cursor()
        cur.execute("UPDATE cidr SET scanning=1 WHERE cidr='"+cidr+"'")
        connection.mydb.commit()
        cur.close()

        scan(ip,country_code,cidr)

        cur = connection.mydb.cursor()
        cur.execute("UPDATE cidr SET scanning=0 WHERE cidr='"+cidr+"'")
        connection.mydb.commit()
        cur.close()
    except:
        print("\033[31m[ ERROR ]\033[0m")


def byCountry(country_code):
    try:
        cur = connection.mydb.cursor()
        cur.execute("select ip.ip,cidr.cidr from ip inner join cidr on cidr.cidr=ip.cidr where cidr.country_code='"+country_code+"' and cidr.scanning=0 and ip.last_scan='0000-00-00 00:00:00' ORDER BY RAND() LIMIT 1")
        resultado = cur.fetchall()
        cur.close()

        ip=resultado[0][0].strip()
        cidr=resultado[0][1].strip()

        cur = connection.mydb.cursor()
        cur.execute("UPDATE cidr SET scanning=1 WHERE cidr='"+cidr+"'")
        connection.mydb.commit()
        cur.close()

        scan(ip,country_code,cidr)

        cur = connection.mydb.cursor()
        cur.execute("UPDATE cidr SET scanning=0 WHERE cidr='"+cidr+"'")
        connection.mydb.commit()
        cur.close()
    except:
        print("\033[31m[ ERROR ]\033[0m")