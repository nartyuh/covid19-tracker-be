# COVID-19 GeoTracker - Backend

#### Register
```curl
curl --location --request POST 'https://apic19gt.tranquanghuy.me/auth/register' \
--header 'Content-Type: text/plain;charset=UTF-8' \
--data-raw '{
	"username": "johndoe",
	"email": "john.doe@example.com",
	"password": "12345
}'
```

#### Login
```cURL
curl --location --request POST 'https://apic19gt.tranquanghuy.me/auth/login' \
--header 'Content-Type: text/plain;charset=UTF-8' \
--data-raw '{
    "username": "johndoe",
    "password": "12345"
}'
```

#### 


