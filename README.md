# OpenClassrooms Project 3

## Help MacGyver break free !
- Clone this repo and `cd` into it
- Setup a virtualenv : `python -m venv venv`
- Activate the virtualenv :
    - Windows : `.\venv\Scripts\activate.ps1`
    - Linux / Mac : `source venv/bin/activate`
- install dependencies : `pip install -r requirements.txt`
- run the game with `python run.py`
    - (Optionnal) You can build a standalone version with cx-freeze:
        - First, install cx-Freeze `pip install cx_freeze`
        - Build the game ! `python setup.py build`


## Functionality
- [x] Only 1 level, modifiable in a text file  
- [x] Controlled with the keyboard arrow keys  
- [x] Randomized items location  
- [x] Square game window of 15 sprites width  
- [x] Retrieves items by walking on them  
- [x] Game stops if the player gets all items and finds the guard at the exit, player dies if he finds the guard without all the items  
- [x] Standalone  


## Todo / Possible improvements
- [ ] GUI / some menus
- [ ] Better graphics
- [ ] Sound effects
