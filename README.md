# PenChecker

## Description

PenChecker is a student project carried out as part of our Master 1 year at Oteria Cyber School.
We wanted to create a tool based on a plug-and-play physical module that would enable any type of population to scan their local network and identify vulnerabilities.

## Features

The features currently available on the software are :
* Scanning and versioning of accessible machines
* Links service versions to known vulnerabilities
* Clear and simple report, with known remediation to be implemented, in markdown and pdf versions

## Getting Ready

### Setting up :

You need to install some dependencies first :
- chmod +x install.sh
- sudo ./install.sh
- Everything you need will be install, with the .venv ready to use with python dependecies installed with pip
- source .venv/bin/activate

Then you can just run the main.py program.  
You can indicate the network interface from which you want to run the script by doing: `python Main.py --interface interface_name`.  
Or else, by doing: `python Main.py` the default interface will be "eth0"  
Note that for a full nmap scan you need to run the programm with elevated privileges (with sudo or run as root)

## How to push

```sh
git add .
git commit -m "add feature"
git push origin main
git tag vX.X
git push origin vX.X
```

## Contact

To report problems during installation, or bugs with the tool, you can contact us at:
- alexandre.tornier@oteria.fr
- matias.dandois@oteria.fr
- benjamin.di-paola@oteria.fr

## Special thanks

* Paul de Montalivet, Head of Training and Projects at Oteria Cyber School, for his guidance throughout the year.

* Laurent Ladreyt, IT Manager/Cybersecurity Referent at KROHNE France, who helped us come up with ideas for the development, accompanied us on the project and tested the solution on a perimeter of his company.

* To all the people who contacted us via LinkedIn to advise us and give their opinion on the features we had planned for our solution.

## Disclaimer

This project is intended solely for educational and defensive purposes. The creators and contributors are not responsible for any misuse or malicious use of this tool. Use it responsibly and ethically, adhering to all relevant laws and regulations.
