from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    asteroids = []
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        api_key = ''
        url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            asteroids = data.get('near_earth_objects', [])
    return render_template('index.html', asteroids=asteroids)

if __name__ == '__main__':
    app.run(debug=True)
