# Recipe App Django

## Description
This is a Recipe web app built with Django. It is the successor to the [Python command line recipe app](https://github.com/cmr927/recipe-app-cli).

Users can create and modify recipes with ingredients, cooking time, and a difficulty parameter that is automatically calculated by the app. Users should also be able to search for recipes by their ingredients.

## Features
- Allow for user authentication, login, and logout.
- Let users search for recipes according to ingredients.
- Automatically rate each recipe by difficulty level.
- Receive user input and handle errors appropriately.
- Display more details on each recipe if the user asks for that.
- Add user recipes to an SQLite database.
- Include a Django Admin dashboard for working with database entries.
- Show statistics and visualizations based on trends and data analysis.

## Technical Requirements
- Works on Python 3.6+ installations and Django version 5.
- Handles exceptions or errors that arise during user input, for example, then displays user-friendly error messages.
- Connects to a PostgreSQL database hosted locally on the same system (an SQLite database is needed during the development of your application).
- Provides an easy-to-use interface, supported by simple forms of input and concise, easy-to-follow instructions. Menus containing features like login and logout must be presented neatly—with concise and easy-to-follow prompts.

## Installation
