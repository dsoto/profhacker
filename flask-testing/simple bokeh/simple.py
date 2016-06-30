'''This example demonstrates embedding a standalone Bokeh document
into a simple Flask application, with a basic HTML web form.

To view the example, run:

    python simple.py

in this directory, and navigate to:

    http://localhost:5000

'''
from __future__ import print_function

import flask

from bokeh.charts import Histogram, show
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8

import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import pandas as pd

app = flask.Flask(__name__)

colors = {
    'Black': '#000000',
    'Red':   '#FF0000',
    'Green': '#00FF00',
    'Blue':  '#0000FF',
}

def getitem(obj, item, default):
    if item not in obj:
        return default
    else:
        return obj[item]

@app.route("/")
def polynomial():
    """ Very simple embedding of a polynomial chart

    """



    # connect to google spreadsheet and get sheet
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('oauth-keyfile.json', scopes=scope)
    gc = gspread.authorize(credentials)
    responses = gc.open("Homework Histogram (Responses)")
    responses = responses.worksheet("Form Responses 1")

    # create plot html elements
    data = pd.DataFrame(responses.get_all_records())
    hist = Histogram(data, values='Question 1')
    script, div = components(hist, INLINE)



    # Grab the inputs arguments from the URL
    # This is automated by the button
    # args = flask.request.args



    # Configure resources to include BokehJS inline in the document.
    # For more details see:
    #   http://bokeh.pydata.org/en/latest/docs/reference/resources_embedding.html#bokeh-embed
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # For more details see:
    #   http://bokeh.pydata.org/en/latest/docs/user_guide/embedding.html#components
    script, div = components(hist, INLINE)
    html = flask.render_template(
        'embed.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return encode_utf8(html)

if __name__ == "__main__":
    print(__doc__)
    app.run()
