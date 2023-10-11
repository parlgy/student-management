# student-management
This project contains code for a blogging web app which enables users to easily share, express and publish the contents in the form of blog.


### Technologies Used

* _python_
* _flask_

## Getting Started
### Installations
You can use the git clone  command as follows:
```sh 
user@username:~$ git clone https://github.com/parlgy/student-management.git  
user@username:~$ cd  student-management
user@username:~$ pip3 install -r requirements.txt  #install all the dependecies used in this project
user@username:~$ flask run  # use this command to start the server
```  
### User registration    
#### User gets registered to the system by making a request to the endpoint below
   + url: POST  [http://studentcrud1.pythonanywhere.com/api/auth/register]()
   ```python
     {"Content-type": "application/json"}

        body = {
                "first_name": "user first name",
                "last_name": "user last name",
                "email": "email@gmail.com",
                "password":"password"
        } 
````
    
The status_code of the response == 201 if the registration is successfull else returns a bad request error.(400)

### User Login  


