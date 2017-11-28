import json

import jwt

payload = {"x": 3}
encoded_jwt = jwt.encode(payload, 'secret', algorithm='HS256')
print(encoded_jwt)
decoded_jwt = jwt.decode(encoded_jwt.decode(), 'secret', algorithms='HS256')
print(decoded_jwt)
