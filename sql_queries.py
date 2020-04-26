# DROP TABLES

songplay_table_drop = "DROP TABLE SONGPLAYS"
user_table_drop = "DROP TABLE USERS"
song_table_drop = "DROP SONGS"
artist_table_drop = "DROP TABLE ARTISTS"
time_table_drop = "DROP TABLE TIME"

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

song_table_create = ("""CREATE TABLE IF NOT EXISTS SONGS (song_id int, 
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

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]