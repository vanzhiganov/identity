# Identityserver

## Endpoints

### `[POST] /api/identity/0.1/user/`

Create a new user account

**Request**

    curl -X POST 'https://rest-api.ru/api/identity/0.1/user/' \
    -H 'Content-Type: application/json' \
    -d '{
        "email": "vanzhiganov@ya.ru",
        "password": "...",
        "domain": "rest-api.ru"
    }'

**Response**

    {
        "status": {
            "code": 0,
            "message": "Success"
        }
    }

### `[POST] /api/identity/0.1/tokens/`

Create new JWT-token

**Request**

    curl -X POST 'https://rest-api.ru/api/identity/0.1/tokens/' \
    -H 'Content-Type: application/json' \
    -d '{
        "email": "vanzhiganov@ya.ru",
        "password": "...",
        "domain": "rest-api.ru"
    }'

**Response**

    {
        "response": {
            "token": "<JWT>"
        },
        "status": {
            "code": 0,
            "message": "Success"
        }
    }

### `[DELETE] /api/identity/0.1/tokens/`

Revoke current JWT-token

**Request**

    curl -X DELETE 'https://rest-api.ru/api/identity/0.1/tokens/' \
    -H '{JWT}'

