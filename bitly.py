import bitly_api

import sys

# API information

API_USER = 'o_3g4b3j4neo'
API_KEY = 'R_ed96d7e6f21643bba6eb6d073165600a'

b = bitly_api.Connection(API_USER, API_KEY)


# Replace this with your Long URL Here
longurl = input('enter you long url : \n')
response = b.shorten(uri = longurl)

# Now let us print the Bitly URL
print(response['url'])

