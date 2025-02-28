def trilogy(year):
	movies = {
		2005 : "Batman Begins",
		2008 : "The Dark Knight",
		2012 : "The Dark Knight Rises"
	}
 
 
	if year in movies:
		print(movies[year])

	else:
		print(f"Christopher Nolan did not release a Batman movie in {year}.")
     
     
year = 2008
trilogy(year)

year = 1998
trilogy(year)