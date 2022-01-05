from flask import Flask, render_template, request

app = Flask(__name__)

from utils import get_settings, get_candidates, get_candidates_by_id, get_candidates_by_name


@app.route('/')
def page_index():
    settings = get_settings()
    online = settings.get("online")
    if online:
        return "Приложение работает"
    return "Приложение не работает"


@app.route('/list')
def page_list_of_candidate():

    cans = get_candidates()

    return render_template("list.html", cans=cans)


@app.route('/candidate/<int:can_id>')
def page_single_candidate(can_id):

    can = get_candidates_by_id(can_id)

    return render_template("candidate.html", can=can)


@app.route('/search')
def page_search_by_name():

    name = request.args['name']

    cans = get_candidates_by_name(name)

    cans_count = len(cans)

    return render_template("search.html", cans=cans, cans_count=cans_count)







app.run()
