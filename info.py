
# select ip.cidr,count(ip.ip),cidr.country_code from ip inner join cidr on cidr.cidr=ip.cidr group by cidr.cidr;

