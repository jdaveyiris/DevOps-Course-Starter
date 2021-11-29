from flask import Flask
from flask import render_template
from todo_app.data.session_items import save_item, get_items, add_item
from flask import request, redirect

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def adding():

    if request.method == "POST":

        item = request.form.get("item")
        add_item(item)
        return redirect('/')

    return render_template('additem.html')
