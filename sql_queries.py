# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SONGPLAYS"
user_table_drop = "DROP TABLE IF EXISTS USERS"
song_table_drop = "DROP TABLE IF EXISTS SONGS"
artist_table_drop = "DROP TABLE IF EXISTS ARTISTS"
time_table_drop = "DROP TABLE IF EXISTS TIME"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS SONGPLAYS (songplay_id int,
	start_time varchar,
    user_id int,
    level varchar, 
    song_id varchar, 
    artist_id int, 
    session_id int, 
    location varchar, 
    user_agent varchar
)

""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS USERS (user_id int, 
	first_name varchar, 
	last_name varchar, 
	gender varchar, 
	level varchar)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS SONGS (song_id varchar, 
	title varchar, 
	artist_id varchar, 
	year int, 
	duration numeric)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS ARTISTS (artist_id varchar, 
	name varchar, 
	location varchar, 
	latitude varchar, 
	longitude varchar)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS TIME (start_time varchar, 
	hour varchar, 
	day varchar, 
	week varchar, 
	month varchar, 
	year varchar, 
	weekday varchar)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO SONGPLAYS (songplay_id,
	start_time,
    user_id,
    level, 
    song_id, 
    artist_id, 
    session_id, 
    location, 
    user_agent)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO USERS (user_id, 
	first_name, 
	last_name, 
	gender, 
	level)
	VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""INSERT INTO SONGS (song_id, 
	title, 
	artist_id, 
	year, 
	duration)
	VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""INSERT INTO ARTISTS (artist_id, 
	name, 
	location, 
	latitude, 
	longitude)
	VALUES (%s, %s, %s, %s, %s)
""")


time_table_create = ("""CREATE TABLE IF NOT EXISTS TIME (start_time timestamp, 
	hour int, 
	day int, 
	week int, 
	month int, 
	year int, 
	weekday int)
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]