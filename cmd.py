import subprocess, random, urllib.parse, http.client
import sys

done = []

file_object = open('valid.txt', 'w', buffering=1)

GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

def generate_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

def ping_ip(ip):
    request = subprocess.Popen(['ping', '-n', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = request.communicate()
    return 'Lost = 0' in out.decode()

def sweep_ip(ip):
    base_ip = '.'.join(ip.split('.')[:3]) + '.'
    print(f'{GREEN}[Sweeping] {RESET}{ip}')
    for i in range(1, 255):
        test_ip = base_ip + str(i)
        if ping_ip(test_ip):
            print(f'{GREEN}[Access Granted] {RESET}{test_ip}')
            file_object.write(f'valid ip: {test_ip}\n')
            file_object.flush()

while True:
    ipv_gen = generate_ip()
    if ping_ip(ipv_gen):
        if ipv_gen not in done:
            print(f'{GREEN}[Access Granted] {RESET}{ipv_gen}')
            file_object.write(f'valid ip: {ipv_gen}\n')
            file_object.flush()
            done.append(ipv_gen)
            sweep_ip(ipv_gen)
    else:
        print(f'{RED}[Access Denied] {RESET}{ipv_gen}')
