This is a basic solver for the game ["Same" by Smo876](https://gitlab.com/Smo876/Same) on fdroid. This solver leverages entropy and the copious amounts of compute available on modern systems. In theory it could go forever without solving the puzzle, but it's usually almost instant. This can solve boards in both gamemode 2 and 3, though gamemode 3 takes much longer to solve.

# Method:
This solver randomly applies moves to the board until the board is entirely 0s, 1s or 2s(in mode 3). It repeats this procedure until it stumbles into a solution with 6 steps or less(12 in mode 3), the theoretical maximum for any given board. 

# Usage:
Just run the script and enter your board configuration. For mode 3 you must enter the values as their position in the rotation.

# Notes
Though it's already really fast it's still much slower than it could be. Unless you're trying to solve thousands of these per second it won't make much difference so I'm not going to bother.
