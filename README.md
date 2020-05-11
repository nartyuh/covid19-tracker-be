# COVID-19 GeoTracker - Backend

#### Register
```cURL
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

#### Check user token
```cURL
curl --location --request POST 'https://apic19gt.tranquanghuy.me/auth/user' \
```

#### Get user logs
```cURL
curl --location --request GET 'https://apic19gt.tranquanghuy.me/logs/log' \
```

