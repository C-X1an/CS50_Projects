SELECT SUM(energy) / COUNT(*) FROM artists JOIN songs ON songs.artist_id = artists.id WHERE artists.name = 'Drake';
