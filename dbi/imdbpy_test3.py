import nltk
import imdb
i =  imdb.IMDb('sql', uri='mysql://imdb@localhost/imdb')
global current
current = i.get_movie('426722')
i.update(current)

def find_movie(fn_input, current):
    result = i.search_movie(fn_input)
    if len(result) > 0:
        length = len(result)
        count = 0
        #max_count = min(length,5)
        user_input = raw_input("How many of the %d movies do you want listed (Give #)?  "%(length))
        max_count = int(user_input)
        while count < max_count:
            print count + 1, '->', result[count]['long imdb title']
            count = count + 1
        user_input = raw_input("Want any of these(0 to pass)?  ")
        if (int(user_input) > max_count) or (int(user_input) < 0):
            print 'Not a valid selection!'
            return current
        elif int(user_input) is 0:
            return current
        movie = result[int(user_input) - 1]
        print"Movie ID =", movie.movieID
        i.update(movie)
        #print movie['title']
        print movie.keys()
        print movie.summary()
        #current = movie
        return movie
    else:
        print 'No movies found, sorry.'
        return current

def find_person(fn_input, current):
    result = i.search_person(fn_input)
    if len(result) > 0:
        length = len(result)
        count = 0
        #max_count = min(length,5)
        user_input = raw_input("How many of the %d people do you want listed (Give #)?  "%(length))
        max_count = int(user_input)
        while count < max_count:
            print count + 1, '->', result[count]['long imdb name']
            count = count + 1
        user_input = raw_input("Want any of these(0 to pass)?  ")
        if (int(user_input) > max_count) or (int(user_input) < 0):
            print 'Not a valid selection!'
            return current
        elif int(user_input) is 0:
            return current
        person = result[int(user_input) - 1]
        print "Person ID =",person.personID
        i.update(person)
        print person.keys()
        #print person['name']
        print person.summary()
        #current = person
        return person
    else:
        print 'No people listed, sorry.'
        return current

def find_keyword(fn_input, current):
    result = i.get_keyword(fn_input)
    if len(result) > 0:
        length = len(result)
        count = 0
        #max_count = min(length,5)
        user_input = raw_input("How many of the %d movies do you want listed (Give #)?  "%(length))
        max_count = int(user_input)
        while count < max_count:
            print count + 1, '->', result[count]['long imdb title']
            count = count + 1
        user_input = raw_input("Want any of these(0 to pass)?  ")
        if (int(user_input) > max_count) or (int(user_input) < 0):
            print 'Not a valid selection!'
            return current
        elif int(user_input) is 0:
            return current
        movie = result[int(user_input) - 1]
        i.update(movie)
        #print movie['title']
        print movie.summary()
        #current = movie
        return movie
    else:
        print 'No movies for that keyword, sorry.'
        return current

def find_character(fn_input, current):
    result = i.search_character(fn_input)
    if len(result) > 0:
        length = len(result)
        count = 0
        #max_count = min(length,5)
        user_input = raw_input("How many of the %d characters do you want listed (Give #)?  "%(length))
        max_count = int(user_input)
        while count < max_count:
            print count + 1, '->', result[count]['long imdb name']
            count = count + 1
        user_input = raw_input("Want any of these(0 to pass)?  ")
        if (int(user_input) > max_count) or (int(user_input) < 0):
            print 'Not a valid selection!'
            return current
        elif int(user_input) is 0:
            return current
        character = result[int(user_input) - 1]
        print "Character ID =",character.characterID
        i.update(character)
        print character.summary()
        print character.keys()
        return character
    else:
        print 'No characters found, sorry.'
        return current

def find_company(fn_input, current):
    result = i.search_company(fn_input)
    if len(result) > 0:
        length = len(result)
        count = 0
        #max_count = min(length,5)
        user_input = raw_input("How many of the %d companies do you want listed (Give #)?  "%(length))
        max_count = int(user_input)
        while count < max_count:
            print count + 1, '->', result[count]['long imdb name']
            count = count + 1
        user_input = raw_input("Want any of these(0 to pass)?  ")
        if (int(user_input) > max_count) or (int(user_input) < 0):
            print 'Not a valid selection!'
            return current
        elif int(user_input) is 0:
            return current
        company = result[int(user_input) - 1]
        print "Company ID =",company.companyID
        i.update(company)
        print company.keys()
        print company.summary()
        return company
    else:
        print 'No company found, sorry.'
        return current

#def get_director(movie):
#    if 'director' in movie.keys():
#        result = movie['director']
#        if len(result) > 0:
#            length = len(result)
#            count = 0
#            max_count = min(length,5)
#            while count < max_count:
#                print count + 1, '->', result[count]['long imdb name']
#                count = count + 1
#            user_input = raw_input("Want any of these(1-%d)?  "%(max_count))
#            if int(user_input) <= max_count:
#                person = result[int(user_input) - 1]
#                i.update(person)
#                print person.summary()
#                return person
#            else:
#                print 'Not a valid selection.'
#                return movie
#        else:
#            print 'No people listed, sorry.'
#            return movie
#    else:
#        print 'No directors listed for selection!'
#        return movie

#def get_cast(movie):
#    if 'cast' in movie.keys():
#        result = movie['cast']
#        if len(result) > 0:
#            length = len(result)
#            count = 0
#            max_count = min(length,5)
#            while count < max_count:
#                print count + 1, '->', result[count]['long imdb name']
#                count = count + 1
#            user_input = raw_input("Want any of these(1-%d)?  "%(max_count))
#            if int(user_input) <= max_count:
#                person = result[int(user_input) - 1]
#                i.update(person)
#                print person.summary()
#                return person
#            else:
#                print 'Not a valid selection.'
#                return movie
#        else:
#            print 'No people listed, sorry.'
#            return movie
#    else:
#        print 'No cast members listed for selection!'
#        return movie

def get_director(movie):
    if 'director' in movie.keys():
        result = movie['director']
        for director in result:
            print "("+director['long imdb name']+")",
        print ""
    else:
        print "No directors listed for selection!"

def get_cast(movie):
    if 'cast' in movie.keys():
        result = movie['cast']
        length = len(result)
        user_input = raw_input("How many of the %d cast members do you want listed (Give #)?  "%(length))
        count = 0
        user_input = int(user_input)
        for cast in result:
            if count >= user_input:
                break
            print cast['long imdb name'],"as",cast.currentRole
            count = count + 1
        print ""
    else:
        print "No cast members listed for selection!"

def get_genre(movie):
    if 'genres' in movie.keys():
        result = movie['genres']
        for genre in result:
            print genre,
        print ""
    else:
        print "No genres listed for selection!"

def get_plot(movie):
    if 'plot' in movie.keys():
        result = movie['plot']
        count = 1
        for plot in result:
            print "Plot Summary %d: "%(count),plot
            count = count + 1
        print ""
    else:
        print "No plot listed for selection!"

def get_actor_filmography(person):
    if 'actor' in person.keys():
        result = person['actor']
        length = len(result)
        user_input = raw_input("How many of the %d movies do you want listed (Give #)?  "%(length))
        count = 0
        user_input = int(user_input)
        for actor in result:
            if count >= user_input:
                break
            print actor['long imdb title']
            count = count + 1
        print ""
    else:
        print "No filmography listed for selection!"

def get_character_filmography(character):
    if 'filmography' in character.keys():
        result = character['filmography']
        length = len(result)
        user_input = raw_input("How many of the %d movies do you want listed (Give #)?  "%(length))
        count = 0
        user_input = int(user_input)
        for actor in result:
            if count >= user_input:
                break
            print actor['long imdb title']
        print ""
    else:
        print "No filmography listed for selection!"

def get_rating(movie):
    if 'rating' in movie.keys():
        result = movie['rating']
        print "Hmm...on a scale from 1-10, I'd say",result
    else:
        print "No rating listed for selection!"

def get_runtimes(movie):
    if 'runtimes' in movie.keys():
        result = movie['runtimes']
        for runtimes in result:
            print runtimes,"minutes",
        print ""
    else:
        print "No runtimes listed for selection!"

def get_mpaa(movie):
    print movie.keys()
    if 'mpaa' in movie.keys():
        result = movie['mpaa']
        for mpaa in result:
            print mpaa,
        print ""
    else:
        print "No mpaa rating listed for selection!"

def actor_keyword(current):
    person_input = raw_input("Give me an actor!  ")
    people = i.search_person(person_input)
    if len(people) > 0:
        length = len(people)
        count = 0
        max_count = min(length,5)
        while count < max_count:
            print count + 1, '->', people[count]['long imdb name']
            count = count + 1
        user_input = raw_input("Want any of these(1-%d)?  "%(max_count))
        person = people[int(user_input) - 1]
        i.update(person)
        if 'actor' in person.keys():
            list1 = person['actor']
            #print list1
            key_input = raw_input("Give me a keyword!  ")
            list2 = i.get_keyword(key_input)
            #print list2
            set1 = set(list1)
            set2 = set(list2)
            set3 = set1 & set2
            list3 = list(set3)
            #print ""
            #print "size of actor movie list: ", len(list1)
            #print "size of keyword movie list: ", len(list2)
            #print list3
            if len(list3) > 0:
                length = len(list3)
                count = 0
                max_count = length
                while count < max_count:
                    print count + 1, '->', list3[count]['long imdb title']
                    count = count + 1
                user_input = raw_input("Want any of these(1-%d)?  "%(max_count))
                movie = list3[int(user_input) - 1]        
                i.update(movie)
                print movie.summary()
                return movie
            else:
                print 'No similar movies for given actor/keyword combo!'
                return current
        else:
            print 'No movies found for chosen actor'
            return current
    else:
        print 'No actor found.'
        return current

count = 1
print "Current selection defaulted to " + current['long imdb title']
print i.get_movie('479849')['title']
while count is count:
    print ""
    choice = raw_input("#1-9 // 1. Find Movie, 2. Find Person, 3. Find Keyword, 4. Find Character, 5. Find Company,"
    +" 6. Get Director(s), 7. Get Cast, 8. Get Genre, 9. Get Plot, 10. Get Actor's Filmography, 11. Get Character Filmography,"
    +" 12. Get Movie Rating, 13. Get Runtimes, 14. Get MPAA Rating, 15. Actor & Keyword Search: ")                
    choice = int(choice)
    if choice is 1:
        name = raw_input("Title?  ")
        current = find_movie(name,current)
    if choice is 2:
        name = raw_input("Name?  ")
        current = find_person(name,current)
    if choice is 3:
        name = raw_input("Keyword?  ")
        current = find_keyword(name,current)
    if choice is 4:
        name = raw_input("Name?  ")
        current = find_character(name,current)
    if choice is 5:
        name = raw_input("Name?  ")
        current = find_company(name,current)
    if choice is 6:
        get_director(current)
    if choice is 7:
        get_cast(current)
    if choice is 8:
        get_genre(current)
    if choice is 9:
        get_plot(current)
    if choice is 10:
        get_actor_filmography(current)
    if choice is 11:
        get_character_filmography(current)
    if choice is 12:
        get_rating(current)
    if choice is 13:
        get_runtimes(current)
    if choice is 14:
        get_mpaa(current)
    if choice is 15:
        current = actor_keyword(current)
    print ""
    if 'long imdb name' in current.keys():
        print "Current selection is: " + current['long imdb name']
    elif 'long imdb title' in current.keys():
        print "Current selection is: " + current['long imdb title']
    else:
        print "Current selection has no name/title!"






