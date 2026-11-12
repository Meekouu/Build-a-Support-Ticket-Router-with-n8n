import json
import requests

WEBHOOK_URL = "http://localhost:5678/webhook-test/63787399-1fbe-4ca5-afb4-83f56c8c7ec0"

payload = {
    "ticket_id": "TICK-1001",
    "customer_tier": "premium",
    "customer_name": "Mico Agtay",
    "message": "The system crashed when I tried to export my report!",
    "severity": 3,
    "priority_hint": "high"
}

try:
    print("Sending test payload to n8n...")
    # Using the 'requests' library properly
    response = requests.post(WEBHOOK_URL, json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response from n8n: {response.text}")
except Exception as e:
    print(f"Error sending request: {e}")