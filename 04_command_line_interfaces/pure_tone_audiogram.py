from psychopy.sound import Sound
from psychopy.visual import Window, TextStim
from psychopy.event import waitKeys

###  Define Parameters ####
FREQUENCY = 1000  # frequency of the pure tone
N_REVERSALS = 5  # number of times the staircase reverses
SECS = 0.25 # duration of the tone in seconds
KEY_YES = "y" # key to press if the tone was heard
KEY_NO = "n" # key to press if the tone was not head
START_VOLUME = 0.8 # starting intensity of the tone
STEP_SIZE = 0.1 # step size of the staircase

instructions = "Press " + KEY_YES + " if you heard the tone and " + KEY_NO + " if you didn't!"
#### Run Experiment ####
with Window() as win:

    # show instructions
    text = TextStim(win, text=instructions)
    text.draw()
    win.flip()

    # create tone
    tone = Sound(value=FREQUENCY, secs=SECS, volume=START_VOLUME, stereo=False)

    # start the staircase
    reversals=[]
    direction=-1  # directon of the staircae
    while len(reversals) < N_REVERSALS:
        tone.play()
        keys = waitKeys(keyList=[KEY_NO, KEY_YES])
        if keys[0] == KEY_NO: # increase volume if key was not heard
            if direction == -1:
                direction = 1
                reversals.append(tone.volume) # append current level
            tone.setVolume(tone.volume+STEP_SIZE)
        else: # decrease volume if key was heard
            if direction == 1:
                direction = -1
                reversals.append(tone.volume) # append current level
            tone.setVolume(tone.volume-STEP_SIZE)
    
    threshold = round(sum(reversals)/len(reversals), 3) # compute threshold by averaging reversals
    print("The detection threshold for " + str(FREQUENCY) + " Hz is: " + str(threshold))
        


