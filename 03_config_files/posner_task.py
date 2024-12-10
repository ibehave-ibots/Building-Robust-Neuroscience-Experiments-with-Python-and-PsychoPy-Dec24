import json
from random import shuffle
from psychopy.core import Clock, wait
from psychopy.visual import Window, Rect, Circle, TextStim
from psychopy.event import waitKeys

#### Define parameters ####
N_TRIALS = 10  # number of trials
P_VALID = 0.8  # probability that a cue is valid
FIX_DUR = 0.5  # duration for which fixation is displayed
CUE_DUR = 0.5  # duration for which cue is displayed
INSTRUCTIONS = """
    Welcome! \n
    When the experiment starts, you'll see a white dot and two white boxes. \n
    Fixate the white dot whenever it appears!
    After a short while, a red dot will appear in one box.
    Use the arrow keys to say that the red dot is in the left or right box.
    Respond as soon as possible! \n
    Before the red dot appears, one of the boxes will be highlighted red.
    Most of the time, the red dot will appear in the highlighted box.\n
    Press space to start the experiment!
    """

##### Create the trial sequence ####
side, valid = [], []
if N_TRIALS / 2 * P_VALID % 1 != 0:
    raise ValueError("Trials can't be evenly divided between conditions!")
for s in ["left", "right"]:
    n = int(N_TRIALS / 2)
    side += [s] * n  # side the stimulus appears ("left" or "right")
    n_valid = int(n * P_VALID)
    valid += [True] * n_valid + [False] * (n - n_valid)  # whether the cue is valid (True or False)

idx = list(range(N_TRIALS))
shuffle(idx)  # randomize the order
trials = []
for i in idx:
    trials.append([side[i], valid[i]])  # list of trials where each element is a list of 2, e.g. ["left", True]

#### Run the Experiment ####
clock = Clock()
with Window() as win:

    #### Show instructions ####
    text = TextStim(win, text=INSTRUCTIONS, height=0.07)
    text.draw()
    win.flip()
    waitKeys(keyList=["space"])

    #### Run trials ####
    count = 0
    for t in trials:
        count+=1

        # show boxes and fixation
        box_left = Rect(win, lineColor="white", pos=(-0.5, 0))
        box_right = Rect(win, lineColor="white", pos=(0.5, 0))
        fixation = Circle(win, fillColor="white", radius=0.05)
        _, _, _ = box_left.draw(), box_right.draw(), fixation.draw()
        win.flip()

        wait(FIX_DUR)

        # if stim is on the left and cue is valid OR if stim is on the right and cue is invalid
        if ( t[0] == "left" and t[1] == True) or ( t[0] == "right" and t[1] == False):
            box_left = Rect(win, lineColor="red", pos=(-0.5, 0)) # highlight the left box
            box_right = Rect(win, lineColor="white", pos=(0.5, 0))
        else:
            box_left = Rect(win, lineColor="white", pos=(-0.5, 0))
            box_right = Rect(win, lineColor="red", pos=(0.5, 0)) # highlight the right box
        _, _, _ = box_left.draw(), box_right.draw(), fixation.draw()
        win.flip()

        wait(CUE_DUR)

        # show stimulus
        box_left = Rect(win, lineColor="white", pos=(-0.5, 0))
        box_right = Rect(win, lineColor="white", pos=(0.5, 0))
        if t[0] == "left":
            stim = Circle(win, fillColor="red", pos=(-0.5, 0), radius=0.05)
        else:
            stim = Circle(win, fillColor="red", pos=(0.5, 0), radius=0.05)
        _, _, _ = box_left.draw(), box_right.draw(), stim.draw()
        win.flip()

        #### Obtain Response ####
        clock.reset() 
        keys = waitKeys(keyList=["left", "right"], timeStamped=clock) # get response
        name = keys[0][0] # key name
        rt = keys[0][1] # reaction time
        rt = round(rt, 4) # round to 4 decimals
        
        if name == t[0]:
            response = "correct"
        else:
            response = "wrong"
        print("Trial " + str(count) + ": " + response + " response with rt=" + str(rt))