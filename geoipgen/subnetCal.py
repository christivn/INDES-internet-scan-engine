def printCalculate(cidr):
    s_cidr=cidr.split("/")

    ip=s_cidr[0]
    binary_ip=""
    s_ip=ip.split(".")
    for i in range(4):
        int_ip=int(s_ip[i])
        str_binary=str(decimalToBinary(int_ip))
        zeros=""
        for i in range(8-len(str_binary)):
            zeros+="0"
        binary_ip+=zeros+str_binary+"."
    binary_ip=binary_ip[:-1]

    binary_mask=""
    binary_wildcard=""
    for i in range(32):
        if(i%8==0 and i!=0):
            binary_mask+="."
            binary_wildcard+="."
        if(i<int(s_cidr[1])):
            binary_mask+="1"
            binary_wildcard+="0"
        else:
            binary_mask+="0"
            binary_wildcard+="1"

    mask=""
    s_binary_mask=binary_mask.split(".")
    for i in range(4):
        mask+=str(int(s_binary_mask[i], 2))
        if(i<3):
            mask+="."

    aux_binary_min_host=""
    change=False
    changeIndex=0
    for i in range(len(binary_ip)):
        if(binary_ip[34-i]=="0" and change==False):
            change=True
            changeIndex=34-i
            aux_binary_min_host+=binary_ip[i]
        else:
            aux_binary_min_host+=binary_ip[i]
    binary_min_host=""
    for i in range(len(aux_binary_min_host)):
        if(i==changeIndex):
            binary_min_host+="1"
        else:
            binary_min_host+=aux_binary_min_host[i]

    binary_max_host=""
    for i in range(len(binary_mask)):
        if(binary_mask[i]=="0"):
            if(i==changeIndex):
                binary_max_host+="0"
            else:
                binary_max_host+="1"
        else:
            binary_max_host+=binary_ip[i]

    min_host=""
    s_binary_min_host=binary_min_host.split(".")
    for i in range(4):
        min_host+=str(int(s_binary_min_host[i], 2))
        if(i<3):
            min_host+="."
    
    max_host=""
    s_binary_max_host=binary_max_host.split(".")
    for i in range(4):
        max_host+=str(int(s_binary_max_host[i], 2))
        if(i<3):
            max_host+="."

    zero_bits=0
    for i in range(4):
        zero_bits+=s_binary_mask[i].count("0")
    total_host=pow(2,zero_bits)-2

    print("""\033[34m+--------------------------------------------------------+\033[0m
\033[32m\033[01mNETWORK:\033[0m """+cidr+"""
\033[32m\033[01mIP:\033[0m      """+ip+"""
\033[32m\033[01mMASK:\033[0m    """+mask+"""
\033[32m\033[01mRANGE:\033[0m   """+min_host+""" / """+max_host+"""
\033[34m+--------------------------------------------------------+\033[0m 
\033[36m\033[01mBINARY IP:\033[0m       """+binary_ip+"""
\033[36m\033[01mBINARY MASK:\033[0m     """+binary_mask+"""
\033[36m\033[01mBINARY WILDCARD:\033[0m """+binary_wildcard+"""

\033[36m\033[01mBINARY MIN HOST:\033[0m """+binary_min_host+"""
\033[36m\033[01mBINARY MAX HOST:\033[0m """+binary_max_host+"""
\033[34m+--------------------------------------------------------+\033[0m
\033[95m\033[01mMIN HOST:\033[0m """+min_host+"""
\033[95m\033[01mMAX HOST:\033[0m """+max_host+"""
\033[95m\033[01mTOTAL NUMBER OF HOSTS:\033[0m """+str(total_host)+"""
\033[34m+--------------------------------------------------------+\033[0m """)



def simpleCalculate(cidr):
    s_cidr=cidr.split("/")

    ip=s_cidr[0]
    binary_ip=""
    s_ip=ip.split(".")
    for i in range(4):
        int_ip=int(s_ip[i])
        
        str_binary=str(decimalToBinary(int_ip))
        zeros=""
        for i in range(8-len(str_binary)):
            zeros+="0"
        binary_ip+=zeros+str_binary+"."
    binary_ip=binary_ip[:-1]

    binary_mask=""
    binary_wildcard=""
    for i in range(32):
        if(i%8==0 and i!=0):
            binary_mask+="."
            binary_wildcard+="."
        if(i<int(s_cidr[1])):
            binary_mask+="1"
            binary_wildcard+="0"
        else:
            binary_mask+="0"
            binary_wildcard+="1"

    mask=""
    s_binary_mask=binary_mask.split(".")
    for i in range(4):
        mask+=str(int(s_binary_mask[i], 2))
        if(i<3):
            mask+="."

    aux_binary_min_host=""
    change=False
    changeIndex=0
    for i in range(len(binary_ip)):
        if(binary_ip[34-i]=="0" and change==False):
            change=True
            changeIndex=34-i
            aux_binary_min_host+=binary_ip[i]
        else:
            aux_binary_min_host+=binary_ip[i]
    binary_min_host=""
    for i in range(len(aux_binary_min_host)):
        if(i==changeIndex):
            binary_min_host+="1"
        else:
            binary_min_host+=aux_binary_min_host[i]

    binary_max_host=""
    for i in range(len(binary_mask)):
        if(binary_mask[i]=="0"):
            if(i==changeIndex):
                binary_max_host+="0"
            else:
                binary_max_host+="1"
        else:
            binary_max_host+=binary_ip[i]

    min_host=""
    s_binary_min_host=binary_min_host.split(".")
    for i in range(4):
        min_host+=str(int(s_binary_min_host[i], 2))
        if(i<3):
            min_host+="."
    
    max_host=""
    s_binary_max_host=binary_max_host.split(".")
    for i in range(4):
        max_host+=str(int(s_binary_max_host[i], 2))
        if(i<3):
            max_host+="."

    zero_bits=0
    for i in range(4):
        zero_bits+=s_binary_mask[i].count("0")
    total_host=pow(2,zero_bits)-2

    return [cidr,ip,mask,min_host,max_host,total_host]



def decimalToBinary(number):
    if number<0:
        return 'Not positive'
    i = 0
    result = ''
    while number>>i:
        result = ('1' if number>>i&1 else '0') + result
        i += 1
    return result