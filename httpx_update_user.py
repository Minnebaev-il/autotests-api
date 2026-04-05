import httpx
from tools import faker


create_payload = {
    "email": faker.get_random_email(),
    "password": "string",
    "lastName": "Minnebaev",
    "firstName": "Ilnur",
    "middleName": "Wilurovich"
}
create_response = httpx.post(url="http://localhost:8000/api/v1/users", json=create_payload)
print(create_response.status_code)
print(create_response.json())

login_payload = {
    "email": create_payload['email'],
    "password": create_payload['password']
}
login_response = httpx.post(url="http://localhost:8000/api/v1/authentication/login", json=login_payload)
user_token = login_response.json()
print(login_response.status_code)
print(login_response.json())

edit_payload = {
    "email": faker.get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
edit_headers = {
    "Authorization": f"Bearer {user_token['token']['accessToken']}"
}
edit_response = httpx.patch(url=f"http://localhost:8000/api/v1/users/{create_response.json()['user']['id']}", headers=edit_headers, json=edit_payload)
print(edit_response.status_code)
print(edit_response.json())





