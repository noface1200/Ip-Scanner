# IP Scanner

## UPDATE 2 | 23rd November
- Added Ip Sweeping
- Removed Colorama And Replaced It With Ansi escape codes
- Removed Requests Lib

## Main

A Python-based IP scanner that randomly generates IP addresses and checks if there valid by sending a ping request. Valid IPs (those that respond) are logged in a file (`valid.txt`). Invalid IPs are displayed as denied in the console.

## Features

- Generates random IP addresses.
- Pings each IP address to check for validity.
- Logs valid IP addresses in `valid.txt`.
- Uses the `requests` library for HTTP requests.

## Requirements
None All Dependincies Come With Cpython

## Run The Script
Run the script:
```shell
python ip_scanner.py
```
