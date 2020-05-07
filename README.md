# Project 1: Data Modeling with Postgres


## Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app

## Project

Create normalized tables  and store them into PostgreSQL.  Create Fact and Dimension tables  from songs metadata and user activity logs for analyzing user activity.

## Files

- etl.ipynb: develop the ETL process for each tables
- test.ipynb: test sql_queries.py and elt.ipynb (etl.py) 
- create_tables.py: create database and tables
- elt.py: define the ETL process
- sql_queries.py: define the SQL queries

## Data

### Songs metadata

The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.

```
song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json
```

And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.

```
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
```

### User activity logs

The log files in the dataset you'll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.

```
log_data/2018/11/2018-11-12-events.json
log_data/2018/11/2018-11-13-events.json
```

And below is an example of what a single activity log in 2018-11-13-events.json, looks like.

```
{"artist":null,"auth":"Logged In","firstName":"Kevin","gender":"M","itemInSession":0,"lastName":"Arellano","length":null,"level":"free","location":"Harrisburg-Carlisle, PA","method":"GET","page":"Home","registration":1540006905796.0,"sessionId":514,"song":null,"status":200,"ts":1542069417796,"userAgent":"\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.125 Safari\/537.36\"","userId":"66"}
```

## ETL Processes

### Songs metadata

#### #1: songs table

- Parse and read a song JSON file by using pandas.read_json function.
- Select columns for song ID, title, artist ID, year, and duration from dataframe.
- Execute insert query to songs table in PostgreSQL.
  - If the song ID confliction is occured, do nothing.

#### #2: artists table

- Parse and read a song JSON file by using pandas.read_json function.
- Select columns for artist ID, name, location, latitude, and longitude from dataframe.
- Execute an insert query to artists table in PostgreSQL.
  - If the artist ID confliction is occured, do nothing.

### User activity logs

#### #3: time table

- Parse and read a JSON file of user activity log by using pandas.read_json function.
- Filter records by NextSong action.
- Convert the ts timestamp column to datetime.
- Extract the timestamp, hour, day, week of year, month, year, and weekday from dataframe.
- Execute insert query to time table in PostgreSQL.


#### #4: users table

- Parse and read a JSON file of user activity log by using pandas.read_json function.
- Filter records by NextSong action.
- Select columns for user ID, first name, last name, gender and level from dataframe.
- Execute an insert query to songs table in PostgreSQL.
  - If the user ID confliction is occured, Update value of level on the recored.

#### #5: songsplays table

- Parse and read a JSON file of user activity log by using pandas.read_json function.
- Filter records by NextSong action.
- Select the timestamp, user ID, level, song ID, artist ID, session ID, location, and user agent from dataframe.
  - Log files don't include song ID and artist ID, so get these ID by executing select query to songs and artists tables.
- Execute  insert query to songs table in PostgreSQL.


## Usage

Create tables and execute ETL.

```
$ python create_tables.py
$ python etl.py
```
