## Contents
- [My Recipe Book site](#my-recipe-book-site)
- [UX](#ux)
- [Database Schema](#database-schema)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

# My Recipe Book site 
My Recipe Book represents a full-stack web application that uses the relational database PostgreSQL, the Django full stack MVC framework. The project also includes setup of the authentication mechanism and checkout system.

![screen shots on various devices](static/img/readme/am-i-responsive.PNG)

# UX

## Who is this website for?
For users who want to create and manage their recipes online.

## What it is that they want to achieve?
They need a simple way to write down new cooking recipes in an online recipe book, be able to find them, edit or delete.

## How does the project fulfil the users’ needs?
The implementation provides intuitive user interface for creation of new recipes. The website requests users to be authenticated and authorised in order to manage their own recipes. Add recipe page lists all necessary fields for writing a new recipe, e.g. recipe name, course name, ingredients, preparation steps and time. Additionally image upload option is available for users. For quick and easy search, users can use either the course cards from Home page or the search field and 'Filter by Course' dropdown located on My recipes page. Each recipe can be modified and removed. The site is functioning on desktop as well as on mobile devices.

## Wireframes
The [wireframes](https://github.com/AnaStasia1331/ms4-recipe-book/tree/master/static/img/readme/wireframes) were created using Balsamiq tool.

## User Stories 
As a website user, I want to:

1. access the website as an anonymous user and understand what it offers to users.
2. be able to create a new account.
3. be able to log into an existing account.
4. be able to reset password.
5. use the Google authentication to sign into the website account.
6. be able to log out.
7. be able to add/edit/delete recipes when I'm logged in.
8. see only my own recipes.
9. find an existing recipe based on the category/group it belongs to.
10. search recipes via the search field.
11. make one-time secure payment for using the website.
12. my recipes are not visible when I'm an anonymous user.
13. access the website from multiple devices of different sizes without major UI issues.

## Nice-to-have features 

1. User settings page with the option to edit username or email address and the reset password functionality. 
2. As the next stage it could be the possibility to share recipes with other users.

# Database Schema 

Heroku deployment uses the PostgreSQL relational database, whereas in the development mode the project runs on SQLite3 provided by the Django framework by default.

The database schema:
![Schema](static/img/readme/)