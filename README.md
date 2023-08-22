# dir_brute
dir_brute is a Python script for parallel directory enumeration on web servers. It uses a wordlist of common directory names to check the existence of directories on a given server. The script makes HTTP requests in parallel using multiple threads and provides colorful output based on the HTTP response status.

# Usage
1. Clone the repository:
git clone https://github.com/uddeshvaidya/dir_brute.git
2. Change the Directory
cd dir_brute
3. Install the required Python packages:
pip install requests colorama
4. Run the script:
python dir_brute.py -u <base_url> -w <wordlist_path>

# Example:
python dir_brute.py -u https://example.com -w custom_wordlist.txt
Flags:
  -u, --url    Base URL of the target website (e.g., https://example.com)
  -w, --wordlist    Path to a custom wordlist file (default: common.txt)
  -h, --help    Show help message and exit

# Features
Parallel directory enumeration using multiple threads. Colored output for different HTTP response statuses. Redirect handling and URL validation.

# Contributing
Contributions are welcome! If you find any issues or have ideas for improvements, please feel free to open an issue or submit a pull request.

# License
This project is licensed under the GNU General Public License (GNU GPL). See LICENSE for details.

# Disclaimer: This script is intended for educational and ethical purposes. Only use it on systems you have permission to test. Unauthorized use is not encouraged.
