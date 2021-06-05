#Kelly Shea

def firstPart():
    print("Go, team, go!" )
    print("Defeat your foe." )
def secondPart():
    print ("Simply the best,") 
    print("Better than the rest.")
def chorus():
    firstPart()
    secondPart()
    firstPart()
    print('')
def sing_fight_song():
    firstPart()
    print('')
    
    for index in range(2):
        chorus()
    
    firstPart()
  
sing_fight_song()
