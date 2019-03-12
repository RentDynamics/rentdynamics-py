## Installation

```
pip install rentdynamics
```

## Usage
```python
from rentdynamics.client import Client

api_key = 'some api key'
api_secret = 'some api secret'
endpoint = '/some/endpoint'
payload = {
    'arg1': 'val1',
    'arg2': 2
}

client = Client(api_key=api_key, api_secret=api_secret, development=False)

resp = client.post(endpoint, payload)
print(resp.json())
```

## Options
When creating a new client you can pass along ```development=True``` which will send all requests to Rent Dynamics development environment.