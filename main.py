import requests, argparse

version = 1.0
author = 'badaboum#6183'

print(f'\n\t\tbr00k {version} by {author}\n\n')

parser = argparse.ArgumentParser(usage='%(prog)s [options]')
parser.add_argument('-t', '--target', help='webhook URL', dest='url', metavar='')
parser.add_argument('-s', '--spam', help='spam with a message (will be asked later)', dest='spam', action='store_true')
parser.add_argument('-d', '--delete', help='delete webhook', dest='delete', action='store_true')
parser.add_argument('-i', '--infos', help='webhook informations', dest='infos', action='store_true')

args = parser.parse_args()

if not args.url:
    parser.print_help()
    exit()

if not args.spam and not args.delete and not args.infos:
    parser.print_help()
    exit()

r = requests.get(args.url)
if r.status_code == 401:
    print('[-] invalid webhook')
    exit()

if args.infos:
    r = requests.get(args.url)
    if r.status_code == 200:
        json_data = r.json()
        for key, value in json_data.items():
            if value != None:
                print(f'[+] {key}: {value}')
    else:
        print('[-] failed')

    exit()

if args.delete:
    requests.delete(args.url)
    r = requests.get(args.url)
    if r.status_code == 200:
        print('[-] failed')
    else:
        print('[+] done')
    exit() 

if args.spam:
    message = input('message to spam> ')

    data = {
        'content': message,
        'username': 'br00k is here lol'
    }
    while 1:
        r = requests.post(args.url, data=data)
        if r.status_code == 204:
            print('[+] sent')
        else:
            print('[-] failed')
    exit()

