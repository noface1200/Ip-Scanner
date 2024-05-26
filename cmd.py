import subprocess, random, colorama
from requests import post

done = []

file_object = open('valid.txt', 'w', buffering=1)

colorama.init(autoreset=True)

def generate_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

while True:
    ipv_gen = generate_ip()
    request = subprocess.Popen(['ping', '-n', '1', ipv_gen], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    out, err = request.communicate()
    
    if 'Lost = 0' in out.decode():
        if ipv_gen not in done:
            print(f'{colorama.Fore.GREEN}[Access Granted] {colorama.Fore.RESET}{ipv_gen}')
            file_object.write(f'valid ip: {ipv_gen}\n')
            file_object.flush()
            done.append(ipv_gen)
    else:
        print(f'{colorama.Fore.RED}[Access Denied] {colorama.Fore.RESET}{ipv_gen}')