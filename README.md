# INDES
IPV4 Internet Connected Devices Scan Engine

# [ IN PROCESS ]

## How does it work
The search engine uses the library [subnet-calculator-cidr](https://github.com/christivn/subnet-calculator-cidr) to generate IP ranges according to country, for targeted attacks. Then it goes through the whole range getting the data through [NMAP](https://github.com/nmap/nmap) and saves the data in a DB with MYSQL, and can use the TOR network u other Proxy to remain anonymous.

## Requirements
<p>> Python 3<br>
> Nmap<br>
> Tor<br>
> Mysql database (can be used remote db)</p>

### Disclaimer
This open code is for educational and safety purposes only, the author is not responsible for improper use of the tool.
