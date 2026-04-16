import httpx
from tools import faker


create_payload = {
    "email": faker.get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
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


create_file_header = {
    "Authorization": f"Bearer {user_token['token']['accessToken']}"
}

create_file_response = httpx.post(
    "http://localhost:8000/api/v1/files",
    data={"filename": "image.png", "directory": "courses"},
    files={"upload_file": open('./testdata/files/images.jpg', 'rb')},
    headers=create_file_header
)

create_file_response_data = create_file_response.json()
print(f"Create File data:", create_file_response_data)