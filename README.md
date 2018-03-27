# Identityserver

## Endpoints

`[POST] /api/identity/0.1/tokens/` - Create new JWT-token

Request

    curl -X POST 'https://rest-api.ru/api/identity/0.1/tokens/' \
    -H 'Content-Type: application/json' \
    -d '{
        "email": "vanzhiganov@ya.ru",
        "password": "...",
        "domain": "rest-api.ru"
    }'


Response

    {
        "token": "<jwt-token>"
    }