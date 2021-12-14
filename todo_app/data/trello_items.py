import json
import requests
import os

def get_cards():
    """
    Fetches all saved cards from the board.

    Returns:
        list: The list of card items. Need to get to cards[name]. jsonAPI is a list apparently and .items() isn't functioning.
    """
    # payload = { 'key' : os.getenv('KEY') , 'token' : os.getenv('TOKEN'), 'board' : os.getenv('BOARD_ID'), 'cards' : 'open'}
    # API_Call = requests.get('https://api.trello.com/1/boards/', params=payload)

    API_Call = requests.get('https://api.trello.com/1/boards/61b71a4598be348b8acd7908/lists/?key=51770b20dd956e8815c8a28148814c11&token=be833b43e080328ea14ce522b45fe41a22db1e2eeb2dd5ab99169f7e1bcacdb0&cards=open');

    jsonAPI = API_Call.json()
    print(type(jsonAPI))
    for key, value in jsonAPI.items():
        if key == 'cards':
          print(key, ":", value)
    
    return jsonAPI

def add_card():

    """
    Adds a new card with the specified title to the list.

    Args:
        title: The title of the card.

    Returns:
        item: The saved card.
    """

    name_of_card = "Input from html here"
    payload = { 'key' : os.getenv('KEY') , 'token' : os.getenv('TOKEN'), 'idList' : '61b71a556e218d506a196867', 'name' : name_of_card}
    API_Call = requests.post('https://api.trello.com/1/cards/', params=payload)

    # Determine the ID for the item based on that of the previously added item - Not sure if this is needed for Trello
    #id = items[-1]['id'] + 1 if items else 0

    #item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # Add the item to the list
    #items.append(item)
    #session['items'] = items

    #return item