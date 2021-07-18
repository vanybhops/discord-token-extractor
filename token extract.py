import requests
import ast
url="https://discord.com/api/v9/auth/login"
email=input("write your email: ")
password=input("write your password: ")
data={
    'login':f"{email}",
    'password':f"{password}",
}
r=requests.post(url,json=data)
r2=ast.literal_eval(r.text)
try:
    print(r2['token'])
except Exception as e:
    print("wrong email or password")
