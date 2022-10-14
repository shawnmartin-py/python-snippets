from hashlib import sha1
from sys import argv, exit

from requests import get, Response


def request_api_data(query_char: str) -> Response:
    res = get('https://api.pwnedpasswords.com/range/' + query_char)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again'
        )
    return res


def get_password_leaks_count(hashes: Response, hash_to_check: str) -> int:
    hashes = (line.split(':') for line in hashes.text.splitlines())
    return next((count for h, count in hashes if h == hash_to_check), 0)


def pwned_api_check(password: str):
    sha1_password = sha1(password.encode()).hexdigest().upper()
    first5_char, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        if count := pwned_api_check(password):
            print(
                f'{password} was found {count} times... you should probally '
                'change your password!'
            )
        else:
            print(f'{password} was NOT found. Carry on!')
        return 'done!'


if __name__ == '__main__':
    exit(main(argv[1:] or ['hello']))

