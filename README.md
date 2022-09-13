# Library_mangement_system
it is created using django drf as backend and jquery &amp; javascript in frontend


List of Endpoints :
 1) http://127.0.0.1:8000/api/admin [crud can be performed only by user with usertype = "1" ie Admin , usertype  = "2" means Student.
 2) http://127.0.0.1:8000/api/student [only read operation]
 3) http://127.0.0.1:8000/api/user [for creating new users, ever new user is a student , however superuser can change them into admin (choice is available).
 4) http://127.0.0.1:8000/login [for login purpose, based on which user will be redirected to respective page.]
 
 i have used token based authentication system (email based).
 
 In frontend (Html, css, javaScript, query and bootstrap) is used for simplicity purposes as they were sufficient for the project.

For frontend, following are the urls : 
1) http://127.0.0.1:5500/login.html
2) http://127.0.0.1:5500/register.html
3) http://127.0.0.1:5500/adminView.html
4) http://127.0.0.1:5500/studentview.html

 use following ports only , as in settings.py file I have allowed only one domain ie   "http://127.0.0.1:5500/" .
