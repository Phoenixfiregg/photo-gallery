import json

def load_data():
    try:
        with open('tracker.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"Movies": [],"Shows": [], "Watchlist": [] }

def save_data(data):
    with open('tracker.json', 'w') as f:
        json.dump(data, f)

def add_movie(data):
    m_name = input("Enter movie name: ")
    m_genre = input("Enter movie genre: ")
    m_status = input("Status (watched/want to watch/watching): ")
    movie = {"name": m_name, "genre": m_genre, "status": m_status}
    data["Movies"].append(movie)
    save_data(data)
    print("Movie added!")

def add_show(data):
    s_name = input("Enter show name: ")
    s_genre = input("Enter show genre: ")
    s_status = input("Enter show status (watching/completed/want to watch/dropped): ")
    season = input("Enter show season: ")
    episode = input("Enter show episode: ")
    show = {"name": s_name, "genre": s_genre, "status": s_status, "season": season, "episode": episode}
    data["Shows"].append(show)
    save_data(data)
    print("Show added!")

def rate_movie(data):
    if not data["Movies"]:
        print("(No movies yet)")
        return
    for i, movie in enumerate(data["Movies"]):
        print(f"   {i+1}.", movie["name"], "-", movie["genre"], "-", movie["status"])
    movie_number = int(input("Pick a number: "))
    movie = data["Movies"][movie_number - 1]
    m_rating = input("Enter movie rating: ")
    m_review = input("Enter movie review: ")
    movie["rating"] = m_rating
    movie["review"] = m_review
    save_data(data)
    print("Movie rating added!")

def rate_show(data):
    if not data["Shows"]:
        print("(No shows yet)")
        return
    for i, show in enumerate (data["Shows"]):
        print(f"   {i+1}.", show["name"], "-", show["genre"], "-", show["status"])
    show_number = int(input("Pick a number: "))
    show = data["Shows"][show_number - 1]
    s_rating = input("Enter show rating: ")
    s_review = input("Enter show review: ")
    show["rating"] = s_rating
    show["review"] = s_review
    save_data(data)
    print("Show rating added!")

def delete_movie(data):
    if not data["Movies"]:
        print("(No movies yet)")
        return
    for i, movie in enumerate(data["Movies"]):
        print(f"   {i + 1}.", movie["name"], "-", movie["genre"], "-", movie["status"])
    movie_number = int(input("Pick a number: "))
    data["Movies"].pop(movie_number - 1)
    save_data(data)
    print("Movie deleted!")

def delete_show(data):
    if not data["Shows"]:
        print("(No shows yet)")
        return
    for i, show in enumerate(data["Shows"]):
        print(f"   {i + 1}.", show["name"], "-", show["genre"], "-", show["status"])
    show_number = int(input("Pick a number: "))
    data["Shows"].pop(show_number - 1)
    save_data(data)
    print("Show deleted!")

def show_stats(data):
    movie_count = len(data["Movies"])
    show_count = len(data["Shows"])
    movies_watched = sum(1 for movie in data["Movies"] if movie["status"] == "watched")
    shows_watched = sum(1 for show in data["Shows"] if show["status"] == "completed")
    print(f"Total Movies: {movie_count}.",f"\nTotal Shows: {show_count}.", )
    print(f"You have watched {movies_watched} movies and {shows_watched} shows.")
    rated_movies = [movie for movie in data["Movies"] if "rating" in movie]
    rated_shows = [show for show in data["Shows"] if "rating" in show]
    if rated_movies:
        avg_movie = sum(float(movie["rating"]) for movie in rated_movies) / len(rated_movies)
        print(f"You're average rating for all your movies is {avg_movie:.2f}.")
    else:
        print("You haven't rated any movies.")

    if rated_shows:
        avg_show = sum(float(show["rating"]) for show in rated_shows) / len(rated_shows)
        print(f"\nYou're average rating for all shows is {avg_show:.2f}.")
    else:
        print("You haven't rated any shows.")

def add_to_watch_list(data):
    want_to_watch = [m for m in data["Movies"] if m["status"] == "want to watch"] + [s for s in data["Shows"] if s["status"] == "want to watch"]
    pick_watch = int(input("Pick a number: "))
    data["Watchlist"].append
    save_data(data)

def main():
    data = load_data()
    action = input("What do you want to do? (add movie/add show/rate movie/rate show/delete movie/delete show/ show stats): ").lower()
    if action == "add movie":
        add_movie(data)
    elif action == "add show":
        add_show(data)
    elif action == "rate movie":
        rate_movie(data)
    elif action == "rate show":
        rate_show(data)
    elif action == "delete movie":
        delete_movie(data)
    elif action == "delete show":
        delete_show(data)
    elif action == "show stats":
        show_stats(data)

    print('''Movie/Show tracker
    Movie
    ---------------''')
    for movie in data["Movies"]:
        print("   ", movie["name"], "-", movie["genre"], "-", movie["status"])
    if not data["Movies"]:
        print("(No movies yet)")


    print('''Shows
    ---------------''')
    for show in data["Shows"]:
        print("   ", show["name"], "-", show["genre"], "-", show["status"], "-", f"S{show['season']} E{show['episode']}")
    if not data["Shows"]:
        print("(No shows yet)")
    print('''---------------
    1.Add movie
    
    ----------------
    2.Delete movie
    
    ----------------
    3.Rate movie
    
    ----------------
    4.Add show
    
    ----------------
    5.Delete show
    
    ----------------
    6.Rate show
    
    ----------------
    7.Display stats
    
    ''')


main()