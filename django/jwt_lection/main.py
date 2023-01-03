import time
from jwt_handler import encodeJWT, decodeJWT, refreshJWT


user = {"username":"nastya","id":1}

# получаем токены
jwt_token = encodeJWT(user)
print(jwt_token)

# проходит время
time.sleep(6)
decoded = decodeJWT(jwt_token['access'])
print(decoded) # токен просрочился

new_jwt = refreshJWT(jwt_token['refresh'])
print(new_jwt) # получили новые токены
