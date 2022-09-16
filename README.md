**Assignment:** 
True Value Access - Create REST APIs using Python (Flask, Django, any other web framework of your choice) for managing the user’s data.
The Django Rest Framework is used.The defualt Django database SQLite is used. 
The user data has been taken from the sample data already given. It is assumed as user data. 

The API has the following functionalities:

1) list users (/api/users - GET) - This functionality lists all the users in the database (There are 500 users in the given sample data). The endpoint for this is taken as - **'/api/users'**
2) create new user (/api/users - POST) - new users are created. The endpoint is **'/api/users'** 
3) get detail of a user (/api/users/ - GET) - using the id the details of the user can be fetched. The endpoint is **'/api/users/3'**. Here <id> is 3. 
4) update details of a user (/api/users/ - PUT) - details of the user can be updated. The endpoint is **'/api/users/3'**. Here <id> is 3.
5) delete a user (/api/users/ - DELETE) - details of a user can be deleted by selecting the id of the user. The endpoint is **'/api/users/3'**. Here <id> is 3.  
6) search for a user by name - Search functionality has been implemented which checks for the first_name and last_name and renders the user whose name matches. Also the endpoint can be changed as **'/api/users/usersearch/?search=ram'**. Here, url has been made as usersearch and here <ram> is the name queried 
7) sort list by field name - Django filters have been used (ordering class) which gives a drop down box in a 'filters' option of ascending and descending order of all the field names which can be chosen. Also the endpoint can be changed as **'/api/users/usersearch/?ordering=-city'**. Here, url has been made as usersearch and here <city> is the field sorted through in descending order (- is included for descending order). 
8) pagination of users list - Pagination has been done where there are page numbers for listing the users. Limits and pages have been applied which gives the limit of the number of users to be listed in a particular page. The endpoint created for pagination is **'/api/users/usersearch/?limit=3&page=6'**

**How to setup and run this project:- **
1) Install the latest version of Python. 
2) Install VS Code 
3) Activate the virtual environment using **venv\Scripts\activate**
4) Start th project with **python manage.py runserver**
