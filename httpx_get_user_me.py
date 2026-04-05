import httpx


payload = {
        "email": "iw@qaen.ru",
        "password": "Dream=007!"
}
with httpx.Client() as client:
    login = client.post("http://localhost:8000/api/v1/authentication/login", json=payload)
    login.raise_for_status()
    print(login.json())
    print(login.status_code)
    token = login.json().get("token", {}).get("accessToken")
    headers = {"Authorization": f"Bearer {token}"}
    me = client.get("http://localhost:8000/api/v1/users/me", headers=headers)
    me.raise_for_status()
    print(me.json())
    print(me.status_code)