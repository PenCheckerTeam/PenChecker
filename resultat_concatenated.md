# Voici le rapport final du scan effectué par PenChecker

Dans ce rapport vous retrouverez dans l'ordre des @IP les différents résultats
Voici le rapport final du scan effectué par PenChecker, le rapport est articulé ainsi : 

 
- La machine concernée
  - Port and Services
    - Listes des différents ports/services accessibles avec numéros de versions
  - Répartition des CVEs en fonction des services
    - Représentation graphique camembert
  - Repartition des CVEs en fonction de leur score CVSS
    - Représentation graphique barre
  - CVEs
    - Listing de toutes les CVEs trouvées pour tous les ports/services


# Scan Results for IP: 192.168.50.2 (OS: Linux 4.15 - 5.8 (Accuracy: 100%))

Voici la liste des services fonctionnant sur les différents ports accessibles de la machine. **Le nombre de CVEs** par service est indiqué entre parenthèse. Si le nombre de CVE est de 0, **nous vous recommandons de vérifier**, si elle est identifiée, **que la version du service est à jour**

## Ports and Services
- <span style='color:green;'>21: ftp vsftpd (before 2.0.8) or WU-FTPD (CVE Count: 0)</span>
- <span style='color:green;'>23: telnet (CVE Count: 0)</span>
- **<span style='color:orange;'>25: smtp-proxy Python SMTP Proxy version=0.3 (CVE Count: 9)</span>**
- <span style='color:green;'>53: domain (CVE Count: 0)</span>
- **<span style='color:red;'>80: http Apache httpd version=2.2.3 (CVE Count: 31)</span>**
- <span style='color:green;'>110: pop3 (CVE Count: 0)</span>
- <span style='color:green;'>143: imap (CVE Count: 0)</span>
- <span style='color:green;'>389: ldap (CVE Count: 0)</span>
- **<span style='color:orange;'>443: http nginx version=1.12.1 (CVE Count: 1)</span>**
- <span style='color:green;'>445: microsoft-ds (CVE Count: 0)</span>
- <span style='color:green;'>1080: socks5 (CVE Count: 0)</span>
- <span style='color:green;'>1433: ms-sql-s Microsoft SQL Server (CVE Count: 0)</span>
- <span style='color:green;'>1521: oracle (CVE Count: 0)</span>
- **<span style='color:red;'>3306: mysql MySQL version=5.7.00 (CVE Count: 82)</span>**
- <span style='color:green;'>3389: ms-wbt-server (CVE Count: 0)</span>
- <span style='color:green;'>5432: postgresql (CVE Count: 0)</span>
- <span style='color:green;'>5900: vnc VNC (CVE Count: 0)</span>
- <span style='color:green;'>6667: irc (CVE Count: 0)</span>
- <span style='color:green;'>8080: http-proxy (CVE Count: 0)</span>
- <span style='color:green;'>9100: jetdirect (CVE Count: 0)</span>
- <span style='color:green;'>9200: wap-wsp (CVE Count: 0)</span>


## Répartition des CVEs en fonction des services
![pie_chart](./Rapport_Tmp\192.168.50.2\pie_chart.png)

## Repartition des CVEs en fonction de leur score CVSS
![bar_chart](./Rapport_Tmp\192.168.50.2\cve_count_by_cvss_chart.png)
## CVEs
### Port 25 : smtp-proxy Python SMTP Proxy version=0.3
<span style='color:red;'>**9.8** | CVE-2019-10160</span>

<span style='color:orange;'>**7.8** | CVE-2017-20052</span>

<span style='color:orange;'>**7.5** | CVE-2022-0391</span>

<span style='color:orange;'>**7.5** | CVE-2021-3737</span>

<span style='color:orange;'>**7.5** | CVE-2020-10735</span>

<span style='color:orange;'>**7.5** | CVE-2019-5010</span>

<span style='color:orange;'>**6.5** | CVE-2021-3733</span>

<span style='color:green;'>**5.7** | CVE-2021-3426</span>

<span style='color:green;'>**5.3** | CVE-2021-4189</span>

### Port 80 : http Apache httpd version=2.2.3
<span style='color:red;'>**9.8** | CVE-2017-7679</span>

<span style='color:red;'>**9.8** | CVE-2017-3169</span>

<span style='color:red;'>**9.8** | CVE-2017-3167</span>

<span style='color:red;'>**9.1** | CVE-2017-9788</span>

<span style='color:red;'>**8.1** | CVE-2016-5387</span>

<span style='color:orange;'>**7.8** | CVE-2011-3192</span>

<span style='color:orange;'>**7.8** | CVE-2007-6423</span>

<span style='color:orange;'>**7.5** | CVE-2017-9798</span>

<span style='color:orange;'>**7.5** | CVE-2016-8743</span>

<span style='color:orange;'>**7.5** | CVE-2009-2699</span>

<span style='color:orange;'>**7.1** | CVE-2009-1891</span>

<span style='color:orange;'>**7.1** | CVE-2009-1890</span>

<span style='color:orange;'>**6.9** | CVE-2012-0883</span>

<span style='color:orange;'>**6.8** | CVE-2014-0226</span>

<span style='color:orange;'>**6.8** | CVE-2006-4154</span>

<span style='color:orange;'>**6.5** | CVE-2017-12171</span>

<span style='color:orange;'>**6.2** | CVE-2007-1741</span>

<span style='color:orange;'>**6.1** | CVE-2016-4975</span>

<span style='color:green;'>**5.8** | CVE-2009-3555</span>

<span style='color:green;'>**5.1** | CVE-2013-1862</span>

<span style='color:green;'>**5.0** | CVE-2015-3183</span>

<span style='color:green;'>**5.0** | CVE-2014-0231</span>

<span style='color:green;'>**5.0** | CVE-2014-0098</span>

<span style='color:green;'>**5.0** | CVE-2013-6438</span>

<span style='color:green;'>**5.0** | CVE-2013-5704</span>

<span style='color:green;'>**5.0** | CVE-2010-1452</span>

<span style='color:green;'>**5.0** | CVE-2010-0408</span>

<span style='color:green;'>**5.0** | CVE-2009-3095</span>

<span style='color:green;'>**5.0** | CVE-2008-2364</span>

<span style='color:green;'>**5.0** | CVE-2007-6750</span>

<span style='color:green;'>**5.0** | CVE-2007-3847</span>

### Port 443 : http nginx version=1.12.1
<span style='color:green;'>**5.0** | PRION:CVE-2017-7529</span>

### Port 3306 : mysql MySQL version=5.7.00
<span style='color:red;'>**10.0** | PRION:CVE-2016-6662</span>

<span style='color:red;'>**10.0** | PRION:CVE-2016-0705</span>

<span style='color:red;'>**10.0** | PRION:CVE-2016-0639</span>

<span style='color:orange;'>**7.8** | PRION:CVE-2018-2696</span>

<span style='color:orange;'>**7.8** | PRION:CVE-2017-3599</span>

<span style='color:orange;'>**7.5** | PRION:CVE-2020-14760</span>

<span style='color:orange;'>**7.5** | PRION:CVE-2019-14540</span>

<span style='color:orange;'>**7.5** | PRION:CVE-2018-2647</span>

<span style='color:orange;'>**7.5** | PRION:CVE-2018-2612</span>

<span style='color:orange;'>**7.5** | PRION:CVE-2018-2562</span>

<span style='color:orange;'>**7.5** | PRION:CVE-2016-9843</span>

<span style='color:orange;'>**7.5** | PRION:CVE-2016-9841</span>

<span style='color:orange;'>**7.2** | PRION:CVE-2016-0546</span>

<span style='color:orange;'>**7.1** | PRION:CVE-2021-2011</span>

<span style='color:orange;'>**6.9** | PRION:CVE-2016-6664</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2021-2060</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2021-2014</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2021-2001</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2020-14869</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2020-14867</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2020-14812</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2020-14765</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2020-14672</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2766</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2703</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2668</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2667</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2665</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2646</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2640</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2622</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2600</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2591</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2590</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2586</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2583</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2576</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2573</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2565</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-9842</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-9840</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-5507</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-3521</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-3518</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-3495</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-3492</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-3486</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-0505</span>

<span style='color:orange;'>**6.5** | PRION:CVE-2021-2144</span>

<span style='color:orange;'>**6.3** | PRION:CVE-2021-2022</span>

<span style='color:orange;'>**6.0** | PRION:CVE-2017-3600</span>

<span style='color:green;'>**5.8** | PRION:CVE-2017-3633</span>

<span style='color:green;'>**5.5** | PRION:CVE-2022-21367</span>

<span style='color:green;'>**5.5** | PRION:CVE-2020-2760</span>

<span style='color:green;'>**5.5** | PRION:CVE-2019-2819</span>

<span style='color:green;'>**5.5** | PRION:CVE-2019-2791</span>

<span style='color:green;'>**5.5** | PRION:CVE-2019-2778</span>

<span style='color:green;'>**5.5** | PRION:CVE-2019-2758</span>

<span style='color:green;'>**5.5** | PRION:CVE-2019-2731</span>

<span style='color:green;'>**5.5** | PRION:CVE-2019-2534</span>

<span style='color:green;'>**5.5** | PRION:CVE-2018-3247</span>

<span style='color:green;'>**5.5** | PRION:CVE-2018-3187</span>

<span style='color:green;'>**5.5** | PRION:CVE-2018-3185</span>

<span style='color:green;'>**5.5** | PRION:CVE-2018-3064</span>

<span style='color:green;'>**5.5** | PRION:CVE-2018-3060</span>

<span style='color:green;'>**5.5** | PRION:CVE-2018-2812</span>

<span style='color:green;'>**5.5** | PRION:CVE-2018-2787</span>

<span style='color:green;'>**5.5** | PRION:CVE-2018-2786</span>

<span style='color:green;'>**5.5** | PRION:CVE-2017-3455</span>

<span style='color:green;'>**5.5** | PRION:CVE-2017-3454</span>

<span style='color:green;'>**5.5** | PRION:CVE-2017-10365</span>

<span style='color:green;'>**5.0** | PRION:CVE-2020-1967</span>

<span style='color:green;'>**5.0** | PRION:CVE-2019-2924</span>

<span style='color:green;'>**5.0** | PRION:CVE-2019-2923</span>

<span style='color:green;'>**5.0** | PRION:CVE-2019-2922</span>

<span style='color:green;'>**5.0** | PRION:CVE-2019-2632</span>

<span style='color:green;'>**5.0** | PRION:CVE-2017-3450</span>

<span style='color:green;'>**5.0** | PRION:CVE-2017-3329</span>

<span style='color:green;'>**5.0** | PRION:CVE-2017-3302</span>

<span style='color:green;'>**5.0** | PRION:CVE-2017-10276</span>

<span style='color:green;'>**5.0** | PRION:CVE-2017-10155</span>

<span style='color:green;'>**5.0** | PRION:CVE-2016-2105</span>



# Scan Results for IP: 192.168.50.3 (OS: Linux 4.15 - 5.8 (Accuracy: 100%))

Voici la liste des services fonctionnant sur les différents ports accessibles de la machine. **Le nombre de CVEs** par service est indiqué entre parenthèse. Si le nombre de CVE est de 0, **nous vous recommandons de vérifier**, si elle est identifiée, **que la version du service est à jour**

## Ports and Services
- **<span style='color:orange;'>22: ssh OpenSSH version=9.2p1 Debian 2+deb12u2 (CVE Count: 8)</span>**
- <span style='color:green;'>143: imap (CVE Count: 0)</span>
- **<span style='color:red;'>3306: mysql MySQL version=5.7.00 (CVE Count: 82)</span>**


## Répartition des CVEs en fonction des services
![pie_chart](./Rapport_Tmp\192.168.50.3\pie_chart.png)

## Repartition des CVEs en fonction de leur score CVSS
![bar_chart](./Rapport_Tmp\192.168.50.3\cve_count_by_cvss_chart.png)
## CVEs
### Port 22 : ssh OpenSSH version=9.2p1 Debian 2+deb12u2
<span style='color:red;'>**9.8** | CVE-2023-38408</span>

<span style='color:red;'>**9.8** | CVE-2023-28531</span>

<span style='color:orange;'>**7.5** | PRION:CVE-2023-38408</span>

<span style='color:orange;'>**7.5** | PRION:CVE-2023-28531</span>

<span style='color:orange;'>**6.5** | CVE-2023-51385</span>

<span style='color:orange;'>**6.4** | PRION:CVE-2023-51385</span>

<span style='color:green;'>**5.9** | CVE-2023-48795</span>

<span style='color:green;'>**5.5** | CVE-2023-51384</span>

### Port 3306 : mysql MySQL version=5.7.00
<span style='color:red;'>**10.0** | PRION:CVE-2016-6662</span>

<span style='color:red;'>**10.0** | PRION:CVE-2016-0705</span>

<span style='color:red;'>**10.0** | PRION:CVE-2016-0639</span>

<span style='color:orange;'>**7.8** | PRION:CVE-2018-2696</span>

<span style='color:orange;'>**7.8** | PRION:CVE-2017-3599</span>

<span style='color:orange;'>**7.5** | PRION:CVE-2020-14760</span>

<span style='color:orange;'>**7.5** | PRION:CVE-2019-14540</span>

<span style='color:orange;'>**7.5** | PRION:CVE-2018-2647</span>

<span style='color:orange;'>**7.5** | PRION:CVE-2018-2612</span>

<span style='color:orange;'>**7.5** | PRION:CVE-2018-2562</span>

<span style='color:orange;'>**7.5** | PRION:CVE-2016-9843</span>

<span style='color:orange;'>**7.5** | PRION:CVE-2016-9841</span>

<span style='color:orange;'>**7.2** | PRION:CVE-2016-0546</span>

<span style='color:orange;'>**7.1** | PRION:CVE-2021-2011</span>

<span style='color:orange;'>**6.9** | PRION:CVE-2016-6664</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2021-2060</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2021-2014</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2021-2001</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2020-14869</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2020-14867</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2020-14812</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2020-14765</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2020-14672</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2766</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2703</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2668</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2667</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2665</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2646</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2640</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2622</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2600</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2591</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2590</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2586</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2583</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2576</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2573</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2018-2565</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-9842</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-9840</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-5507</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-3521</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-3518</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-3495</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-3492</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-3486</span>

<span style='color:orange;'>**6.8** | PRION:CVE-2016-0505</span>

<span style='color:orange;'>**6.5** | PRION:CVE-2021-2144</span>

<span style='color:orange;'>**6.3** | PRION:CVE-2021-2022</span>

<span style='color:orange;'>**6.0** | PRION:CVE-2017-3600</span>

<span style='color:green;'>**5.8** | PRION:CVE-2017-3633</span>

<span style='color:green;'>**5.5** | PRION:CVE-2022-21367</span>

<span style='color:green;'>**5.5** | PRION:CVE-2020-2760</span>

<span style='color:green;'>**5.5** | PRION:CVE-2019-2819</span>

<span style='color:green;'>**5.5** | PRION:CVE-2019-2791</span>

<span style='color:green;'>**5.5** | PRION:CVE-2019-2778</span>

<span style='color:green;'>**5.5** | PRION:CVE-2019-2758</span>

<span style='color:green;'>**5.5** | PRION:CVE-2019-2731</span>

<span style='color:green;'>**5.5** | PRION:CVE-2019-2534</span>

<span style='color:green;'>**5.5** | PRION:CVE-2018-3247</span>

<span style='color:green;'>**5.5** | PRION:CVE-2018-3187</span>

<span style='color:green;'>**5.5** | PRION:CVE-2018-3185</span>

<span style='color:green;'>**5.5** | PRION:CVE-2018-3064</span>

<span style='color:green;'>**5.5** | PRION:CVE-2018-3060</span>

<span style='color:green;'>**5.5** | PRION:CVE-2018-2812</span>

<span style='color:green;'>**5.5** | PRION:CVE-2018-2787</span>

<span style='color:green;'>**5.5** | PRION:CVE-2018-2786</span>

<span style='color:green;'>**5.5** | PRION:CVE-2017-3455</span>

<span style='color:green;'>**5.5** | PRION:CVE-2017-3454</span>

<span style='color:green;'>**5.5** | PRION:CVE-2017-10365</span>

<span style='color:green;'>**5.0** | PRION:CVE-2020-1967</span>

<span style='color:green;'>**5.0** | PRION:CVE-2019-2924</span>

<span style='color:green;'>**5.0** | PRION:CVE-2019-2923</span>

<span style='color:green;'>**5.0** | PRION:CVE-2019-2922</span>

<span style='color:green;'>**5.0** | PRION:CVE-2019-2632</span>

<span style='color:green;'>**5.0** | PRION:CVE-2017-3450</span>

<span style='color:green;'>**5.0** | PRION:CVE-2017-3329</span>

<span style='color:green;'>**5.0** | PRION:CVE-2017-3302</span>

<span style='color:green;'>**5.0** | PRION:CVE-2017-10276</span>

<span style='color:green;'>**5.0** | PRION:CVE-2017-10155</span>

<span style='color:green;'>**5.0** | PRION:CVE-2016-2105</span>



