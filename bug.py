import subprocess
import argparse
import requests

# Function to run a command-line tool and capture output
def run_tool(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        if stderr:
            print(f"Error running {command[0]}: {stderr}")
        return stdout.splitlines()
    except FileNotFoundError:
        print(f"Error: {command[0]} not found. Please ensure it is installed and in your PATH.")
        return []

# Function for subdomain discovery
def subdomain_discovery(domain):
    tools = {
        "Sublist3r": ['python3', 'Sublist3r/sublist3r.py', '-d', domain, '-o', 'sublist3r_output.txt'],
        "Amass": ['amass', 'enum', '-d', domain],
        "Subfinder": ['subfinder', '-d', domain, '-silent'],
        "Assetfinder": ['assetfinder', '--subs-only', domain]
    }
    
    all_subdomains = set()
    for tool, command in tools.items():
        print(f"Running {tool}...")
        result = run_tool(command)
        all_subdomains.update(result)
    
    return list(all_subdomains)

# Function for directory discovery
def directory_discovery(domain):
    tools = {
        "Dirsearch": ['python3', 'dirsearch/dirsearch.py', '-u', f'http://{domain}', '-e', 'php,html,txt'],
        "FFUF": ['ffuf', '-u', f'http://{domain}/FUZZ', '-w', '/path/to/wordlist.txt'],
        "Gobuster": ['gobuster', 'dir', '-u', f'http://{domain}', '-w', '/path/to/wordlist.txt'],
        "Wfuzz": ['wfuzz', '-c', '-z', 'file,/path/to/wordlist.txt', '--hc', '404', f'http://{domain}/FUZZ']
    }

    all_directories = set()
    for tool, command in tools.items():
        print(f"Running {tool}...")
        result = run_tool(command)
        all_directories.update(result)

    return list(all_directories)

# Main function
def main():
    parser = argparse.ArgumentParser(description="Bug bounty tool for subdomain and directory discovery.")
    parser.add_argument('domain', help="The target domain (e.g., example.com)")
    parser.add_argument('-o', '--output', help="Output file format (e.g., txt, csv)", default='txt')
    args = parser.parse_args()

    domain = args.domain

    # Run subdomain discovery
    subdomains = subdomain_discovery(domain)
    unique_subdomains = list(set(subdomains))

    # Check status codes
    checked_subdomains = []
    for subdomain in unique_subdomains:
        url = f"http://{subdomain}"
        try:
            response = requests.head(url, timeout=5)
            checked_subdomains.append((url, response.status_code))
            print(f"{url}: {response.status_code}")
        except requests.RequestException:
            print(f"{url}: Request failed")

    # Run directory discovery
    directories = directory_discovery(domain)

    # Save the results
    output_file = f"results.{args.output}"
    with open(output_file, 'w') as file:
        for url, status in checked_subdomains:
            file.write(f"{url}: {status}\n")
        for entry in directories:
            file.write(f"{entry}\n")

    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()
