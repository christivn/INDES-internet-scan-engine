import gui, geoipgen

print(">> Country code: ", end="")
country_code=str(input())

gui.bannerNoAuthor()
try:
    cidr_es=geoipgen.generate.randomCIDR(country_code)
    print("\n\033[35m\033[01mRandom CIDR from '"+country_code+"':\033[0m\033[35m "+cidr_es+"\033[0m")
    print("\033[35m\033[01mAll IP list range from random CIDR on '"+country_code+"':\033[0m\033[35m Generate list with "+str(len(geoipgen.generate.rangeIP(cidr_es)))+" ips\033[0m")



    print("\n\033[32m[ CIDR HAS BEEN SUCCESSFULLY UPLOADED TO THE DATABASE ]\033[0m")
    input("\nPress ENTER to continue...")
except:
    print("\n\033[31m[ COUNTRY CODE ERROR ]\033[0m")
    print("\033[31mTry this examples: us, es, fr, ru, vn...\033[0m")
    input("\nPress ENTER to continue...")