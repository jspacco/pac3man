import pacman

'''
metarun.py runs things that look like command-line arguments
for Berkeley Python. You can leave the 'python pacman.py' part
at the beginning, or remove it, since we are not really running
from the command line.

You should comment out all lines in the file except one!
'''

#pacman.main('--layout tinyMaze --pacman GoWestAgent')
#pacman.main('-l tinyMaze -p SearchAgent -a fn=tinyMazeSearch')
#pacman.main('python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs')
pacman.main('python pacman.py -t test_cases/q2/1-bridge-grid')