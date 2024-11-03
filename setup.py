import os
import subprocess

def install_packages():
    # Install Python packages
    subprocess.run(['pip', 'install', 'requests', 'argparse'], check=True)

    # Install Sublist3r
    print("Installing Sublist3r...")
    subprocess.run(['git', 'clone', 'https://github.com/aboul3la/Sublist3r.git'], check=True)
    os.chdir('Sublist3r')
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)
    os.chdir('..')

    # Install Amass
    print("Installing Amass...")
    subprocess.run(['sudo', 'apt', 'install', '-y', 'amass'], check=True)

    # Install Findomain
    print("Installing Findomain...")
    subprocess.run([
        'wget', 'https://github.com/findomain/findomain/releases/download/latest/findomain-linux'
    ], check=True)
    subprocess.run(['chmod', '+x', 'findomain-linux'], check=True)
    subprocess.run(['sudo', 'mv', 'findomain-linux', '/usr/local/bin/findomain'], check=True)

    # Install Subfinder
    print("Installing Subfinder...")
    subprocess.run(['go', 'install', 'github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest'], check=True)

    # Install Assetfinder
    print("Installing Assetfinder...")
    subprocess.run(['go', 'install', 'github.com/tomnomnom/assetfinder@latest'], check=True)

    # Install Dirsearch
    print("Installing Dirsearch...")
    subprocess.run(['git', 'clone', 'https://github.com/maurosoria/dirsearch.git'], check=True)

    # Install FFUF
    print("Installing FFUF...")
    subprocess.run(['go', 'install', 'github.com/ffuf/ffuf@latest'], check=True)

    # Install Gobuster
    print("Installing Gobuster...")
    subprocess.run(['go', 'install', 'github.com/OJ/gobuster/v3@latest'], check=True)

    # Install Wfuzz
    print("Installing Wfuzz...")
    subprocess.run(['pip', 'install', 'wfuzz'], check=True)

    # Install Feroxbuster
    print("Installing Feroxbuster...")
    subprocess.run(['cargo', 'install', 'feroxbuster'], check=True)

    print("All tools installed successfully!")

if __name__ == "__main__":
    install_packages()
