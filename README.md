# Chop It Like It's Hot, The Django Recipe App

## Description
[Chop It Like It's Hot](https://shielded-badlands-21677-49d691812b2d.herokuapp.com/) is a recipe web app built with Django. It is the successor to the [Python command line recipe app](https://github.com/cmr927/recipe-app-cli).

Users can create and modify recipes with ingredients, cooking time, and a difficulty parameter that is automatically calculated by the app. Users are able to search for recipes by their name and/or ingredients.

## Features
- Allow for user authentication, login, and logout.
- Let users search for recipes by name and/or ingredients.
- Automatically rate each recipe by difficulty level.
- Receive user input and handle errors appropriately.
- Display more details on each recipe if the user asks for that.
- Let users add their own recipes to a database.
- Include a Django Admin dashboard for working with database entries.
- Show statistics and visualizations based on trends and data analysis.

## Technical Stack
- Backend: Django, SQLite/PostgreSQL
- Frontend: HTML, CSS, Bootstrap
- Media Storage: Amazon S3 (via django-storages)
- Deployment: Heroku
- Data Visualization: Matplotlib
- Authentication: Django auth system (login, logout, register)

## Deployment
- Hosted on Heroku at:
[https://shielded-badlands-21677-49d691812b2d.herokuapp.com/]

Heroku environment includes:

- DEBUG=False for production
- DATABASE_URL for PostgreSQL
- AWS credentials for S3 integration

## Installation
1. Clone the repo

```
git clone <repository-url>
cd recipe-app
```

2. Create and activate the virtual environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```
pip install requirements.txt
```

4. Set up your .env:

```
DEBUG=True
DJANGO_SECRET_KEY=your_secret_key
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_STORAGE_BUCKET_NAME=your_bucket_name
```

5. Run migrations:
```
python manage.py makemigrations
python manage.py migrate
```
6. Create a superuser:
```
python manage.py createsuperuser
```

7. Create required directories:
```
mkdir media
mkdir static
python manage.py collectstatic
```

8. Start the server:
```
python manage.py runserver
```

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit)
