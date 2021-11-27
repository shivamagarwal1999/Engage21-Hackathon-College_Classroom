# Engage21-Hackathon-College_Classroom

## Introduction:

College-Classroom-Portal  is a web application that is meant for providing easy access between students and teachers during online learning. The app has two different types of users. You can register as a teacher, or you could register as a student. If you register as a teacher, you can create classrooms, and inside those classrooms, you can create announcements. If you register as a student, you can join classes with a unique code generated for that class. Students will be able to see announcements and can comment.Students and teachers are both able to post announcements and class comments in the classroom. Class comments are a good way to communicate with other peers in the class.In addition to the base functionality of classrooms, announcements and comments, users can upload profile pictures to customize their profile.
Registration cane be done using College mail id ,for now, I have used **@nsec.ac.in** as condition that only with this mail id, sudents and teachers can register and I have also made username  unique,so that anyone with same mail id can't create another usernames.
After registration , one need to again login and then wil be lended to **index.html** page.

## Files:

The files that make up most of the project,I have changed are inside the educationPortal app/folder inside the project directory called education-app.

## Templates:
The templates folder inside the app directory contains the HTML files for the different pages on the website.

The **layout.html** template contains the base HTML code that other templates can extend from.

The next templates are **login.html** and **register.html**. These templates handle users logging in and creating new users respectively. They both have a form that sends a POST request to the **views.py** file when the user registers or signs in.

The **index.html** template is the main page the user arrives at when he/she is logged in. This page displays all of the classes the user is associated with. If the user is a teacher, the user will see all of the classes he/she teaches. If the user is a student, the **index.html** page will show all the classes that he/she is a part of.

The **ViewClass.html** template is the page that displays a specific classroom. On that page, classroom information, announcements, and class comments will be displayed. The user can create announcements and class comments.

## Python Files:

The main python files outside the templates directory I edited were **models.py**, **views.py**, and **urls.py**.

The **models.py** file has all the models in the app. In this app, there are 4 models. Each model has a specific purpose. Here is a list of the models: User, Classroom, Comment (class comments on announcements), Announcement. 

## Views.py functions:
The **views.py** has all the functions that handle the different paths on my website and handle the information processing. The index view gets all the classes associated with the signed-in user.

The **login_view** view takes data from the incoming post request and attempts to sign the user in.

The **register** view takes incoming post request data and tries to create a new user.

The **createNewClassroom** view creates a new classroom with a unique code using the data provided from a post request (such as the name of the classroom).

The **JoinClassroom** view allows a user to join a classroom as a student if it received a post request. If it receives a delete request from a teacher, it will delete the classroom with the given code from the delete request.

The **ViewClassroom** view will send information about the classroom, and all the announcements associated with the selected classroom.

The **makeAnnouncent** view will create an announcement with an Announcement model.

The **addComment** view will add a class comment to a given announcement.

The **urls.py** file has all of the different paths on my website set up. Each path has a view function, name, and URL associated with it.


## Static Files:

There are also many static files I created that are in the static folder inside the educationPortal app. These files include several CSS files. These CSS files are each associated with a template mentioned above. The CSS files help position and style the HTML content on the webpage. There are also some icons and images I used to make the website more visually appealing. Lastly, some static JavaScript files control the front end of the website (templates).

The **Classroom.js** file handles POST requests for making class comments and announcements while controlling the user interface and input fields.

The **index.js** file controls UI changes and post requests when making a new classroom. It also handles the side menu animation when you click on the three bars.


## Static Media Files:

I have configured a directory outside the educationPortal app, but in the main project directory education-app, where uploaded files by users during runtime get saved to. This directory is also called static/images. To configure this directory, I had to add the following to the **settings.py** file:
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
```

## How To Run:

To run this project, make sure you have a version of python that is greater than 3.8 installed on your computer. When you download the project, open the main parent directory of the entire project in any text editor with a built-in terminal (such as Visual Studio Code), or open the directory in your computer's terminal/command prompt. Once you have the terminal open at the same directory as the manage.py file, execute
```
pip install -r "requirements.txt"
```
This will install all the dependencies the project uses. Next, run
```
python manage.py runserver
```
in your terminal. This will open a local server in your browser window where you can use this app.

## Admin-access:

For accessing the 127.0.0.1:8000/admin .We need to run:
```
python manage.py createsuperuser
```
Then need to provide:
```
username:""
email:""
password:""
```
