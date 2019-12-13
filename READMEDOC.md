# teacher-student-task-assigner
a django based backend implementation of a teacher-student task assignment system

# Task-Assignment-System

Student's View
![24](https://user-images.githubusercontent.com/46242531/70828496-76861f00-1e11-11ea-99a8-f6862294f739.PNG)

Teacher's view
![23](https://user-images.githubusercontent.com/46242531/70828811-2065ab80-1e12-11ea-9b1d-fa3f797e3a64.PNG)
# New Features!

  - Import a HTML file and watch it magically convert to Markdown
  - Drag and drop images (requires your Dropbox account be linked)



## Requirements
  - Django v >=2.1, Python v >=3
  - Sqlite 3
  - Python 3.6

# Procedure
Clone this repository and then

### First install a virtual environment to test this, using command


```sh 
    $ virtualenv testenv 
    $ source testenv/bin/activate
    $ pip install -r requirements.txt
```


### Just do migration for the app from project root.

```sh    
    $ python manage.py migrate
```

### Creating an admin and other users for testing
- Admin (Teacher) can be created using this command.

```sh   
    $ python manage.py createsuperuser
```

### after that run server locally with following command

```sh
   $ python manage.py runserver 0.0.0.0:8000
```

- Visit http://localhost:8000/admin in the browser to add few students(users).

#### Done
- Admin(teacher) can create new tasks and assign them to multiple students.
- Can see all taskes he created and who else are assigned to him from dashboard.
- User(student) can login to his account and see tasks assigned to him.
- He/She can change the status of task assigned to him like todo, doing, done etc.

### Todo
> Signup & Password recovery

> Approval & Disapproval of assignments by Admin(Teacher)

> Real time notifications to the Admin about the student task updates.

> Please check the issues/features and give pull requests to improve tasker.

> Check images/ directory for screenshots.


Markdown is a lightweight markup language based on the formatting conventions that people naturally use in email.
