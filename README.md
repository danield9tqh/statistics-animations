## Motivation
I created these animation to better understand statistical primitives (variance, covariance etc.). Hopefully it makes it to a point where it is helpful for others to understand them as well
 
## Setup
### Install Manim
Manim is the rendering library used to create the animations and documentation and installation instructions can be found [here](https://github.com/ManimCommunity/manim/#installation).

### Run Animation
The SingleDiceRollDistribution animation represents the probability distribution of rolling a single dice up to 10000 times. To generate and run the animation run the following:
```
manim -p -ql src/animations.py SingleDiceRollDistribution
```
