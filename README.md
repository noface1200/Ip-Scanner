# IP Scanner

A Python-based IP scanner that randomly generates IP addresses and checks if there valid by sending a ping request. Valid IPs (those that respond) are logged in a file (`valid.txt`). Invalid IPs are displayed as denied in the console.

## Features

- Generates random IP addresses.
- Pings each IP address to check for validity.
- Logs valid IP addresses in `valid.txt`.
- Uses the `requests` library for HTTP requests.

## Requirements
```shell
pip install -r requirements.txt
```

Run the IP scanner script:
```shell
python ip_scanner.py
```
