# PenChecker
![logo](./logo.png)
## Description

PenChecker is a student project carried out as part of our Master 1 year at Oteria Cyber School.
We wanted to create a tool based on a plug-and-play physical module that would enable any type of population to scan their local network and identify vulnerabilities.

## Features

The features currently available on the software are :
* Scanning and versioning of accessible machines
* Links service versions to known vulnerabilities
* Clear and simple report

## Getting Ready

### Installation :
- `chmod +x install.sh`
- `./install.sh`, which will install everything needed, with the python dependencies with pip in .venv

:warning: You have to start .venv in an elevated account (or root) to let nmap perform everything needed.  
Then you can just run the Main.py program.  
`python Main.py --interface Interface_name` let you choose the network interface (without it's eth0 by default)

## How to push

push.sh is there to help you commit corrections or modifications you want to propose

## Special thanks

* Paul de Montalivet, Head of Training and Projects at Oteria Cyber School, for his guidance throughout the year.

* Laurent Ladreyt, IT Manager/Cybersecurity Referent at KROHNE France, who helped us come up with ideas for the development, accompanied us on the project and tested the solution on a perimeter of his company.

* To all the people who contacted us via LinkedIn to advise us and give their opinion on the features we had planned for our solution.

## Disclaimer

This project is intended solely for educational and defensive purposes. The creators and contributors are not responsible for any misuse or malicious use of this tool. Use it responsibly and ethically, adhering to all relevant laws and regulations.
