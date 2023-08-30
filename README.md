
# Order Handler

This is a simple api service for "making" orders to deliver your parcel from point to point. The service taking client`s name, length, width, weight of parcel and point from/to delivery. When order is created you're getting a number of your parcel by which you can check your parcel's status in the future if to be a such necessarity.



## Installation

There are two ways that depends on your wishes.

First way is where you`re gonna be using Docker.

- Clone or download the project from github.

- Have .env file in the project directory

- run your Docker engine (Desktop app)

- Run docker-compose --env-file {your .env file} up --build or     

- docker-compose up -d --build in your interpretator environment   or from console

- wait for gets builded all the containers

- check all the containers

- use the api (if it's required you can create your own virtual environment in app's docker container)


```bash
    git clone https://github.com/SteveJops/Test-task

    cd cloned repository
    
    run redis (Check Ping)
    
    run docker

    toggle to your browser
```

- Enter your request in browser (you can change the port of api)

    https://localhost:1337

Must see json response with urls (drf frontend switched off)

The second is to run the app without buiding docker containers.


```bash
    git clone https://github.com/SteveJops/Test-task

    cd cloned repository
    
    python -m pip -V

    python -m venv {your_venv_name}

    if windows: 

        {your_venv_name}\Scripts\activate

        cd {directory_with_env_file}

        move {env_file} {path_to_project_directory}

        cd {path_to_project_directory}

        dir (to check everything is okay)

        
    if linux:

        /usr/bin/activate

        cd {directory_with_env_file}

        mv {env_file} {path_to_project_directory}

        cd {path_to_project_directory}

        ls -l\a (to check everything is okay)

    pip install -r requirements.txt

    pip list (to check comparence the correctness of the libs)

    python manage.py runserver

    toggle to your browser

    localhost:8000
```
## Usage/Examples

/api/v1/ordesapp/orders/ - to get the list of list of all records or to make a new order from creation form (When your order was created it gets status "New", after a while status is being changed to "Placed", then to other remaining)

/api/v1/ordesapp/orders/<parcel_serial_number> - to get an opportunity to change your order, unless your status "Given", "Placed", but "New", "Refusal" (When your order was updated it gets status "New", after a while status is being changed to "Placed", then to other remaining)

/api/v1/ordesapp/order/<parcel_serial_number> - to get a current status of your parcel 
