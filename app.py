# Flask (Server)
from flask import Flask, render_template

app = Flask(__name__)

# NewsReleases = NewsReleases()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/boundaries')
def boundaries():
    return render_template('boundaries.html')

@app.route('/articles')
def news_releases():
    # Assuming NewsReleases is defined elsewhere in your code
    return render_template('newsReleases.html', newsReleases=NewsReleases)

@app.route('/article/<string:id>/')
def newsRelease(id):
    return render_template('newsRelease.html', id=id)

@app.route('/parks')
def parks():
    return render_template('parks.html')

@app.route('/visits')
def visits():
    return render_template('visits.html')

if __name__ == '__main__':
    app.run(debug=True)
