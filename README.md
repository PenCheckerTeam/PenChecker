# PenChecker

## Description

PenChecker is a student project carried out as part of our Master 1 year at Oteria Cyber School.
We wanted to create a tool based on a plug-and-play physical module that would enable any type of population to scan their local network and identify vulnerabilities.

## Features

The features currently available on the software are :
* Scanning and versioning of accessible machines
* Links service versions to known vulnerabilities
* Clear and simple report, with known remediation to be implemented

## Getting Ready

### For a Kali RaspeberryPI version :

You need to install some dependencies first :  
- chmod +x install.sh
- ./install.sh
- Then do the same than the next point

### For a basic Kali version :  
- Install virtualvenv for python and then : python -m venv name_of_your_venv
- source name_of_your_venv/bin/activate
- pip install -r requirements.txt

Then you can just run the main.py program.

## How to push

```sh
git add .
git commit -m "add feature"
git push origin main
git tag vX.X
git push origin vX.X
```

## Special thanks

* Paul de Montalivet, Head of Training and Projects at Oteria Cyber School, for his guidance throughout the year.

* Laurent Ladreyt, IT Manager/Cybersecurity Referent at KROHNE France, who helped us come up with ideas for the development, accompanied us on the project and tested the solution on a perimeter of his company.

* To all the people who contacted us via LinkedIn to advise us and give their opinion on the features we had planned for our solution.

## Disclaimer

This project is intended solely for educational and defensive purposes. The creators and contributors are not responsible for any misuse or malicious use of this tool. Use it responsibly and ethically, adhering to all relevant laws and regulations.
