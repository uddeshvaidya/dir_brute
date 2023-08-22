# dir_brute
dir_brute is a Python script for parallel directory enumeration on web servers. It uses a wordlist of common directory names to check the existence of directories on a given server. The script makes HTTP requests in parallel using multiple threads and provides colorful output based on the HTTP response status.

# Usage
Clone the repository: <br>
git clone https://github.com/uddeshvaidya/dir_brute.git <br> <br>
Change the Directory <br>
cd dir_brute <br> <br>
Install the required Python packages: <br>
pip install requests colorama <br> <br>
Run the script: <br>
python3 dir_brute.py -u <base_url> -sw -ew -bw <br> <br>
Flags: <br>
  -u, --url    Base URL of the target website (e.g., https://example.com) <br>
  -sw          Use small.txt wordlist <br>
  -ew          Use extensions.txt wordlist <br>
  -bw          Use big.txt wordlist <br>
  -h, --help   Show help message and exit <br>

# Wordlists:
The wordlists (small.txt, extensions.txt, big.txt, common.txt) should be placed in the 'wordlist' folder next to the 'dir_brute.py' script.

# Features
Parallel directory enumeration using multiple threads. Colored output for different HTTP response statuses. Redirect handling and URL validation.

# Contributing
Contributions are welcome! If you find any issues or have ideas for improvements, please feel free to open an issue or submit a pull request.

# License
This project is licensed under the GNU General Public License (GNU GPL). See LICENSE for details.

# Disclaimer: 
This script is intended for educational and ethical purposes. Only use it on systems you have permission to test. Unauthorized use is not encouraged.
