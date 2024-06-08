# *DogSpot*

#### *Discover Dog Friendly Adventures.*

---

## The Team:
* [**Adele Cousins**](https://github.com/adelikinz)
* [**Chloe Page**](https://github.com/ChloeSAPage)
* [**Yasmin Panahi**](https://github.com/YasPan98)
* [**Jessica Steventon**](https://github.com/Jess7000)
* [**Ellie Caldwell**](https://github.com/WhatIsEllie)

#### Here is some information about us:

<details>
<summary>About Adele</summary>
Hello, my name is Adele and im based in Bristol. im a student on the CFG Degree Spring '24 cohort for software engineering.

---

Fact about me:
* I have two gerbils named bean and toast which I adore and spoil way too much.
* I love playing video games, I have a love hate relationship with counterstrike 2 (cs2)
* I also love to read, I prefer reading biographies, but I also enjoy an occasional fantasy novel too

<details>
<summary> My Tech journey </summary>
before joining the CFG Degree Spring course I actually never wrote code before. for years before I was always put off
as I thought it looked complicated. Early December I was encouraged to give it a try and I started by researching
and reading basic guides on python. this then developed a passion and made me look for ways to pursue education further.

</details>
</details>
&nbsp;
<details>
<summary> About Chloe</summary>
Hiya! I'm Chloe.


---

Facts about me:

- I really like birds.
- I enjoy hiking.
- I like playing video games, and have been playing League of Legends for way too long.

<details>
  <summary> My Tech journey </summary>

I did my degree in Microbiology, and during that time I did one coding project. When I graduated and entered the working world, I realised I didn't really enjoy the practical work of a laboratory, so I decided to take up some Python courses which lead me here!


</details>
</details>
&nbsp;
<details>
<summary> About Yasmin</summary>
...add

---

Facts about me:

... insert facts about you ...

<details>
  <summary> My Tech journey </summary>

... insert tech journey summary ...


</details>
</details>
&nbsp;
<details>
<summary> About Jessica</summary>
...add summary...

---

Facts about me:

... insert facts about you ...

<details>
  <summary> My Tech journey </summary>

... insert tech journey summary ...


</details>
</details>
&nbsp;
<details>
<summary> About Ellie</summary>
...add summary...

---

Facts about me:

... insert facts about you ...

<details>
  <summary> My Tech journey </summary>

... insert tech journey summary ...


</details>
</details>
---

## About our project

...why we made this project...

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
to do this you need to make sure your config file has your sql login details, then all thats needed to do is run the `database.py` file, this should create the database and the necessary data tables needed to run this app.

> [!WARNING]
> **Make sure the config has the correct details otherwise the database will not be created. this will cause issues running the app**

### 5. Run

> [!CAUTION]
> Running the files in a different order may cause issues, please use `app.log` to debug further.

1. Make sure all the above steps above have been followed.
2. Run `app.py`
3. Go to this address in your browser if you are localhosting `http://127.0.0.1:5000` refer to link in `app.log` otherwise.
5. Use the app

