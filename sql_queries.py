# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SONGPLAYS"
user_table_drop = "DROP TABLE IF EXISTS USERS"
song_table_drop = "DROP TABLE IF EXISTS SONGS"
artist_table_drop = "DROP TABLE IF EXISTS ARTISTS"
time_table_drop = "DROP TABLE IF EXISTS TIME"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE SONGPLAYS (songplay_id serial NOT NULL PRIMARY KEY,
    start_time bigint NOT NULL,
    user_id varchar NOT NULL,
    level varchar NOT NULL,
    song_id varchar,
    artist_id varchar,
    session_id int NOT NULL,
    lcation varchar,
    user_agent varchar);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS USERS (user_id int PRIMARY KEY, 
	first_name varchar NOT NULL, 
	last_name varchar NOT NULL, 
	gender varchar, 
	level varchar NOT NULL)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS SONGS (song_id varchar PRIMARY KEY, 
	title varchar NOT NULL, 
	artist_id varchar NOT NULL, 
	year int, 
	duration numeric NOT NULL)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS ARTISTS (artist_id varchar PRIMARY KEY, 
	name varchar NOT NULL, 
	location varchar, 
	latitude varchar, 
	longitude varchar)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS TIME (start_time timestamp PRIMARY KEY, 
	hour int NOT NULL, 
	day int NOT NULL, 
	week int NOT NULL, 
	month int NOT NULL, 
	year int NOT NULL, 
	weekday int NOT NULL)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO SONGPLAYS (
    start_time
    ,user_id
    ,level
    ,song_id
    ,artist_id
    ,session_id
    ,lcation
    ,user_agent
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""INSERT INTO USERS (user_id, 
	first_name, 
	last_name, 
	gender, 
	level)
	VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT ON CONSTRAINT users_pkey DO UPDATE SET level=excluded.level;
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
    ON CONFLICT ON CONSTRAINT artists_pkey DO NOTHING;
""")


time_table_insert = ("""INSERT INTO TIME (start_time, 
	hour, 
	day, 
	week, 
	month, 
	year, 
	weekday)
	VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT ON CONSTRAINT time_pkey DO NOTHING;
""")

# FIND SONGS

song_select = ("""

    
    
    SELECT s.song_id,a.artist_id 
    FROM songs s 
    JOIN artists a ON s.artist_id=a.artist_id
    WHERE
    s.title = %s
    AND a.name = %s
    AND s.duration = %s
GROUP BY
    s.song_id
    ,a.artist_id;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]