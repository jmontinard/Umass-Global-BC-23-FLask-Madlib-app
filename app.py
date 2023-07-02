from flask import Flask, request, render_template
from random import choice, sample
# from stories import story 
from stories import Story

from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

story_temps = [
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
    """This weekend I am going to {place} with my {adjective} {noun}.
        we are going to {verb} {plural_noun}.""",
    """It was about {adjective} ago when {noun} came to the {place} in a {adjective}. 
       At this {place} we {verb} that there are a lot of{plural_noun} here."""
]

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)


@app.route('/')
def index():
    """Return homepage. with the selecation of story templates"""
    
    return render_template('select-story-temp.html', templates = story_temps)


@app.route('/form')
def show_form():
    """Return homepage."""
    template = request.args["story-templates"]
    story.template = template
    input_prompts = story.prompts
    
    return render_template("form.html", prompts = input_prompts, temp = template)


@app.route('/story')
def show_story():
    place= request.args['place']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    plural_noun = request.args['plural_noun']
    madlib = {
        "place": place,
        "noun": noun,
        "verb": verb,
        "adjective": adjective,
        "plural_noun": plural_noun
    }
    
    your_madlib = story.generate(madlib)

    return render_template('story.html', your_story = your_madlib)
