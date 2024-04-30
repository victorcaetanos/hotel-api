# hotel-api
## Swagger Documentation
 + /app/swagger
## Methods

API methods are defined as follows:

| Method   | Description                               |
|----------|-------------------------------------------|
| `GET`    | Returns one or more object's information. |
| `PUT`    | Creates a new object.                     |
| `PATCH`  | Updates an object information.            |
| `DELETE` | Deletes the object.                       |

## Status Codes

| Code  | Description                                     |
|-------|-------------------------------------------------|
| `200` | Successful request carrying a payload body.     |
| `201` | Successful request, resource created.           |
| `204` | Successful request not carrying a payload body. |
| `400` | Requested made with invalid syntax.             |
| `404` | Requested information not found.                |

## [/api/hotels/]

| String Parameters | Description        |
|-------------------|--------------------|
| None              | Use: ` `           |

### [GET]

+ Request (` `)

    + Response 200 (application/json)

          + Body
          [
              {
                  "id": 1,
                  "name": "Name1",
                  "city": "City1",
                  "address": "Address1"
              },
              {
                  "id": 2,
                  "name": "Name2",
                  "city": "City2",
                  "address": "Address2"
              },
              {
                  "id": 3,
                  "name": "Name3",
                  "city": "City3",
                  "address": "Address3"
              }
          ]
    + Response 404 (application/json)

          + Body
          {
              "message": "Could not find any hotel"
          }


### [PUT]

| JSON Parameters | Description       |
|-----------------|-------------------|
| name            | 0 > String <= 100 |
| city            | 0 > String <= 100 |
| address         | 0 > String <= 100 |

+ Request (application/json)

    + Body

          {
              "name": "Name1",
              "city": "City1",
              "address": "Address1"
          }
+ Response 201 (application/json)

    + Body

          {
              "id": 1,
              "name": "Name1",
              "city": "City1",
              "address": "Address1"
          }

+ Response 400 (application/json)

    + Body

          {
              "message": "Missing *JSON Parameter*, cannot insert"
          }

## [/api/hotels/<hotel_id>]

| String Parameters | Description        |
|-------------------|--------------------|
| hotel_id          | Use: `Integer > 0` |

### [GET]

+ Request (`hotel_id`)

    + Response 200 (application/json)

          + Body
          {
              "id": 1,
              "name": "Name1",
              "city": "City1",
              "address": "Address1"
          }

    + Response 404 (application/json)

          + Body
          {
              "message": "Could not find hotel with that id"
          }

### [PATCH]

| JSON Parameters | Description        |
|-----------------|--------------------|
| name            | 0 > String <= 100  |
| city            | 0 > String <= 100  |
| address         | 0 > String <= 100  | 

+ Request (application/json)

    + Body

          {
              "name": "Name1",
              "city": "City1",
              "address": "Address1"
          }
+ Response 200 (application/json)

    + Body

          {
              "id": 1,
              "name": "Name1",
              "city": "City1",
              "address": "Address1"
          }

+ Response 400 (application/json)

    + Body

          {
              "message": "Missing all parameters, cannot update"
          }

+ Response 404 (application/json)

    + Body

          {
              "message": "Hotel doesn't exist, cannot update"
          }

### [DELETE]

+ Request (`hotel_id`)


+ Response 204 (Empty)

        
+ Response 404 (application/json)

    + Body

          {
              "message": "Hotel doesn't exist, cannot delete"
          }
