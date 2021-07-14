-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name FROM tv_genres
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_show.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;
