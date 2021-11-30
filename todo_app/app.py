from flask import Flask
from flask import render_template
from todo_app.data.session_items import get_items, add_item, get_item, remove_item
from flask import request, redirect
#from flask_bootstrap import Bootstrap
from flask import session


from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/', methods=['GET', 'POST'])
def index():
    items = get_items()
    if request.method == "POST":
        id = request.form.getlist("item.id")
        for x in id:
            items[int(x)-1].update({"status": "Complete"})
            
    print(items)      

    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def adding():
    if request.method == "POST":
        item = request.form.get("item")
        add_item(item)
        return redirect('/')

    return render_template('additem.html')

@app.route('/remove', methods=['GET', 'POST'])
def removing():
    items = get_items()
    if request.method == "POST":
        id = request.form.getlist("item.id")
        for x in id:
            print(x)
            itemToRemove = get_item(int(x))
            remove_item(itemToRemove)
    print(items)
        
    
    return render_template('removeitem.html', items=items)
