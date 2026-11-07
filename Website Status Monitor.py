
import urllib.request
import urllib.error
import time


def check_website(url):
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Python Website Monitor"}
    )

    start_time = time.time()

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            status_code = response.status
            response_time = time.time() - start_time

            return {
                "url": url,
                "status": status_code,
                "response_time": round(response_time, 2),
                "result": "Online"
            }

    except urllib.error.HTTPError as error:
        response_time = time.time() - start_time

        return {
            "url": url,
            "status": error.code,
            "response_time": round(response_time, 2),
            "result": "HTTP Error"
        }

    except urllib.error.URLError as error:
        response_time = time.time() - start_time

        return {
            "url": url,
            "status": "N/A",
            "response_time": round(response_time, 2),
            "result": "Connection Error"
        }

    except TimeoutError:
        response_time = time.time() - start_time

        return {
            "url": url,
            "status": "N/A",
            "response_time": round(response_time, 2),
            "result": "Timeout"
        }


def display_results(results):
    print("\nWebsite Monitoring Report")
    print("=" * 65)

    for result in results:
        print(f"Website: {result['url']}")
        print(f"Result: {result['result']}")
        print(f"HTTP Status: {result['status']}")
        print(f"Response Time: {result['response_time']} seconds")
        print("-" * 65)

    online_count = sum(
        1 for result in results
        if result["result"] == "Online"
    )

    print(f"\nTotal Websites: {len(results)}")
    print(f"Online Websites: {online_count}")
    print(f"Other Results: {len(results) - online_count}")


def main():
    print("Website Status Monitor")
    print("-" * 30)

    websites_input = input(
        "Enter website URLs separated by commas:\n"
    )

    websites = [
        url.strip()
        for url in websites_input.split(",")
        if url.strip()
    ]

    if not websites:
        print("No website URLs were entered.")
        return

    results = []

    for url in websites:
        if not url.startswith(("http://", "https://")):
            print(f"\nInvalid URL format: {url}")
            continue

        print(f"\nChecking {url} ...")

        result = check_website(url)
        results.append(result)

    if results:
        display_results(results)
    else:
        print("\nNo valid websites to check.")


if __name__ == "__main__":
    main()
