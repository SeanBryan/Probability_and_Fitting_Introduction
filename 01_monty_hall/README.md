# Monte Carlo Simulation

Computer random number generators enable experiments to be simulated under ideal conditions before the experiment is performed. This is called a Monte Carlo simulation. In areas of statistics where the results of a pen and paper calculation differ depending on the approximations and assmptions that the analyst has chosen, repeatedly simulating the experiment and evaluating the results yields results without relying on a pen and paper calculation. In fact, performing a Monte Carlo simulation, then performing a pen and paper calculation that reproduces key results of the simulation, yields far more insights than either a simulation or analytic model alone.

To illustrate the concept, this code performs a Monte Carlo simulation of the Monty Hall problem. In a classic gameshow, the host presented the contestant with three doors. The host knows that behind one door is a valuable prize, a car. The host knows that behind the other two doors is a worthless prize, a goat. The host also knows which doors have which prize. The contestant is only shown the closed doors, and is asked to pick one. Since all three are the same, the contestant picks a door at random with no information. The host then opens a door that the host is sure contains a worthless prize, showing the contestant a goat. Then the key question, the host asks the contestant if they want to stick with their original choice, or switch their choice to the other still-closed door.

One pen and paper argument suggests that since the contestant did not know which door has the valuable prize, and still does not know which door has the prize even after they are shown the goat, it does not matter if the contestant switches doors. (Indeed, I used to believe this!) Another argument enumerates all possible outcomes, and after that exhaustive enumeration concludes that the contestant has higher odds of winning if they switch doors. (Indeed, I used to be very confused at these presentations, and elected not to believe them.)

The conclusive way to resolve this question, as to which pen and paper model is correct, is to play thousands of games with the no-switch strategy, then play thousands more games with the yes-switch strategy, and see which strategy yields more wins. Doing this in person would be very tedious. The idea of a Monte Carlo simulation is to program a computer to generate random game scenarios (random initial choices by the contestant) and simulate how each game would play out. Then to repeat the simulation with the other strategy, and compare.

After running this code, which does exactly that, the results printed to the screen are:

```python
Monty Hall Problem Simulation
ndoors = 3
Number of Wins while Switching: 6650 / 10000 or 66.5%
Number of Wins while NOT Switching: 3365 / 10000 or 33.65%
```

Since the details of the random number generator and especially its initialization may differ from computer to computer, the exact results may vary, but the conclusion is obvious. The player has about a 66% chance of winning if they switch, and only a 33% chance if they do not switch.

Armed with this Monte Carlo result, the decision about which pen and paper approach is more correct is obvious. (This is what convinced me, and what made me change my mind away from the naive opinion and towards the correct one.) The "it doesn't matter" model is clearly incorrect, and if the model that enumerates all outcomes yields simular results to this Monte Carlo, we will be inclined to believe the model. Indeed, the full pen and paper model says that, since opening the door takes one of the goats out of the game, the contestant has a 2/3 chance of winning if they switch. If they do not switch, they have a 1/3 chance of winning since they are not availing themselves of the location of the known goat. These pen and paper percentages match the Monte Carlo model well.

# Questions

1) Read the code carefully, does the simulation of the game make sense? Does simulating several games with the no-switch strategy and counting the results make sense? Does simulating several games with the yes-switch strategy make sense?

2) Re-run the code with a higher number of doors, say 10. Do the results make sense? Can you create a pen-and-paper model of this case? Does your pen and paper model compare well with the Monte Carlo simulation?

