
# PicsGarage
[![BCH compliance](https://bettercodehub.com/edge/badge/kamauvick/PicsGarage?branch=master)](https://bettercodehub.com/) 
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)   
#### Author
> Victor Waichigo K.

## Description
PicsGarage is a personal gallery django application that allows users display their photos for others to see.

## Screenshots
<img src='https://github.com/kamauvick/PicsGarage/blob/master/pics/static/assets/galleryshot.png?raw=true' width=1000>
<img src='https://github.com/kamauvick/PicsGarage/blob/master/pics/static/assets/gshot.png?raw=true' width=1000>

## Setup Instructions:
### Requirements

##### 1. Clone the repository
Clone the the repository by running 

   ```bash
   git clone https://github.com/kamauvick/PicsGarage.git
   ```
 or download a zip file of the project from github
 

Navigate to the project directory
```bash
cd PicsGarage
```

##### 2. Create a virtual environment
 Install `Virtualenv` 

   ```prettier
   pip install virtualenv
   ```

To create a virtual environment named `virtual`, run

   ```prettier
   virtualenv virtual
   ```
To activate the virtual environment we just created, run

   ```bash
   source virtual/bin/activate
   ```

##### 3. Create a database
You'll need to create a new postgress database, Type the following command to access postgress
   ```bash
    $ psql
   ```
   Then run the following query to create a new database named ```picsgarage``` 
   ```prettier
   # create database picsgarage
   ```


#####  4.Install dependencies
To install the requirements from `requirements.txt` file,

   ```prettier
   pip install -r requirements.txt
   ```

#####  5.Create Database migrations
Making migrations on postgres using django

```prettier
python3 manage.py makemigrations garage
```

 
then run the command below;

 ```bash
 python3 manage.py migrate
 ```

##### 6.Run the app
To run the application on your development machine, 

    python3 manage.py runserver

### Running Tests
>To run tests;

    python3 manage.py test

## Technologies Used
* Django
* Python
* Html
* Css
* Javascript
* Bootstrap


## User stories
>As a user of the application I should be able to:

- [X] View different photos that interest me.
- [X] Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
- [X] Search for different categories of photos. (ie. Travel, Food)
- [X] Copy a link to the photo to share with my friends.
- [X] View photos based on the location they were taken.

## Behaviour Driven Development (BDD)

## Bugs
There are no know bugs at the moment

## License
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)
>MIT license &copy;  2019 Victor
 
## Collaboration Information
* Clone the repository
* Make changes and write tests
* Push changes to github
* Create a pull request

## Contacts
Reach me on:
>Email:  waichigovick@gmail.com

>Twitter:  [@kamau_vick](https://twitter.com/kamau_vick)

