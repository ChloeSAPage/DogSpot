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
Hi, I'm Yasmin and I'm a student on the Spring '24 Software CFGdegree Programme.

---

Facts about me:

- I love anything to do with fitness, expecially running and CrossFit
- I did my degree in Chemistry, and used to work as a Chemical Analyst
- I love animals, and I have a Pomeranian called Benji!

<details>
  <summary> My Tech journey </summary>
I work in an ed-tech company and discuss technical concepts everday at work, but never fully knew what they meant. I tried a few of the CFG classes and loved them, so decided to take the plunge and do the CFGdegree to expand my knowledge and help me gain a better understanding of the world of tech!

</details>
</details>
&nbsp;
<details>
<summary> About Jessica</summary>
Hi, my name is Jessica and I'm a student on the CFG Degree specialising in software engineering.


---

Facts about me:

- I love playing and watching sports, especially football.
- I enjoy binging netflix shows and watching new films at the cinema.
- I enjoy trying new restaurants with friends.


<details>
  <summary> My Tech journey </summary>

I studied Accounting & Finance at uni, but after beginning my first full-time job I realised I was interested in taking on more technical work and so I started to teach myself to code. I discovered Code First Girls and completed the 8-week SQL course which I loved. This then led me to apply to the nano degree to continue my coding journey and I am hoping this will lead me to my first job as a software engineer.


</details>
</details>
&nbsp;
<details>
<summary> About Ellie</summary>
Hi, I'm Ellie 👋 I'm a student on the CFG Degree doing the software engineering stream.

---

Facts about me:

- In my free time I snowboard and play roller derby
- I have a pet cat called Maggie
- I love gaming and have a fully pink gaming set up

<details>
  <summary> My Tech journey </summary>

I studied data science at univeristy and have been working as a data analyst for the last two and a half years. I have a bit of tech background from both my studies and my career, and spend a lot of my day writing SQL and retrieving and cleaning data from APIs using Python. However, I have a real passion for the software engineering side of things from all the way back at college so have really enjoyed learning more on the CFG Degree. I hope to move into a career in software engineering! 


</details>
</details>
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

