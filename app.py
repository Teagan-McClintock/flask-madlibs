from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import story_dict


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def show_story_selector():
    story_titles = story_dict.keys()
    return render_template("pick_story.html", story_titles=story_titles)


@app.get("/questions")
def show_question_form():
    """Generate and show form to ask for all prompts"""

    # for story in story_list:
    #     if story.title = form_answer:
    #         current_story = story

    story_title = request.args["stories"]

    prompts = story_dict[story_title].prompts
    return render_template("questions.html", prompts=prompts
                           , story_title = story_title)

@app.get("/results/<story_title>")
def show_story(story_title):
    """Show story result."""

    story_text = story_dict[story_title].get_result_text(request.args)
    return render_template("results.html", story_text=story_text)

