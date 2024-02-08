This is a basic solver for the game ["Same" by Smo876](https://gitlab.com/Smo876/Same) on fdroid. This solver leverages entropy and the copious amounts of compute available on modern systems. In theory it could go forever without solving the puzzle, but it's usually almost instant.

# Method:
This solver randomly applies moves to the board until the board is entirely 1s or 0s. It repeats this procedure until it stumbles into a solution with 5 steps or less, the theoretical maximum for any given board. 

# Usage:
Just run the script and enter your board configuration.

# Notes
Though it's already really fast it's still much slower than it could be. Unless you're trying to solve thousands of these per second it won't make much difference so I'm not going to bother.
