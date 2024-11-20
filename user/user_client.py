import requests
import sys

 
def create_user():
    url = 'http://localhost:8000/user/create_list'

    # Open the file and ensure it remains open during the request
    with open('./learning.py', 'rb') as file:
        files = {'user_cv': file}
        data = {
            'username': 'gwadaigi',
            'email': 'gigiwd@gmail.com',
        }

        # Make the request inside the with block
        res = requests.get(url=url, data=data, files=files)

    print(res.status_code)
    print(res.text)


if __name__ == '__main__':
    if sys.argv[1] == 'create_list':
        create_user()
