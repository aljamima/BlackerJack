
# Blacker Jack Card Counter

Blacker Jack is a card counting app that will display the top 3 card counting methods. It will allow you to type in cards as they are being played, to get an idea of what your True Count would be for Omega Halves, Wong, and Hi-Lo counting methods. There is also a graphical representation of the Hi-Lo count as it progresses through your game, as well as a chart that displays the running total of each card value remaining in the deck(s).

Note: The selector for counting methods is useless now and will be removed shortly.
## Motivation

I have been interested in card counting and wanted an exercise to familiarize myself with counting techniques and strategies. This project has been the motivation for me to keep learning and testing new strategies while also playing games and having fun!
## Coming Soon:

NEED TO ADD MORE ERROR HANDLING AND GRACEFUL SHUTDOWNS!

Will add a section for bet spread.

Will remove useless counting method selector.

Fix bug where long entries of >4 or 5 chars does not wrap inside card history box.

~~Fix allowing "T" -or- 10 for 10's.~~

Fix bug where text is not ALWAYS cleared on invalid input. 

~~Add history to show previously entered card values.~~

~~Add audible alert when no input was given.~~

~~Add input validation.~~

~~Discard anything invalid.~~

~~Allowing input without spaces or any delimiter.~~

~~Add counting methods so we can see multiple counts at the same time.~~


## Built With:
    Python 3
    PyQt6
    Qt Designer

### Install Dependencies:
    pip install PyQt6 matplotlib pygame
    
    (pygame dep will likely be removed soon.)

## Installation

Simply download and run the executable for your platform.
### Usage
![Sample GUI](https://github.com/aljamima/BlackerJack/blob/main/screenshot.png?raw=true)
### Usage:
To use this app, you will select the number of decks you are playing with. Then just type in the card values as they are dealt. You do NOT need to enter the suit, as this doesn't really affect the count at all. Any invalid inputs will be discarded. You can enter card values for high cards (A,K,Q,J,T) in upper or lower case. You can separate by spaces or commas if you choose, but no delimiter is actually required. Anytime the cards are reshuffled, just hit the shuffle button to start over.

There are two charts. One on the right will display the Hi-Lo count as you progress through the game. The chart on the bottom is useful for a quick visual as to how many of each card value is left in the deck.




## Credits
This project is inspired by another project I found on Github. Although it's been refactored and upgraded to PyQt6, I used this project as a starting point.

Credit due to: https://github.com/PrintName/BlackjackCardCounter
Who also credits: countingedge.com
