# Chapter 2.3.1: Heuristic Algorithms

This is where "Intelligence" was first approximated.

## Heuristic Search

A heuristic search is a search strategy that uses a **heuristic function** to estimate the cost of reaching the goal from a given state. The heuristic function provides guidance to the search algorithm, allowing it to `prioritize` certain paths over others based on their estimated cost.

A Heuristic is a Function:
    h(s) ~ distance to goal

It injects domain knowledge into search


### Example: A* Search Algorithm

The A* search algorithm is a popular heuristic search algorithm that combines the advantages of both `uniform-cost` and `greedy best-first` search algorithms. 

It uses a heuristic function to estimate the total cost of reaching the goal from a given state, and it prioritizes states based on this estimated cost.