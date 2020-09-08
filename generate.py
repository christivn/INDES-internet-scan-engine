import geoipgen
from gui import time
import connection as connection


def byCountryCode(country_code):
    cur = connection.mydb.cursor()
    cur.execute("select cidr from cidr where country_code='"+country_code+"' and scaned=0 and scanning=0 ORDER BY RAND() LIMIT 1")
    resultado = cur.fetchall()
    cur.close()

    cidr=resultado[0][0]
    ip_list=geoipgen.generate.rangeIP(cidr)

    cur = connection.mydb.cursor()
    cur.execute("UPDATE cidr SET scanning=1 WHERE cidr='"+cidr+"'")
    connection.mydb.commit()
    cur.close()

    for i in range(len(ip_list)):
        try:
            cur = connection.mydb.cursor()
            cur.execute("INSERT INTO ip (cidr,ip) VALUES ('"+cidr+"','"+ip_list[i]+"')")
            connection.mydb.commit()
            cur.close()
            print("\033[34m[\033[01m"+time()+"]\033[0m\033[34m Added ("+ip_list[i]+")\033[0m -\033[36m "+country_code+"\033[0m")
        except:
            print("\033[31m[ "+ip_list[i]+" DUPLICATE ENTRY ]\033[0m")

    cur = connection.mydb.cursor()
    cur.execute("UPDATE cidr SET scaned=1 WHERE cidr='"+cidr+"'")
    connection.mydb.commit()
    cur.close()

    cur = connection.mydb.cursor()
    cur.execute("UPDATE cidr SET scanning=0 WHERE cidr='"+cidr+"'")
    connection.mydb.commit()
    cur.close()



def byCIDR(cidr):
    cur = connection.mydb.cursor()
    cur.execute("select cidr,country_code from cidr where cidr='"+cidr+"'")
    resultado = cur.fetchall()
    cur.close()

    cidr=resultado[0][0]
    country_code=resultado[0][1]
    ip_list=geoipgen.generate.rangeIP(cidr)

    cur = connection.mydb.cursor()
    cur.execute("UPDATE cidr SET scanning=1 WHERE cidr='"+cidr+"'")
    connection.mydb.commit()
    cur.close()

    for i in range(len(ip_list)):
        try:
            cur = connection.mydb.cursor()
            cur.execute("INSERT INTO ip (cidr,ip) VALUES ('"+cidr+"','"+ip_list[i]+"')")
            connection.mydb.commit()
            cur.close()
            print("\033[35m[\033[01m"+time()+"]\033[0m\033[35m Added ("+ip_list[i]+") - "+country_code+"\033[0m")
        except:
            print("\033[31m[ "+ip_list[i]+" DUPLICATE ENTRY ]\033[0m")

    cur = connection.mydb.cursor()
    cur.execute("UPDATE cidr SET scaned=1 WHERE cidr='"+cidr+"'")
    connection.mydb.commit()
    cur.close()

    cur = connection.mydb.cursor()
    cur.execute("UPDATE cidr SET scanning=0 WHERE cidr='"+cidr+"'")
    connection.mydb.commit()
    cur.close()



def randomCIDR():
    cur = connection.mydb.cursor()
    cur.execute("select cidr,country_code from cidr where scaned=0 and scanning=0 ORDER BY RAND() LIMIT 1")
    resultado = cur.fetchall()
    cur.close()

    cidr=resultado[0][0]
    country_code=resultado[0][1]
    ip_list=geoipgen.generate.rangeIP(cidr)

    cur = connection.mydb.cursor()
    cur.execute("UPDATE cidr SET scanning=1 WHERE cidr='"+cidr+"'")
    connection.mydb.commit()
    cur.close()

    for i in range(len(ip_list)):
        try:
            cur = connection.mydb.cursor()
            cur.execute("INSERT INTO ip (cidr,ip) VALUES ('"+cidr+"','"+ip_list[i]+"')")
            connection.mydb.commit()
            cur.close()
            print("\033[35m[\033[01m"+time()+"]\033[0m\033[35m Added ("+ip_list[i]+") - country: "+country_code+"\033[0m")
        except:
            print("\033[31m[ "+ip_list[i]+" DUPLICATE ENTRY ]\033[0m")

    cur = connection.mydb.cursor()
    cur.execute("UPDATE cidr SET scaned=1 WHERE cidr='"+cidr+"'")
    connection.mydb.commit()
    cur.close()

    cur = connection.mydb.cursor()
    cur.execute("UPDATE cidr SET scanning=0 WHERE cidr='"+cidr+"'")
    connection.mydb.commit()
    cur.close()