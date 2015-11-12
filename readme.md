# Seed CG REST API - HTB 2015
====

**About**
----

This REST API serves as the base for our client to access relevant data to our claims along with supporting analysis. 

**Objective**
----

Review and aggregate available data to predict the amount of volume (or range in volumes) that the County of Los Angeles
currently holds from runoff water, recycled water, and ground water. Use this data to determine which percentage each of 
these contributes to the overarching goal of having the County of Los Angeles locally source at least 60% of water supply. 
Also review any additional methods that may contribute to achieving this goal

**URL Parameters**
----

Currently, the following REST API is compatible with HTTP methods: `GET` `POST`

URL parameters exist (suject to change - probably will change tbh):
* `.../water/$` : returns the methods researched upon for water demand and supply in Los Angeles County
* `.../water/data/$` : returns specific claims about water demand/supply for each method listed in `.../water/$` endpoint

**Query Parameters**
----
For `.../water/data/$`, the following exist: 
* `?method=...`: Accepted parameters include any method found in the `.../water/$` endpoint
* `?raw_data=..` : Accepted parameters include `true` or `false` to see robot or human data output, respectively

**Usage: Pre-production**
----

**Non-technical**
  1. Download git: `pip install git`
  2. Clone the repository to your local machine: `git clone https://github.com/anthonycarlos92/seedLA_HTB_2015.git`
  3. Open your terminal and proceed to the path of your cloned repo (probably in Downloads tbh): `cd /path/to/directory/`
  4. Download required tools: `pip install requirements.txt`
  5. Create branch for your contributions to be reviewed using:`git checkout -b <your name>`
  6. Want to play? Runserver using: `python manage.py runserver`
  7. Hit endpoint 127.0.0.1:8000 (or whatever port you chose on local machine...)

**PLEASE NOTE**  If you do not intend to contribute to the REST API, you should not need to do anything mentioned above

**PLEASE ALSO NOTE** Before making any contributions (ie `git commit -m "..."` `git push origin <your branch>` please alert
the team to ensure no versioning conflicts will arise. 

**Techies**
  1. Fork repository https://github.com/anthonycarlos92/seedLA_HTB_2015.git
  2. `git clone https://github.com/<your user name>/seedLA_HTB_2015.git`
  3. If update made, create pull request to master repo
  4. If compatible (ie no merge conflicts) pull req will be merged :+1:


