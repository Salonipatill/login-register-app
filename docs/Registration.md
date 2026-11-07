# Registration Questions and Answers

## Why import `APIRouter`?

`APIRouter` is a FastAPI class used to group related API routes in a separate
module. Registration and login routes can be kept in an authentication router
instead of placing every route in `main.py`.

```python
from fastapi import APIRouter
```

The router is then included in the main application:

```python
from fastapi import FastAPI
from routes.auth import router as auth_router

app = FastAPI()
app.include_router(auth_router)
```

## Why import `EmailStr` and `Field`?

Both are provided by Pydantic and are used to validate request data:

```python
from pydantic import BaseModel, EmailStr, Field
```

- `EmailStr` checks that a value has a valid email address format.
- `Field` adds constraints and metadata to a model field, such as minimum
  length, maximum length, a description, or a default value.

Example:

```python
class RegistrationRequest(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)
```

If a request does not satisfy these rules, FastAPI returns a validation error
instead of passing invalid data to the route function.

## Why create an `APIRouter`?

Creating a router gives a group of related endpoints a clear boundary. It
makes the application easier to organize, test, and maintain.

```python
from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)
```

The router can contain registration, login, logout, and password-reset
endpoints. It must be included with `app.include_router(router)` for its
routes to be available.

## Why use `prefix` and `tags`?

- `prefix` adds the same path prefix to every route in the router. For
  example, `prefix="/auth"` changes a route declared as `"/register"` into
  `"/auth/register"`.
- `tags` groups endpoints in FastAPI's generated Swagger UI documentation.
  Tags affect documentation organization only; they do not change the URL.

Example:

```python
router = APIRouter(prefix="/auth", tags=["Authentication"])
```

## How do I set minimum and maximum length?

Use `min_length` and `max_length` in `Field` for string fields:

```python
username: str = Field(..., min_length=3, max_length=30)
password: str = Field(..., min_length=8, max_length=128)
```

`min_length` rejects strings that are too short, and `max_length` rejects
strings that are too long. The values are inclusive: a string with exactly
the minimum or maximum number of characters is valid.

For a list, use `min_length` and `max_length` in Pydantic v2 as well:

```python
roles: list[str] = Field(default_factory=list, max_length=5)
```

For numeric values, use `ge` and `le` (greater-than-or-equal and
less-than-or-equal), rather than string-length options:

```python
age: int = Field(..., ge=18, le=120)
```

## How do I write `Field()` and assign length?

The first argument, `...`, means the field is required. Constraints are
written as keyword arguments:

```python
field_name: str = Field(
    ...,
    min_length=2,
    max_length=100,
    description="The user's full name",
)
```

If a field is optional or has a default value, provide that value instead:

```python
display_name: str = Field("Guest", min_length=2, max_length=50)
```

Do not use `min` or `max` for string length. Use `min_length` and
`max_length`. Also note that a length limit counts characters; it does not
enforce password complexity such as requiring a number or a special
character.

## How do I create and use `@router`?

`router` is the `APIRouter` instance. Its methods are used as decorators to
register a path operation:

```python
from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register_user(data: RegistrationRequest):
    return {"message": "Registration successful"}
```

The decorator registers the function with the router. FastAPI calls the
function when a matching HTTP request is received.

## Why use `post`?

`POST` is normally used for registration because the client sends data to
create a new resource, such as a user account. The request data is usually
sent in the JSON body.

```python
@router.post("/register", status_code=201)
def register_user(data: RegistrationRequest):
    ...
```

`GET` is generally used to retrieve data, while `PUT` or `PATCH` updates data
and `DELETE` removes data. The HTTP method communicates the intended action
and lets FastAPI generate accurate API documentation.

## Why use `.` (the dot)?

A dot accesses an attribute or method of an object. In this example,
`router.post` accesses the `post` method on the `router` object:

```python
@router.post("/register")
```

The same syntax is used for other objects, such as `app.include_router(...)`
or `Field(...)` when it is accessed through an imported module. The dot does
not create a route by itself; `router.post(...)` (used here as a decorator)
registers the route.
