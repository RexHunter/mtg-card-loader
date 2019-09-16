#!/bin/python3

import shutil
import requests
import sys, os, errno


#read list of card name from file
#parse file to remove amout of cards
#excecute pull for each card
#print cards that have problems with pulling


file_name = sys.argv[1]

#file_name = input("Enter path to file with deck: ")

with open(file_name) as file:
    lines = list(file)
    deck_name = file_name.split(".")[0]

    for line in lines:
        strings = line.split(" ")
        del strings[0]
        card_name = "".join(strings)

        URL = "https://api.scryfall.com/cards/search"
          
        PARAMS = {'q':card_name} 
              
        print("Pulling {} card.....".format(card_name))
        r = requests.get(url = URL, params = PARAMS) 

        data = r.json()

        png_img_uri=data['data'][0]['image_uris']['png']

        response = requests.get(png_img_uri, stream=True)
        
        if '//' in card_name:
            card_name = card_name.split('//')[0]
        png_name = './' + deck_name + '/' + card_name + '.png'

        if not os.path.exists('./' + deck_name):
                os.makedirs('./' + deck_name)

        with open(png_name, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
        del response
