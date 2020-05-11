# COVID-19 GeoTracker - Backend

#### Login
```cURL
curl --location --request POST 'http://127.0.0.1:8000/auth/login' \
--header 'Content-Type: text/plain;charset=UTF-8' \
--data-raw '{
    "username": [username],
    "password": [password]
}'
```
