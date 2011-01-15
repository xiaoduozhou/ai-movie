import imdb
i =  imdb.IMDb('sql', uri='mysql://imdb@localhost/imdb')

def get_id_movie(fn_input):
    results = i.search_movie(fn_input)
    size = len(results)
    if (size <= 0):
        return 'none'
    temp = results[0]['title']
    count = 0
    movie_list = list()
    for movie in results:
        if movie['title'] == temp:
            movie_list.append(movie)
    size = len(movie_list)
    if (size < 1):
        return 'error'
    elif (size == 1):
        return movie_list[0].movieID
    out = movie_list[0]
    votes = 0
    for movie in movie_list:
        temp = movie
        i.update(temp)
        if 'votes' in temp.keys():
            if temp['votes'] > votes:
               votes = int(temp['votes'])
               out = movie
    return out.movieID

def get_id_person(fn_input):
    results = i.search_person(fn_input)
    size = len(results)
    if (size <= 0):
        return 'none'
    temp = results[0]['name']
    count = 0
    person_list = list()
    for person in results:
        if person['name'] == temp:
            person_list.append(person)
    size = len(person_list)
    if (size < 1):
        return 'none'
    elif (size == 1):

        return person_list[0].personID
    out = person_list[0]
    for person in person_list:
        if '(I)' in person['long imdb name']:
            out = person
    return out.personID

def get_cast(movie_id):
    movie = i.get_movie(movie_id)
    if 'cast' in movie.keys():
        result = movie['cast']
        cast = list()
        for person in result:
            temp = list()
            temp.append(person['name'])
            temp.append(" as ")
            temp.append(unicode(person.currentRole))
            temp = "".join(temp)
            cast.append(temp)
        return cast
    return 'none'

def get_director(movie_id):
    movie = i.get_movie(movie_id)
    if 'director' in movie.keys():
        result = movie['director']
        director = list()
        for person in result:
            director.append(str(person['name']))
        return director
    return 'none'

def get_genre(movie_id):
    movie = i.get_movie(movie_id)
    if 'genres' in movie.keys():
        result = movie['genres']
        return result
    return 'none'

def get_plot(movie_id):
    movie = i.get_movie(movie_id)
    if 'plot' in movie.keys():
        result = movie['plot']
        if len(result) >= 1:
            return result[0]
    return 'none'

def get_rating(movie_id):
    movie = i.get_movie(movie_id)
    if 'rating' in movie.keys():
        result = movie['rating']
        return result
    return 'none'

def get_runtimes(movie_id):
    movie = i.get_movie(movie_id)
    if 'runtimes' in movie.keys():
        result = movie['runtimes']
        return result[0]
    return 'none'

def get_year(movie_id):
    movie = i.get_movie(movie_id)
    if 'year' in movie.keys():
        result = movie['year']
        return result
    return 'none'

def get_keywords(movie_id):
    movie = i.get_movie(movie_id)
    if 'keywords' in movie.keys():
        result = movie['keywords']
        return result
        return 'success'
    return 'none'

def get_production(movie_id):
    movie = i.get_movie(movie_id)
    if 'production companies' in movie.keys():
        result = movie['production companies']
        company = list()
        for item in result:
            company.append(item['name'])
        return company
    return 'none'

def get_title(movie_id):
    movie = i.get_movie(movie_id)
    if 'long imdb title' in movie.keys():
        result = movie['title']
        return result
    return 'none'

def get_biography(person_id):
    person = i.get_person(person_id)
    if 'mini biography' in person.keys():
        result = person['mini biography']
        return result
    return 'none'

def get_movies_directed(person_id):
    person = i.get_person(person_id)
    if 'director' in person.keys():
        result = person['director']
        movie = list()
        for item in result:
            movie.append(item['title'])
        return movie
    return 'none'

def get_name(person_id):
    person = i.get_person(person_id)
    if 'name' in person.keys():
        result = person['name']
        return result
    return 'none'

def get_movies_acted(person_id):
    person = i.get_person(person_id)
    if 'actor' in person.keys():
        result = person['actor']
        movie = list()
        for item in result:
            movie.append(item['title'])
        return movie
    return 'none'

def get_other_works(person_id):
    person = i.get_person(person_id)
    if 'other works' in person.keys():
        result = person['other works']
        return result
    return 'none'

def get_birthdate(person_id):
    person = i.get_person(person_id)
    if 'birth date' in person.keys():
        result = person['birth date']
        return result
    return 'none'

count = 1
while count is count:
    print ""
    choice = raw_input("Title of Movie:  ")
    result = get_id_movie(choice)
    print result
    if result is 'none' or result is 'error':
        print 'No movies were found for the given title.'
    else:
        movie = i.get_movie(result)
        print movie.keys()
        print movie['long imdb title']
    print ""
    choice = raw_input("Name of Person:  ")
    result2 = get_id_person(choice)
    print result2
    if result2 is 'none' or result2 is 'error':
        print 'No people were found for the given name.'
    else:
        person = i.get_person(result2)
        print person.keys()
        print person['long imdb name']
    print ""
    print "Testing trivia info functions on movie."
    test = get_cast(result)
    print test
    print ""
    print ""
    test = get_director(result)
    print test
    print ""
    print ""
    test = get_genre(result)
    print test
    print ""
    print ""
    test = get_plot(result)
    print test
    print ""
    print ""
    test = get_rating(result)
    print test
    print ""
    print ""
    test = get_runtimes(result)
    print test
    print ""
    print ""
    test = get_year(result)
    print test
    print ""
    print ""
    test = get_title(result)
    print test
    print ""
    print ""
    test = get_keywords(result)
    print test
    print ""
    print ""
    test = get_production(result)
    print test
    print ""
    print ""
    print "checking trivia info on Mel Gibson"
    test = get_biography(result2)
    print test
    print ""
    print ""
    test = get_name(result2)
    print test
    print ""
    print ""
    test = get_movies_acted(result2)
    print test
    print ""
    print ""
    test = get_movies_directed(result2)
    print test
    print ""
    print ""
    test = get_other_works(result2)
    print test
    print ""
    print ""
    test = get_birthdate(result2)
    print test
    print ""
    print ""
  

    
    




    
