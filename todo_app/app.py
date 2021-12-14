from flask import Flask
from flask import render_template
from todo_app.data.session_items import get_items, add_item, get_item, remove_item
from flask import request, redirect
#from flask_bootstrap import Bootstrap
from flask import session
import requests
from todo_app.data.trello_items import get_cards


from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/', methods=['GET', 'POST'])
def index():
    items = get_cards()
    # if request.method == "POST":
    #     id = request.form.getlist("item.id")
    #     for x in id:
    #         items[int(x)-1].update({"status": "Complete"})       
    # print(items)      
    return render_template('index.html', items=items)
    ###-----------------------------------------------------
    # response = requests.get('https://api.trello.com/1/boards/61b71a4598be348b8acd7908?key=51770b20dd956e8815c8a28148814c11&token=be833b43e080328ea14ce522b45fe41a22db1e2eeb2dd5ab99169f7e1bcacdb0');
    # jsonResponse = response.json()
    # for key, value in jsonResponse.items():
    #     print(key, ":", value)
    # return render_template('index.html')
    ###------------------------------------------------------





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
