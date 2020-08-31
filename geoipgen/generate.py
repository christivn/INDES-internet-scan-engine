from . import subnetCal
from . import functions
from random import randint

def IP(cidr):
    arr=subnetCal.simpleCalculate(cidr)
    min_host=arr[3]
    smin_host=min_host.split(".")

    max_host=arr[4]
    smax_host=max_host.split(".")

    ip=""
    for i in range(4):
        if(smin_host[i]==smax_host[i]):
            ip+=smin_host[i]
        else:
            ip+=str(randint(int(smin_host[i]), int(smax_host[i])))
        if(i<3):
            ip+="."
    return ip


def rangeIP(cidr):
    arr=subnetCal.simpleCalculate(cidr)
    min_host=arr[3]
    max_host=arr[4]
    ip_list=functions.ips(min_host, max_host)
    return ip_list


def randomCIDR(country):
    folder_cidr = open('geoipgen/ipv4/'+country+'.cidr', 'r') 
    cidr_lines = folder_cidr.readlines()
    return cidr_lines[randint(0,len(cidr_lines))].strip()