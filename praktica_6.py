import httpx

login_data = {
    "email": "user@example.com",
    "password": "string"
}
post_response = httpx.post("http://localhost:8000/api/v1/authentication/login",json=login_data)
print(post_response.json())
print(post_response.status_code)

access_token = post_response.json()['token']['refreshToken']

get_response = httpx.get("http://localhost:8000/api/v1/users/me", headers={"Authorization": f"Bearer {access_token}"})
print(get_response.json())
print(get_response.status_code)
