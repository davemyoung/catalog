Project Title : Catalog 

Udacity course project to form a database driven web app using python, SQL alchemy and SQL lite. Main aim of app is set out in course project brief.

Users can log-in via Google+ and once verified have the ability to add, delete and edit categories and items.


Set up instructions 

In desired folder for installation, please run database_setup.py

Followed by additemsenmasse.py to populate the database with sample data.

And the file to start the database is project.py 

API endpoints . 

Json export of categories, and items within each category are provided via the following addresses

/category/<int:category_id>/JSON   - will give items per category

/category/JSON - will give categories 