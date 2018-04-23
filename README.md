# Todo App
This web applicaiton is designed to help you check out things you want to do. 

## Built With
Python 3.6 and Django 2.0

### Libraries 

* **Django libraries** - django.shortcuts django.db.models django.utils django.contrib django.http django.urls

* **Python libraries** - datetime

## Usage and Design
After creating todo lists, you could add todos under them. 
You need to give title and deadline to todos before you can create them.
Each todo has a button that indicates the status whether or not it is completed. 
If you click the button, the status will be reversed. 
At the bottom of the todo detail page, whose url ends with "*/detail/todolist_id/*", you can find two buttons.
First one deletes the todo list this todo belongs to. Second one deletes completed todos in the same todo list.  
Searching for todo lists and todos are also possible by clicking the link on the top-right corner.

## Set up Development Environment
First, clone this repository from github.
```
git clone https://github.com/shiiyan/Todo-App.git
```
After move to the main directory of this app, run

```
cd myproject
python manage.py runserver
```
and you are ready to go.

