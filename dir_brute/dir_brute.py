import os
import requests
import threading
import queue
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama for colored output

THREAD_COUNT = 10  # Number of threads for parallel requests

def check_directory(base_url, directory):
    url = f"{base_url}/{directory}"
    response = requests.get(url)
    
    status_code = response.status_code
    status_message = response.reason

    if status_code == 200:
        print(f"{Fore.GREEN}[{status_code} {status_message}] {Style.RESET_ALL}{url}")
    elif status_code == 308:
        print(f"{Fore.BLUE}[{status_code} {status_message}] {Style.RESET_ALL}{url}")
    elif status_code == 403:
        print(f"{Fore.RED}[{status_code} {status_message}] {Style.RESET_ALL}{url}")
    elif status_code == 404:
        print(f"{Fore.YELLOW}[{status_code} {status_message}] {Style.RESET_ALL}{url}")
    elif status_code == 503:
        print(f"{Fore.MAGENTA}[{status_code} {status_message}] {Style.RESET_ALL}{url}")

def process_directory(base_url, directory_queue):
    while True:
        directory = directory_queue.get()
        if directory is None:  # Exit loop when sentinel value is encountered
            break
        check_directory(base_url, directory)
        directory_queue.task_done()

def main():
    base_url = input("Enter the base URL or IP: ")
    wordlist_path = os.path.join(os.path.dirname(__file__), "common.txt")

    directory_queue = queue.Queue()

    with open(wordlist_path, "r") as wordlist_file:
        for line in wordlist_file:
            directory = line.strip()
            directory_queue.put(directory)

    # Add sentinel values to the queue to signal threads to exit
    for _ in range(THREAD_COUNT):
        directory_queue.put(None)

    threads = []
    for _ in range(THREAD_COUNT):
        t = threading.Thread(target=process_directory, args=(base_url, directory_queue))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()  # Wait for all threads to finish

if __name__ == "__main__":
    main()
