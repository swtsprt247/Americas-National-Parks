# Flask (Server)
from flask import Flask, render_template, request
# [START app]
import logging
#################################################
# Flask Setup
#################################################
app = Flask (__name__)

# Add any libraries installed in thes "lib" folder.



@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/boundaries')
def boundaries():
    return render_template('boundaries.html')

# @app.route('/articles')
# def newsReleases ():
#     return render_template('newsReleases.html', newsReleases = NewsReleases)

# @app.route('/article/<string:id>/')
# def newsRelease (id):
#     return render_template('newsRelease.html', id=id)

@app.route('/parks')
def parks():
    return render_template('parks.html')



@app.route('/visits')
def visits():
    return render_template('visits.html')












@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
