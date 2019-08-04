#!/user/bin/env python

from dicetable import DiceTable
import os
from PIL import Image, ImageDraw, ImageFont
import sys


output_path = "/Users/mikec/Dropbox/games/RPG campaigns/50 fathoms/dbx-bestiary/"
white = (255, 255, 255)
black = (0, 0, 0)

fantasy_bg = {"img": 'scroll-v.png', 
                "font": '/Library/Fonts/Arial.ttf', 
                "size": 12,
                "color": black,
                "offset": (40, 70), 
                "wrap": 36}

die_rolls = [7, 3, 5]
result1 = DiceTable.roll_on_tables('injury', die_rolls,
    show_table=True, show_roll=True)
print(result1)

# die_rolls = [6 ,2, 1]
# result2 = DiceTable.roll_on_tables('insult-pt1', die_rolls,
#     show_table=False, show_roll=False)
# print(result2)

background = fantasy_bg
try:
    result_bg = Image.open(background["img"])
except:
    print("Unable to load background image")
    sys.exit(1)
font = ImageFont.truetype(background["font"], size=background["size"])

idraw = ImageDraw.Draw(result_bg)
idraw.text((40, 70), result1, font=font, fill=background["color"])
result_bg.save(os.path.join(output_path,"table-minion.png"))
