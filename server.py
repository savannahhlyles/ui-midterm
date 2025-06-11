from curses import flash
from flask import Flask
from flask import render_template
from flask import request, jsonify
from flask import redirect, url_for
import statistics
import re

app = Flask(__name__)
app.secret_key = 'wat3rm3lon'

data = [
  {
    "id": "1",
    "title": "Hamilton",
    "image": "https://assets.playbill.com/playbill-covers/Hamilton-Playbill-2023-7-1_Web.jpg",
    "summary": "A musical that blends hip-hop, jazz, R&B, and Broadway styles, telling the story of American Founding Father Alexander Hamilton.",
    "genres": ["Musical", "Biography", "Historical"],
    "avg_ticket_price": "$178",
    "weekly_grosses": {
      "2025-02-23": "$1,900,135",
      "2025-02-16": "$1,921,803",
      "2025-02-09": "$1,532,750",
      "2025-02-02": "$1,655,079"
    },
    "avg_capacity": "97%",
    "critics_score": "9.7/10"
  },
  {
    "id": "2",
    "title": "The Outsiders",
    "image": "https://assets.playbill.com/playbill-covers/The-Outsiders-Playbill-2024-04-01_Web.jpg",
    "summary": "A stage adaptation of S.E. Hinton's classic novel, exploring the struggles of teenage outcasts in 1960s America.",
    "genres": ["Musical", "Drama", "Young Adult"],
    "avg_ticket_price": "$171",
    "weekly_grosses": {
      "2025-02-23": "$1,443,576",
      "2025-02-16": "$1,548,537",
      "2025-02-09": "$1,234,295",
      "2025-02-02": "$1,338,182"
    },
    "avg_capacity": "100%",
    "critics_score": "9.3/10"
  },
  {
    "id": "3",
    "title": "Wicked",
    "image": "https://assets.playbill.com/playbill-covers/738df1a5d8aff1d4e7b11c96859d1153-wicked-playbill-2017-05-web.jpg",
    "summary": "A reimagining of the classic Wizard of Oz story, focusing on the untold story of the Wicked Witch of the West.",
    "genres": ["Musical", "Fantasy", "Drama"],
    "avg_ticket_price": "$166",
    "weekly_grosses": {
      "2025-02-23": "$2,561,492",
      "2025-02-16": "$2,628,457",
      "2025-02-09": "$2,324,693",
      "2025-02-02": "$2,319,734"
    },
    "avg_capacity": "100%",
    "critics_score": "9.5/10"
  },
  {
    "id": "4",
    "title": "Maybe Happy Ending",
    "image": "https://assets.playbill.com/playbill-covers/Maybe-Happy-Ending-Playbill-2024-10-16_Web.jpg",
    "summary": "A romantic comedy that explores the complexities of relationships and finding happiness in unexpected places.",
    "genres": ["Musical", "Romantic Comedy", "Drama"],
    "avg_ticket_price": "$112",
    "weekly_grosses": {
      "2025-02-23": "$818,861",
      "2025-02-16": "$887,264",
      "2025-02-09": "$851,234",
      "2025-02-02": "$894,990"
    },
    "avg_capacity": "93%",
    "critics_score": "9.1/10"
  },
  {
    "id": "5",
    "title": "Hadestown",
    "image": "https://assets.playbill.com/playbill-covers/44eab35f14a5b7f5d2861fcf24ce69bf-hadestown-playbill-2021-09-02-web.jpg",
    "summary": "A dark and enchanting musical that reimagines the Greek myth of Orpheus and Eurydice, set in a post-apocalyptic world.",
    "genres": ["Musical", "Fantasy", "Mythology"],
    "avg_ticket_price": "$100",
    "weekly_grosses": {
      "2025-02-23": "$724,730",
      "2025-02-16": "$855,365",
      "2025-02-09": "$706,582",
      "2025-02-02": "$734,516"
    },
    "avg_capacity": "98%",
    "critics_score": "9.1/10"
  },
  {
    "id": "6",
    "title": "Gypsy",
    "image": "https://assets.playbill.com/playbill-covers/Gypsy-Playbill-2024-11-21_Web.jpg",
    "summary": "A classic Broadway musical following the rise to fame of a young girl, focusing on the relationship with her ambitious stage mother.",
    "genres": ["Musical", "Drama", "Biography"],
    "avg_ticket_price": "$118",
    "weekly_grosses": {
      "2025-02-23": "$877,294",
      "2025-02-16": "$1,476,352",
      "2025-02-09": "$1,564,611",
      "2025-02-02": "$1,690,204"
    },
    "avg_capacity": "99%",
    "critics_score": "8.9/10"
  },
  {
    "id": "7",
    "title": "Sunset Boulevard",
    "image": "https://assets.playbill.com/playbill-covers/Sunset-Boulevard-Playbill-2024-09-28_Web.jpg",
    "summary": "A musical set in Hollywood's Golden Age, following a fading star and her relationship with a screenwriter.",
    "genres": ["Musical", "Drama", "Hollywood"],
    "avg_ticket_price": "$102",
    "weekly_grosses": {
      "2025-02-23": "$1,160,383",
      "2025-02-16": "$1,296,763",
      "2025-02-09": "$1,306,183",
      "2025-02-02": "$1,431,483"
    },
    "avg_capacity": "87%",
    "critics_score": "8.8/10"
  },
  {
    "id": "8",
    "title": "Oh, Mary!",
    "image": "https://assets.playbill.com/playbill-covers/OM-web-cover-Feb.jpg",
    "summary": "A comedy musical about a woman’s adventurous journey of self-discovery, exploring themes of love, loss, and reinvention.",
    "genres": ["Musical", "Comedy", "Romance"],
    "avg_ticket_price": "$118",
    "weekly_grosses": {
      "2025-02-23": "$731,908",
      "2025-02-16": "$775,072",
      "2025-02-09": "$760,485",
      "2025-02-02": "$813,272"
    },
    "avg_capacity": "86%",
    "critics_score": "8.9/10"
  },
  {
    "id": "9",
    "title": "Cabaret",
    "image": "https://assets.playbill.com/playbill-covers/Cabaret-Playbill-2024-04-01_Web.jpg",
    "summary": "A musical set in pre-World War II Berlin, following the lives of performers and patrons at a nightclub during the rise of the Nazi regime.",
    "genres": ["Musical", "Drama", "Cabaret"],
    "avg_ticket_price": "$133",
    "weekly_grosses": {
      "2025-02-23": "$1,075,731",
      "2025-02-16": "$1,114,514",
      "2025-02-09": "$1,063,245",
      "2025-02-02": "$993,262"
    },
    "avg_capacity": "92%",
    "critics_score": "9.0/10"
  },
  {
    "id": "10",
    "title": "Death Becomes Her",
    "image": "https://assets.playbill.com/playbill-covers/Death-Becomes-Her-Playbill-2024-10-23_Web.jpg",
    "summary": "A dark comedy about two rivals who fight over the secret to eternal youth and beauty.",
    "genres": ["Musical", "Comedy", "Dark Comedy"],
    "avg_ticket_price": "$97",
    "weekly_grosses": {
      "2025-02-23": "$1,119,950",
      "2025-02-16": "$1,304,776",
      "2025-02-09": "$1,261,688",
      "2025-02-02": "$1,323,147"
    },
    "avg_capacity": "98%",
    "critics_score": "9.3/10"
  }
]

current_id = 10;

# ROUTES

@app.route('/')
def home():
    return render_template('home.html', data=data)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip().lower()
    results = []
    
    if query:
        # Define a function to highlight matched text in the summary or genres
        def highlight_text(text, query):
            # Escape special characters in query for use in regex
            query = re.escape(query)
            # Use regex to replace matching substrings with <span class="highlight">matched_text</span>
            return re.sub(f"({query})", r'<span class="highlight">\1</span>', text, flags=re.IGNORECASE)
        
        # Filter the data based on the query with highlighting in summary and genres
        results = [
            {
                'title': item['title'],  # No highlighting in the title
                'summary': highlight_text(item['summary'], query),  # Highlighted summary
                'genres': [highlight_text(genre, query) for genre in item['genres']],  # Highlighted genres
                'id': item['id']
            }
            for item in data if 
            query in item['title'].lower() or  # Match in title
            query in item['summary'].lower() or  # Match in summary
            any(query in genre.lower() for genre in item['genres'])  # Match in genres
        ]
        
    # If no results found, display a message
    no_results_message = "No results found." if not results else None

    return render_template('search_results.html', query=query, results=results, no_results_message=no_results_message)

# Helper function for view route
def find_similar_shows_by_gross(current_show, data, num_results=3):
    # Extract weekly grosses for the current show
    current_weekly_grosses = current_show['weekly_grosses']

    # Create a list to store the similarity scores
    similarity_scores = []

    for show in data:
        if show['id'] != current_show['id']:
            # Extract weekly grosses for the other show
            show_weekly_grosses = show['weekly_grosses']
            
            # Calculate the average absolute difference in weekly grosses
            total_diff = 0
            count = 0
            
            # Loop through the dates available for both shows
            for date in current_weekly_grosses.keys():
                if date in show_weekly_grosses:
                    # Extract and clean the gross values (remove "$" and commas)
                    current_gross = float(current_weekly_grosses[date].replace('$', '').replace(',', ''))
                    show_gross = float(show_weekly_grosses[date].replace('$', '').replace(',', ''))
                    
                    # Calculate the difference
                    total_diff += abs(current_gross - show_gross)
                    count += 1
            
            if count > 0:
                avg_diff = total_diff / count
            else:
                avg_diff = float('inf')  # No common dates, so no similarity

            # Store the similarity score and the show
            similarity_scores.append({
                'show': show,
                'avg_gross_diff': avg_diff
            })

    # Sort by the smallest average gross difference (more similar)
    similar_shows = sorted(similarity_scores, key=lambda x: x['avg_gross_diff'])[:num_results]
    
    return [similar_show['show'] for similar_show in similar_shows]

@app.route('/view/<int:item_id>')
def view(item_id):
    item = next((item for item in data if item['id'] == str(item_id)), None)
    
    if item:
        # Find similar shows based on weekly grosses
        similar_shows = find_similar_shows_by_gross(item, data)
        return render_template('view_item.html', item=item, similar_shows=similar_shows)
    else:
        return "Item not found", 404
    



@app.route('/add_show', methods=["POST"])
def add_show():
    global current_id

    # Extract data from the JSON request
    try:
        new_show_data = request.get_json()
        
        # Ensure the required fields are present
        title = new_show_data['title'].strip()
        image = new_show_data['image'].strip()
        summary = new_show_data['summary'].strip()
        avg_ticket_price = new_show_data['avg_ticket_price'].strip()
        genres = new_show_data['genres'].strip()
        weekly_grosses_str = new_show_data['weekly_grosses'].strip()
        avg_capacity = new_show_data['avg_capacity'].strip()
        critics_score = new_show_data['critics_score'].strip()

        # Increment current_id for the new show
        current_id += 1

        # Split the weekly grosses by ', '
        weekly_grosses_lines = weekly_grosses_str.split(', ')

        weekly_grosses = {}
        for line in weekly_grosses_lines:
            line = line.strip()
            if ":" in line:
                try:
                    # Ensure we correctly split the date and gross value
                    date, gross = line.split(":", 1)
                    date = date.strip().replace('"', '')
                    gross = gross.strip().replace('"', '')
                    gross = gross.strip()  # Remove leading/trailing spaces
                    weekly_grosses[date.strip()] = f"{gross}"
                except ValueError:
                    # Log or handle the error where the line can't be split properly
                    print(f"Skipping malformed weekly gross entry: {line}")
            else:
                print(f"Skipping malformed weekly gross entry: {line}")

        # Prepare the new show entry
        new_show = {
            'id': str(current_id),
            'title': title,
            'image': image,
            'summary': summary,
            'avg_ticket_price': avg_ticket_price,
            'genres': [genre.strip() for genre in genres.split(',')],
            'weekly_grosses': weekly_grosses,
            'avg_capacity': avg_capacity,
            'critics_score': critics_score
        }

        # Add the new show to the data list
        data.append(new_show)

        # Prepare the response as JSON
        return jsonify({"new_show_id": new_show['id'], "message": f"'{title}' added successfully!"})

    except Exception as e:
        print(f"Error processing the request: {e}")
        return jsonify({"message": "Internal Server Error", "error": str(e)}), 500

# Route to render the add new show form
@app.route('/show_form', methods=["GET"])
def show_add_form():
    return render_template('add_show.html')

# Helper function to find an item by ID
def find_item_by_id(item_id):
    return next((item for item in data if item['id'] == str(item_id)), None)

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    item = next((item for item in data if item['id'] == str(item_id)), None)
    
    if not item:
        return "Item not found", 404

    if request.method == 'POST':
        # Extract form data
        item['title'] = request.form['title']
        item['image'] = request.form['image']
        item['summary'] = request.form['summary']
        item['avg_ticket_price'] = request.form['avg_ticket_price']
        
        # Update genres
        item['genres'] = [genre.strip() for genre in request.form['genres'].split(',')]
        
        # Update weekly grosses
        weekly_grosses_str = request.form['weekly_grosses'].strip()
        
        # Use regular expression to split by commas outside of the gross value (after the colon)
        weekly_grosses_lines = re.split(r'(?<=\d),\s*(?=\d{4}-\d{2}-\d{2})', weekly_grosses_str)
        
        weekly_grosses = {}
        for line in weekly_grosses_lines:
            line = line.strip()
            if ":" in line:
                try:
                    # Ensure we correctly split the date and gross
                    date, gross = line.split(":", 1)
                    gross = gross.strip()  # Keep commas in the gross value
                    weekly_grosses[date.strip()] = gross  # Store the gross value as a string
                except ValueError:
                    # Log or handle the error where the line can't be split properly
                    print(f"Skipping malformed weekly gross entry: {line}")
            else:
                print(f"Skipping malformed weekly gross entry: {line}")
        
        # Store the updated weekly grosses in the item
        item['weekly_grosses'] = weekly_grosses
        
        # Update critics score
        item['critics_score'] = request.form['critics_score']
        
        # Update average capacity
        item['avg_capacity'] = request.form['avg_capacity']

        return redirect(url_for('view', item_id=item['id']))

    # Prepare the weekly grosses as a comma-separated string for pre-population
    weekly_grosses_str = ', '.join(['{}: {}'.format(date, gross) for date, gross in item['weekly_grosses'].items()])
    
    return render_template('edit_item.html', item=item, weekly_grosses_str=weekly_grosses_str)

if __name__ == '__main__':
    app.run(debug=True, port=5001)