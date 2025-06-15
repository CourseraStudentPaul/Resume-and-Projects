import requests

def main():
    url = input("Enter the URL to analyze (e.g., https://example.com): ")
    try:
        response = requests.get(url)
        print("\nResponse Headers:\n")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")

if __name__ == "__main__":
    main()
