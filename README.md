# INDES
IPV4 Internet Connected Devices Scan Engine.<br>
The data is saved in a **mysql database designed** to visualize the data from there, and have a greater ease of implementation in other tools.

![Internet Connected Devices Scan Engine](https://i.ibb.co/WBQp8hT/indes.png)

## How does it work
The search engine uses the library [subnet-calculator-cidr](https://github.com/christivn/subnet-calculator-cidr) and [geoipgen](https://github.com/christivn/geoipgen) to generate IP ranges according to country, for targeted attacks. Then it goes through the whole range getting the data through [NMAP](https://github.com/nmap/nmap) and saves the data in a DB with MYSQL, can use the TOR network u other Proxy to remain anonymous.

## Requirements
<p>> Python 3<br>
> Nmap<br>
> Tor / Proxy (Optional)<br>
> Mysql</p>

## Next updates
\- Getting OS<br>
\- Getting HTTP Header

### Disclaimer
This open code is for educational and safety purposes only, the author is not responsible for improper use of the tool.
