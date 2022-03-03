"""
Use this code to setup the directory structure if you are starting from scratch.
"""
import os
import re
import unicodedata
import urllib

def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'3-D','3D',value, re.IGNORECASE)
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '_', value).strip('-_')

game_list = ['AceyDucey','Amazing','Animal','Awari','Bagels','Banner','Basketball','Batnum','Battle','Blackjack','Bombardment','Bombs Away','Bounce','Bowling','Boxing','Bug','Bullfight','Bullseye','Bunny','Buzzword','Calendar','Change','Checkers','Chemist','Chief','Chomp','Civil War','Combat','Craps','Cube','Depth Charge','Diamond','Dice','Digits','Even Wins','Flip Flop','Football','Fur Trader','Golf','Gomoko','Guess','Gunner','Hammurabi','Hangman','Hello','Hexapawn','Hi-Lo','High I-Q','Hockey','Horserace','Hurkle','Kinema','King','Letter','Life','Life For Two','Literature Quiz','Love','Lunar LEM Rocket','Master Mind','Math Dice','Mugwump','Name','Nicomachus','Nim','Number','One Check','Orbit','Pizza','Poetry','Poker','Queen','Reverse','Rock, Scissors, Paper','Roulette','Russian Roulette','Salvo','Sine Wave','Slalom','Slots','Splat','Stars','Stock Market','Super Star Trek','Synonym','Target','3-D Plot','3-D Tic-Tac-Toe','Tic Tactoe','Tower','Train','Trap','23 Matches','War','Weekday','Word']

text = '{0}. [{1}](src/{2}/{3}.md)'

menu = []

root_dir = os.getcwd()
src_dir = root_dir + "/src/"

for ind, file in enumerate(game_list):
    os.chdir(src_dir)
    file_label = slugify(file)
    if not os.path.isdir(file):
        os.mkdir(file)
        os.chdir(file)
        open('__init__.py', 'a').close()
        open('%s.py'%file_label, 'a').close()
        with open('%s.md'%file_label, 'a') as f:
            f.write('## {}\n\n[HOME](../../README.md)'.format(file))
    menu.append(text.format(str(ind+2), file, urllib.parse.quote(file),file_label))

os.chdir(root_dir)

with open('README.md','r') as f:
    data = f.read()
    
section = data.index('__Resource')-1

with open('README.md','w') as f:
    f.write(data[:section]+'\n'+'\n'.join(menu)+'\n<br>\n'+data[section:])
