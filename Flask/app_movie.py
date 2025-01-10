# Import Flask and related functions for building a web application.
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application instance.
app = Flask(__name__)

# Initial list of Indian movies
movies_list = [
     # List of dictionaries, each representing a movie with details like ID, title, director, year, and review.
    {"id": 1, "title": "Sholay", "director": "Ramesh Sippy", "year": 1975, "review": "One of the timeless classic in Indian cinema, often regarded as one of the greatest films ever made. This action-adventure film tells the story of two criminals, Jai and Veeru, hired by a retired police officer to capture the notorious dacoit Gabbar Singh. The movie is a perfect blend of action, drama, comedy, and romance, with iconic characters like the fearless Thakur, the quirky Basanti, and the menacing Gabbar"},
    {"id": 2, "title": "Dangal", "director": "Nitesh Tiwari", "year": 2016, "review": "An inspiring tale of a father's dedication to his daughters' wrestling careers. The film portrays a father's determination to break societal norms and empower his daughters to achieve their dreams. With its emotionally charged performances and powerful narrative, Dangal highlights themes of gender equality, resilience, and family values."},
    {"id": 3, "title": "Lagaan", "director": "Ashutosh Gowariker", "year": 2001, "review": "A gripping story of villagers challenging the British in a cricket match. The story revolves around a group of villagers who, led by Bhuvan, challenge the British officers to a cricket match to avoid paying an oppressive tax. The film masterfully combines sports, patriotism, and drama, showcasing the villagers' unity and determination."},
    {"id": 4, "title": "Kabhi Khushi Kabhie Gham", "director": "Karan Johar", "year": 2001, "review": "A family drama that explores relationships and values. The film centers on the Raichand family and the rift caused by a father's disapproval of his son's choice of life partner. With its star-studded cast, opulent sets, and memorable music, K3G strikes a chord with audiences."},
    {"id": 5, "title": "Taare Zameen Par", "director": "Aamir Khan", "year": 2007, "review": "A touching story about a dyslexic child's journey and his teacher's efforts. The story revolves around Ishaan, a dyslexic child misunderstood by his family and teachers, and his art teacher, Ram Shankar Nikumbh, who helps him rediscover his potential. The film is a moving portrayal of empathy, understanding, and the transformative power of education."},
    {"id": 6, "title": "Gully Boy", "director": "Zoya Akhtar", "year": 2019, "review": "A story of a young man from the slums who dreams of becoming a rapper. The film delves into themes of self-expression, social inequality, and the pursuit of dreams against all odds. With its authentic portrayal of the underground hip-hop scene in India, powerful performances, and catchy music,"},
    {"id": 7, "title": "Mughal-e-Azam", "director": "K. Asif", "year": 1960, "review": "An epic historical romance between Prince Salim and Anarkali. Set against the backdrop of the Mughal era, the film is a visual and emotional extravaganza. Its grand sets, exquisite costumes, and timeless music, including the iconic song 'Pyar Kiya To Darna Kya', make it a cinematic gem."},
]

# Route for displaying the list of movies.
@app.route('/')
def list_movies():
    return render_template('list_movies.html', movies=movies_list)

# Route for adding a new movie.
@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':

        # If the form is submitted (POST request), extract data from the form.
        data = request.form
        new_movie = {
            "id": movies_list[-1]["id"] + 1 if movies_list else 1,
            "title": data.get("title"),
            "director": data.get("director"),
            "year": int(data.get("year")),
            "review": data.get("review")
        }

        # Add the new movie to the list.
        movies_list.append(new_movie)
        
        # Redirect to the main movie list after adding.
        return redirect(url_for('list_movies'))    
    return render_template('add_movie.html')

# Route for updating an existing movie based on its ID.
@app.route('/update/<int:movie_id>', methods=['GET', 'POST'])
def update_movie(movie_id):
    movie = None
    for m in movies_list:
        if m["id"] == movie_id:
            movie = m
            break
    if not movie:
        return "Movie not found", 404

    if request.method == 'POST':
        # If the form is submitted (POST request), update the movie details.
        data = request.form
        movie.update({
            "title": data.get("title", movie["title"]),
            "director": data.get("director", movie["director"]),
            "year": int(data.get("year", movie["year"])),
            "review": data.get("review", movie["review"])
        })
        
        # Redirect to the main movie list after updating.
        return redirect(url_for('list_movies'))   

    return render_template('update_movie.html', movie=movie)

# Route for deleting a movie based on its ID.
@app.route('/delete/<int:movie_id>', methods=['GET', 'POST'])
def delete_movie(movie_id):

    # Declare `movies_list` as global to modify it.
    global movies_list

    # Filter out the movie with the matching ID.
    movies_list = [movie for movie in movies_list if movie["id"] != movie_id]
    
    # Reassign IDs to keep them in serial order
    for index, movie in enumerate(movies_list, start=1):
        movie["id"] = index
    return redirect(url_for('list_movies'))

# Run the Flask application on port 5000 with debugging enabled.
if __name__ == "__main__":
    app.run(port=5000, debug=True)
