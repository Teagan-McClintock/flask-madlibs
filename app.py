from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def show_question_form():
    """Generate and show form to ask for all prompts"""

    prompts = silly_story.prompts
    return render_template("questions.html", prompts=prompts)

@app.get("/results")
def show_story():
    """Show story result."""

    story_text = silly_story.get_result_text(request.args)
    return render_template("results.html", story_text=story_text)

