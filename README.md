This is a basic solver for the game ["Same" by Smo876](https://gitlab.com/Smo876/Same) on fdroid. This solver leverages entropy and the copious amounts of compute available on modern systems. In theory it could go forever without solving the puzzle, but it usually takes less than a second.

# Method:
This solver randomly applies moves to the board until the board is entirely 1s or 0s. It repeats this procedure until it stumbles into a solution with 5 steps or less, the theoretical maximum for any given board. From there it's in God's hands.

# Usage:
Just run the script and enter your board configuration.

# Notes:
Everything about this solution is terrible but it works and it didn't take very long to write. I could make this at least an order of magnitude faster by ending attempts when they pass the target maximum but that would take me longer than the second it could potentially save.
