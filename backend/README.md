# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.


## API description

#### Endpoints

1. GET '/drinks'
2. POST '/drinks'
3. GET '/drinks-detail'
4. PATCH '/drinks/<id>'
5. DELETE '/drinks/<id>'

#### GET '/drinks'

Description: Get the list of registered drinks with a short description for visualization.

Parameters: None

Expected result:
```json
{
    "success": true,
    "drinks": 
    [
        {
            "id": 0,
            "title": "drink name",
            "recipe": 
            [
                {
                    "color": "ingredient color",
                    "parts": 1
                }
            ]
        }
    ]
}
```

Errors: None

#### POST '/drinks'

Description: Adds a new recipe to the database.

Parameters: 
1. title: 
    - String
    - Name of the new drink
    - Required:
2. recipe: 
    - String
    - List of ingredients to make the drink
    - Required

Expected result:
```json
{
    "success": true,
    "drinks": 
    [
        {
            "id": 0,
            "title": "new drink name",
            "recipe": 
            [
                {
                    "name": "ingredient name",
                    "color": "ingredient color",
                    "parts": 1
                }
            ]
        }
    ]
}
```

Errors: 
1. Missing required parameter: ERROR 422

#### GET '/drinks-detail'

Description: Get the list of registered drinks with a list of ingredients.

Parameters: None

Expected result:
```json
{
    "success": true,
    "drinks": 
    [
        {
            "id": 0,
            "title": "drink name",
            "recipe": 
            [
                {
                    "name": "ingredient name",
                    "color": "ingredient color",
                    "parts": 1
                }
            ]
        }
    ]
}
```

Errors: None

#### PATCH '/drinks/<id>'

Description: Updates the name or the recipe of an existing drink.

Parameters:
1. title: 
    - String
    - Name of the new drink
    - Optional 
2. recipe: 
    - String
    - List of ingredients to make the drink
    - Optional
Note: Required at least 1 parameter

Expected result:
```json
{
    "success": true,
    "drinks": 
    [
        {
            "id": 0,
            "title": "updated drink name",
            "recipe": 
            [
                {
                    "name": "ingredient name",
                    "color": "ingredient color",
                    "parts": 1
                }
            ]
        }
    ]
}
```

Errors: 
1. No parameter provided: ERROR 422
2. ID does not exist in database: ERROR 404

#### DELETE '/drinks/<id>'

Description: Updates the name or the recipe of an existing drink.

Parameters: None

Expected result:
```json
{
    "success": true,
    "drinks": 1
}
```

Errors: 
1. ID does not exist in database: ERROR 404