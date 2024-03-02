import sys
import requests


def upload_file(path: str):
    with open(path, 'rb') as f:
        files = {'file': f}
        requests.post('http://localhost:8888/', files=files)


def print_list():
    params = {
        'command': 'list'
    }
    r = requests.get('http://localhost:8888/', params=params)
    answer = r.content.strip().decode().lstrip('[').rstrip(']').split(',')
    for val in answer:
        print(val.strip('"'))


def main(args: list):
    if args[1] == 'upload' and len(args) == 3:
        path: str = args[2]
        upload_file(path)
    elif args[1] == 'list':
        print_list()
    else:
        print('Invalid parameter')


if __name__ == '__main__':
    number_args = len(sys.argv)
    if number_args < 2 or number_args > 3:
        print('Invalid number of parameters')
    else:
        main(sys.argv)
