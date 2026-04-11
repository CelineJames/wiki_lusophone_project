import csv
import requests

def get_status_code(url, timeout=10):
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        # fall back to GET
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

def main():
    with open("Task 2 - Intern.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Get first column value regardless of exact key name
            url = list(row.values())[0].strip()
            if url:
                status = get_status_code(url)
                print(f"({status}) {url}")

if __name__ == "__main__":
    main()