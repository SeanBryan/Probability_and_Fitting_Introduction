import random

# heavily inspired by: https://scipython.com/book2/chapter-4-the-core-python-language-ii/examples/the-monty-hall-problem/

def run_trial(contestant_chooses_to_switch_doors=True, ndoors=3):
    '''
    run a single trial of the Monty Hall problem
    
    in this game show, the contestant is presented with ndoors=3 doors
    the contestant does not know what is behind any of the doors
    so the contestant picks a door at random

    the gameshow host knows that there is one valuable prize, the car, behind door #1
    the gameshow host also knows that all other doors have a worthless prize, the goat
    the gameshow host opens one of the doors that the contestant has not chosen that has a goat
    and shows the contestant that this door has the goat
    
    the question: does the contestant stick with their original choice, or do they switch to the other door?

    after the contestant makes their decision, they get the prize behind their final-answer door
    '''

    # have the contestant pick a random door out of the nominally 3 ndoors available
    chosen_door = random.randint(1, ndoors)

    # have the host reveal a goat
    # this would entail the host opening door 2
    # or opening door 3 if the contestant already chose door 2
    revealed_door = 3 if chosen_door==2 else 2

    # if the contestant chooses to switch doors
    if contestant_chooses_to_switch_doors:
        # find which door(/s) is(/are) available for the contestant to switch to
        # excluding their initially-selected door
        # and excluding the door the host just revealed
        available_doors = [dnum for dnum in range(1,ndoors+1)
                                if dnum not in (chosen_door, revealed_door)]
        
        # have the contestant randomly choose from the available door(s)
        chosen_door = random.choice(available_doors)

    # determine if the contestant won the car
    # they win if their final answer chosen door is door #1
    return chosen_door == 1

# choose the number of doors
# (nominally 3)
ndoors = 3

# choose the number of experiments to conduct
Nexperiments = 10000

# count the number of wins if the contestant
# chooses to stay with their original choice
Nwins_no_switch = 0
# count the number of wins if they switch
Nwins_with_switch = 0
# for each of the N experiments
for i in range(Nexperiments):
    # simulate a game in the case where the contestant chooses to switch
    result = run_trial(contestant_chooses_to_switch_doors=True, ndoors=ndoors)
    # if they win the car
    if result:
        # count it
        Nwins_with_switch += 1
    
    # simulate a game in the case where the contestant chooses to not switch
    result = run_trial(contestant_chooses_to_switch_doors=False, ndoors=ndoors)
    # if they win the car
    if result:
        # count it
        Nwins_no_switch += 1

# print out the results to the user
print('Monty Hall Problem Simulation')
print('ndoors = '+str(ndoors))
print('Number of Wins while Switching: '+str(Nwins_with_switch)+\
                                       ' / '+\
                                       str(Nexperiments)+\
                                       ' or '+str(100*Nwins_with_switch/Nexperiments)[0:6]+'%')
print('Number of Wins while NOT Switching: '+str(Nwins_no_switch)+\
                                             ' / '+\
                                             str(Nexperiments)+\
                                             ' or '+str(100*Nwins_no_switch/Nexperiments)[0:6]+'%')