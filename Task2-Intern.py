import csv
import requests
from concurrent.futures import ThreadPoolExecutor

def get_status_code(url, timeout=10):
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        if response.status_code == 405:
            response = requests.get(url, timeout=timeout, allow_redirects=True)
        return response.status_code
    except requests.exceptions.ConnectionError:
        return "ERROR: Connection error"
    except requests.exceptions.Timeout:
        return "ERROR: Timeout"
    except requests.exceptions.TooManyRedirects:
        return "ERROR: Too many redirects"
    except requests.exceptions.RequestException as e:
        return f"ERROR: {e}"

def check_and_print(url):
    status = get_status_code(url)
    print(f"({status}) {url}")

def main():
    with open("Task 2 - Intern.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        urls = [list(row.values())[0].strip() for row in reader if list(row.values())[0].strip()]

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(check_and_print, urls)

if __name__ == "__main__":
    main()