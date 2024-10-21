# AAS Interaction Script

## Overview
This script interacts with an Asset Administration Shell (AAS) to fetch its structure, update variable values, and generate random values at specified intervals. It is designed to be modular and reusable across different AAS setups.

## Requirements
- Python 3.x
- `requests` library (install via `pip install requests`)

## Script Structure
1. **Functions**
   - `fetch_aas_structure(aas_url)`: Fetches the structure of a specified AAS element.
   - `update_variable(aas_update_url, id_short, new_value)`: Updates the specified AAS variable with a new value.
   - `get_random_value()`: Fetches a random number from a designated API.
   - `generate_and_publish_values(variable_urls, iterations=5, interval=5)`: Generates and publishes random values for specified AAS variables at regular intervals.

2. **Main Execution**
   - Base AAS URL and variable mappings are defined.
   - Fetches the structure of the specified variables.
   - Generates and publishes random values to the AAS.

## Usage
1. **Setup**
   - Change the `base_aas_url` and `variable_urls` in the `config.py` file to point to your specific AAS instance.
   - Ensure the AAS server is running and accessible at the defined URLs.

2. **Execution**
   - Run the script using Python: `python aas_interaction.py`.

## Example Configuration
### `config.py`
```python
BASE_AAS_URL = 'http://localhost:8000/submodels/aHR0cHM6Ly9hZG1pbi1zaGVsbC5pby9pZHRhL1N1Ym1vZGVsVGVtcGxhdGUvVGltZVNlcmllcy8xLzE/submodel-elements/'

VARIABLE_URLS = {
    "Time": f"{BASE_AAS_URL}Time",
    "sampleAccelerationX": f"{BASE_AAS_URL}Metadata.Record.sampleAccelerationX",
    "sampleAccelerationY": f"{BASE_AAS_URL}Metadata.Record.sampleAccelerationY",
    "sampleAccelerationZ": f"{BASE_AAS_URL}Metadata.Record.sampleAccelerationZ",
    "SamplingRate": f"{BASE_AAS_URL}Segments.LinkedSegment.SamplingRate"
}
