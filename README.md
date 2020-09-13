# INDES
<h2>🌐 IPV4 Internet Connected Devices Scan Engine<br></h2>

<p><b>INDES</b> is able to analyze all the open ports of a device connected to the internet, and register the services it offers, the OS it uses, or Headers.
The data is saved in a <b>mysql database designed</b> to visualize the data from there, and have a greater ease of implementation in other tools.</p>
      
<table>
  <tr>
    <td><h2>Mode: CLI</h2>
The CLI mode allows you to use the basic options from any terminal on any operating system (Linux, Windows, Mac).
It is the best option, since it can run several processes at the same time on different terminal screens.</td>
    <td width="50%"><img align="right" src="https://i.ibb.co/v1zzPNh/image.png"></td>     
  </tr> 
</table>

## 📢 How does it work
The search engine uses the library [subnet-calculator-cidr](https://github.com/christivn/subnet-calculator-cidr) and [geoipgen](https://github.com/christivn/geoipgen) to generate IP ranges according to country, for targeted attacks. Then it goes through the whole range getting the data through [NMAP](https://github.com/nmap/nmap) and saves the data in a DB with MYSQL.

## 📑 Next updates
\- Getting OS<br>
\- Getting HTTP Header<br>
\- Web Dashboard<br>
\- Dork search<br>
\- CMS detect


| ❌ DISCLAIMER ❌<br> This open source is for educational and security purposes only, the author is not responsible for inappropriate use of the tool. The responsibility will fall on the user of the code. |
| --- |
