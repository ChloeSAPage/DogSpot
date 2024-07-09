# *DogSpot*

#### *Discover Dog Friendly Adventures.*

![image](https://github.com/ChloeSAPage/DogSpot/assets/135153095/dbcdbf1a-0489-4075-96e0-7ec352813619)

---

## The Team:
* [**Adele Cousins**](https://github.com/adelikinz)
* [**Chloe Page**](https://github.com/ChloeSAPage)
* [**Yasmin Panahi**](https://github.com/YasPan98)
* [**Jessica Steventon**](https://github.com/Jess7000)
* [**Ellie Caldwell**](https://github.com/WhatIsEllie)

---

## About our project

The primary aim of our project was to create a user-friendly website to help dog owners find dog-friendly locations. The platform addresses the growing need for reliable information about places where dogs are welcome, allowing owners to include their furry friends in their daily activities and travels.

We have created a search functionality that allows users to find dog-friendly locations based on a given location. We integrated the Yelp API to provide the dog-friendly establishments with additional information such as reviews, opening hours and contact hours. We also integrated the Google Maps API to provide the user with directions to their chosen location.

The inspiration for this project stemmed from the noticeable increase in dog ownership during the COVID-19 pandemic. With many individuals working from home or being furloughed, people looked towards dog adoption for companionship. However, more recently the world has returned to normalcy and lots of people have busy schedules. This has resulted in a struggle between balancing dog care with daily responsibilities. There is a growing need for solutions that enable dog owners to integrate their dogs into their lifestyle.

Our website aims to provide a solution to this problem by providing users with dog-friendly locations. The website has a simple user interface that is easy to use to ensure a seamless user experience. This solution encourages responsible dog ownership as well as mitigating issues related to dog abandonment by making it easier for dog owners to include their dogs in their activities.


### Built with
[![Languages used](https://skillicons.dev/icons?i=js,html,css,python,flask,mysql,git&perline=20)](https://skillicons.dev)

### Tools used
[![Tools used](https://skillicons.dev/icons?i=github,postman,pycharm,vscode&perline=20)](https://skillicons.dev)


---

## Installing and How To Use This Project

This application is _not_ hosted and thus will need to be installed on your local machine.

> [!IMPORTANT]
> You will need:
>
> -   A Yelp API key
> -   A Google Maps API key
> -   MySQL credentials
> 


### 1. Clone the Repository

Using Git, copy these files into a folder.
Use this command:

```
git clone https://github.com/WhatIsEllie/CFG_Software_2_Group_6.git
```

### 2. Install the requirements

```
pip install -r requirements.txt
```

### 3. Edit the config.py file in the root directory and add your yelp API key, Google Maps API key and your MYSQL credentials.

> [!WARNING]
> **The file should be formatted as such, with the appropriate details. Otherwise it will _not_ work**

```
# yelp api key
API_KEY = "" 

# google maps api key
GMAP_API_KEY ="" 

#mysql credentials
host=""
user=""
password=""
database="pet_friendly_database"
```

### 4. Create your database 
To do this you need to make sure your config file has your sql login details, then all thats needed to do is run the `database.py` file, this should create the database and the necessary data tables needed to run this app.

> [!WARNING]
> **Make sure the config has the correct details otherwise the database will not be created. this will cause issues running the app**

### 5. Run

> [!CAUTION]
> Running the files in a different order may cause issues, please use `app.log` to debug further.

1. Make sure all the above steps above have been followed.
2. Run `app.py`
3. Go to this address in your browser if you are localhosting `http://127.0.0.1:5000` refer to link in `app.log` otherwise.
5. Use the app

