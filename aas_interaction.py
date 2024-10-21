import requests
from datetime import datetime
import time
from config import VARIABLE_URLS

def fetch_aas_structure(aas_url):
    """Fetch the AAS structure from the given URL."""
    try:
        response = requests.get(aas_url)

        if response.status_code == 200:
            print("AAS Structure:")
            aas_structure = response.json()
            print(aas_structure)
            return aas_structure  # Return the fetched AAS structure
        else:
            print("Failed to fetch AAS structure:")
            print("Status Code:", response.status_code)
            print("Response Text:", response.text)
            return None

    except requests.ConnectionError as e:
        print("Error connecting to the AAS server:", e)
        return None

def update_variable(aas_update_url, id_short, new_value):
    """Update the specified variable with the new value."""
    # Build the payload to match the expected structure
    payload = {
        "category": "VARIABLE",
        "idShort": id_short,
        "semanticId": {
            "type": "ExternalReference",
            "keys": [
                {
                    "type": "GlobalReference",
                    "value": f"https://sample.com/{id_short}/1/1"  # Modify as needed for each variable
                }
            ]
        },
        "qualifiers": [
            {
                "type": "Cardinality",
                "valueType": "xs:string",
                "value": "ZeroToOne"
            }
        ],
        "valueType": "xs:long",
        "value": str(new_value),  # Convert new_value to string
        "modelType": "Property"  # Add model type
    }

    print(f"Sending payload to AAS to update {id_short}:", payload)

    try:
        response = requests.put(aas_update_url, json=payload)

        if response.status_code in [200, 204]:
            print("Successfully updated AAS.")
        else:
            print("Error updating AAS:", response.status_code)
            print("Response Text:", response.text)

    except requests.ConnectionError as e:
        print("Error connecting to the AAS server:", e)

def get_random_value():
    """Fetch a random number from the API."""
    try:
        response = requests.get("https://www.randomnumberapi.com/api/v1.0/random?min=0&max=10&count=1")
        if response.status_code == 200:
            return response.json()[0]  # Return the first random number
        else:
            print("Failed to fetch random value:")
            print("Status Code:", response.status_code)
            print("Response Text:", response.text)
            return None
    except requests.ConnectionError as e:
        print("Error connecting to the random number API:", e)
        return None

def generate_and_publish_values(variable_urls, iterations=5, interval=5):
    """Generate random values and publish them at specified intervals."""
    for _ in range(iterations):
        new_values = {
            "Time": datetime.utcnow().isoformat() + 'Z',  # Current UTC timestamp in ISO format
            "sampleAccelerationX": get_random_value(),
            "sampleAccelerationY": get_random_value(),
            "sampleAccelerationZ": get_random_value(),
            "SamplingRate": get_random_value()  # New value for SamplingRate
        }

        for id_short, new_value in new_values.items():
            if new_value is not None:  # Ensure the new value is valid
                update_variable(variable_urls[id_short], id_short, new_value)

        time.sleep(interval)  # Wait for the specified interval before the next iteration

if __name__ == "__main__":
    # Fetch and print the structure for each variable
    for id_short, aas_url in VARIABLE_URLS.items():
        fetch_aas_structure(aas_url)

    # Generate and publish values every 5 seconds for 5 times
    generate_and_publish_values(VARIABLE_URLS, 5, 5)
