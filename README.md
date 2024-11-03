# BugBee_helper

Bug Bounty Automation Tool

Overview
This project is a Python command-line tool designed for subdomain and directory discovery during bug bounty hunting. It integrates popular open-source tools for comprehensive scans and outputs the results in a user-specified format. The primary aim is to streamline reconnaissance and make it more efficient for security researchers.

Features
- Subdomain Discovery: Utilizes Sublist3r, Amass, Subfinder, and Assetfinder.
- Directory Discovery: Integrates Dirsearch, FFUF, Gobuster, and Wfuzz.
- Status Code Check: Checks the HTTP status code of discovered subdomains.
- Output Format: Saves the results in user-specified file formats (e.g., txt, csv).
- Easy Setup: Includes a setup.py script for installing dependencies and required tools.

Requirements
- Python 3.x
- pip for Python package installation
- Internet connection for downloading tools
- Necessary permissions to install and run third-party tools

Installation
1. Clone the repository:
   git clone https://github.com/jagadeep05/BugBee_helper

2. Run the setup.py script to install all dependencies and third-party tools:
   sudo python3 setup.py

3. Verify that all tools are correctly installed:
   Ensure Sublist3r, Amass, Subfinder, Assetfinder, Dirsearch, FFUF, Gobuster, and Wfuzz are present in your PATH.

Usage
To run the tool:
python3 bug.py example.com -o txt
Replace example.com with your target domain. The -o flag specifies the output format.

Command-line Arguments
- domain: The target domain (e.g., example.com)
- -o, --output: Specifies the output file format (default is txt)

Example Output
The tool outputs subdomains and directories along with their HTTP status codes in the specified format.

Disclaimer
This tool is for educational and ethical use only.
- Ensure that you have explicit permission from the website owner before running any tests.
- Misuse of this tool for illegal activities is strictly prohibited.
- The authors and contributors are not responsible for any damage or legal consequences resulting from the use of this tool.

Add-ons and Future Enhancements
- Integration with more tools such as Aquatone for screenshots.
- Adding a feature for multi-threaded scanning to improve efficiency.
- Custom wordlist support for directory brute-forcing.
- Option to run only subdomain or directory scans based on user input.

Contribution
Contributions to improve the project are welcome. Feel free to open issues and submit pull requests.

License
This project is licensed under the MIT License. See LICENSE for more details.
