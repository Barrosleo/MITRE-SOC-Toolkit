import requests

def fetch_threat_data():
    """
    Fetch threat data from a public API.
    (For demonstration purposes, this function returns dummy data.)

    In a real-world scenario, uncomment and update the request call below:
    response = requests.get("https://api.threatintel.com/v1/indicators")
    data = response.json()
    """
    # Dummy data for demonstration
    data = [
        {"indicator": "1.2.3.4", "technique": "T1566 - Phishing"},
        {"indicator": "bad-domain.com", "technique": "T1071 - Application Layer Protocol"},
        {"indicator": "abcd1234efgh5678", "technique": "T1059 - Command-Line Interface"}
    ]
    return data

if __name__ == '__main__':
    data = fetch_threat_data()
    for entry in data:
        print(f"Indicator: {entry['indicator']} mapped to MITRE Technique: {entry['technique']}")
