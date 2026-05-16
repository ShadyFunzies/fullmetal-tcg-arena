# Importing the PIL library
import json
import os

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import csv

# Define font
font = ImageFont.truetype("arial.ttf", 32)

text_color = (0,0,0)
cost_color = (0,0,255)
pitch_color = (0,0,255)
atk_color = (255,0,0)
def_color = (0,255,0)

set_id = input("Set ID: ")
starting_id = input("Starting ID: ")

card_dict : dict = {}

current_card_id = int(starting_id)
with open('cards.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in spamreader:

        # Open an Image
        img = Image.open('Template/card_template.png')
        
        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img)

        card_type = row[0]
        card_name = row[1]
        cost = row[2]
        pitch = row[3]
        attack = row[4] if row[4] else "0"
        defense = row[5] if row[5] else "0"
        effect = row[6]

        effect_words = effect.split(" ")
        effect = ""
        word_counter=1
        for word in effect_words:
            effect += word + ('\n' if word_counter%6 == 0 else ' ')
            word_counter+=1

        # Add Name to card
        I1.text((144, 30), card_name,font=font, fill=text_color),

        # Add Type to card
        I1.text((144, 950), card_type,font=font, fill=text_color),

        # Add Cost to card
        I1.text((18, 40), f"Pitch {pitch}",font=font, fill=pitch_color)

        # Add Pitch to card
        I1.text((600, 40), f"Cost {cost}",font=font, fill=cost_color)

        # Add Damage to card
        I1.text((28, 920), f"Atk {attack}",font=font, fill=atk_color)

        # Add Defense to card
        I1.text((608, 920), f"Def {defense}",font=font, fill=def_color)

        # Add Effect to card
        I1.multiline_text((45, 465), effect, font=font, fill=text_color)

        #img.show()
        card_img_name = card_name.replace(' ','_') + ".png"

        # Save the edited image
        img.save(f"output/cards/{card_img_name}")

        full_id = f"{set_id}_{current_card_id}"
        card_dict[full_id] = {
            "id" : full_id,
            "isToken" : False,
            "face" : {
                "front" : {
                    "name" : card_name,
                    "type" : card_type,
                    "cost" : cost,
                    "image": f"https://shadyfunzies.github.io/fullmetal-tcg-arena/cards/{card_img_name}",
                    "IsHorizontal" : False
                }
            },
            "name" : card_name,
            "type" : card_type,
            "cost" : cost,
            "Pitch" : pitch
        }

        current_card_id+=1

with open("output/jsons/cardsList.json","w") as file:
    json.dump(card_dict,file,indent=4)