[![Build Status](https://travis-ci.org/sharkdevs/store-manager-APIs.svg?branch=ft-user-login-161342592)](https://travis-ci.org/sharkdevs/store-manager-APIs)
[![Coverage Status](https://coveralls.io/repos/github/sharkdevs/store-manager-APIs/badge.svg?branch=ft-user-login-161342592)](https://coveralls.io/github/sharkdevs/store-manager-APIs?branch=ft-user-login-161342592)
[![Maintainability](https://api.codeclimate.com/v1/badges/38e88c5668ba8d8b0045/maintainability)](https://codeclimate.com/github/sharkdevs/store-manager-APIs/maintainability) 
# store-manager-APIs
This branch contains a set of API endpoints including a login endpoitn. The endpoints can be used to GET and POST data to the store manager data structures as described below.

## API Endpoints covered included in this branch


| Method        |       Endpoint                |         Description               |
| ------------- |       -------------           |         -------------             |
| `GET`         | `/api/v1/products`            |  Gets all products in the store   |
| `GET`         | `/api/v1/products/<id>`       | Get a product by id               |
| `POST`        | `/api/v1/products`            |   adds a product to the store     |
| `GET`         | `/api/v1/sales`               |  Gets the sales order record      |
| `GET`         | `/api/v1/sales/<id>`          | Get a sale order by id            |
| `POST`        | `/api/v1/sales/<id>`          |   sale a product in the store     |
| `POST`        | `/api/v1/users/registration`  |  Register a user                  |
| `POST`        | `/api/v1/users/login`         | Signin a User                     |

## Set Up instructions
The following are a set of steps you can follow to set tu the application
#### Cloning the application
git clone https://github.com/sharkdevs/store-manager-APIs/

 #### Configure Virtual environment
     pip install Virtialenv
     virtualenv venv
     source /venv/Scripts/activate : windows  
     source /venv/bin/activate : linux

   ### Install dependancies
     pip install -r requirements.txt
    
## Unit Testing
To test the endpointsensure that the following tools are available the follow steps below
   ### Tools:
     Postman
### Commands
  The application was tested using `nose` and coverage. To run the tests on the bash terminal use
     
     nosetests --with-coverage --cover-package=app  && coverage report
     
## Deployment

The app is deployed in heroku. Click [here](https://shark-store-manager.herokuapp.com/)
after it opens, append the specific endpoint. 
ie `<url>/api/v1/products`

## Author

[Meshack Ogeto ](https://github.com/sharkdevs)
