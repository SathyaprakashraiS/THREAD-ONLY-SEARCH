# THREAD-ONLY-SEARCH
Thread only search is a search algorithm i came up to overcome the problems that we face using DFS(depth first search) and BFS(Breadth first search) algorithms

## The problems encountered using BFS AND DFS
1>Takes Long time for search all nodes present
2>Cant handle edge cases
3>May result in infinite loop

So to overcome these there are Iterative Deepening and Limited Depth first search but i consider them unefficient so i came up with a idea called Thread only search
also this algorithm not only works with tree but with graph too

## Working
How the thread only search works is when a target and a start node given the algorithm searches if there is any child node for the next node moving towards targetnode and creates n threads if there are n child nodes for a node
so all nodes are checked at same time using thread and when a thread find target node it raises exception killing all thread and returns a path to the target node and ends the program

Now you may get a doubt what if the target node dosent exist ? does the thread keep running forever?
To overcome this problem i used a clock in the program so after 10 seconds(user can modify the time) the program checks if a path is identified if yes then the pah is returned else the prorgam terminates by posting the target node dosent exist

Now algorithm is not perfectly optimised its just a implementation of idea that i came with when i knew about various algorithms
Open to any suggestion and ideas to improve :)
