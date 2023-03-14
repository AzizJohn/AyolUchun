import requests

url = "http://notify.eskiz.uz/api/auth/login"

payload = {
    'email': 'test@eskiz.uz',
    'password': 'j6DWtQjjpLDNjWEk74Sx'
}

files = [
]

headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

#####################################################
#####################################################
#####################################################
#####################################################

url = "https://notify.eskiz.uz/api/message/sms/send"

payload = {
    'mobile_phone': '998990376004',
    'message': 'Eskiz Test',
    'from': '4546',
    'callback_url': 'http://0000.uz/test.php'
}

files = [
]
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjUsInJvbGUiOiJ1c2VyIiwiZGF0YSI6eyJpZCI6NSwibmFtZSI6Ilx1MDQyN1x1MDQxZiBCZXN0IEludGVybmV0IFNvbHV0aW9uIiwiZW1haWwiOiJ0ZXN0QGVza2l6LnV6Iiwicm9sZSI6InVzZXIiLCJhcGlfdG9rZW4iOiJleUowZVhBaU9pSktWMVFpTENKaGJHY2lPaUpJVXpJMU5pSjkuZXlKemRXSWlPalVzSW5KdmJHVWlPaUoxYzJWeUlpd2laR0YwWVNJNmV5SnBaQ0k2TlN3aWJtRnRaU0k2SWx4MU1EUXlOMXgxTURReFppQkNaWE4wSUVsdWRHVnlibVYwSUZOdmJIVjBhVzl1SWl3aVpXMWhhV3dpT2lKMFpYTjBRR1Z6YTJsNkxuVjZJaXdpY205c1pTSTZJblZ6WlhJaUxDSmhjR2xmZEc5clpXNGlPaUpsZVVvd1pWaEJhVTlwU2t0V01WRnBURU5LYUdKSFkybFBhVXBKVlgiLCJzdGF0dXMiOiJpbmFjdGl2ZSIsInNtc19hcGlfbG9naW4iOiJlc2tpejIiLCJzbXNfYXBpX3Bhc3N3b3JkIjoiZSQkayF6IiwidXpfcHJpY2UiOjUwLCJ1Y2VsbF9wcmljZSI6MTE1LCJ0ZXN0X3VjZWxsX3ByaWNlIjoxMTUsImJhbGFuY2UiOjEwMDMsImlzX3ZpcCI6MCwiaG9zdCI6InNlcnZlcjEiLCJjcmVhdGVkX2F0IjpudWxsLCJ1cGRhdGVkX2F0IjoiMjAyMy0wMy0xM1QxNDo0MDoxMy4wMDAwMDBaIn0sImlhdCI6MTY3ODcxODU3MiwiZXhwIjoxNjgxMzEwNTcyfQ.5wG9ZA6r8-gvhxElGJyq5137LlARBtn59B0-8Bgj3ho'

headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
