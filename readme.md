# Function of fibonacci in python


The Fibonacci sequence is a mathematical sequence that follows this rule: each term is the sum of the two preceding terms. It is defined as follows:

F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for any integer n > 1

The first terms of the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The Fibonacci number is a special term in this sequence. It is identified by an index n, where n is an integer. The Fibonacci number at index n is calculated using the formula F(n) = F(n-1) + F(n-2) with the base values of F(0) = 0 and F(1) = 1.


The fibonacci function takes as input an integer n representing the index of the Fibonacci sequence we wish to calculate.

There is a basic condition that checks whether n is less than or equal to 1. If this condition is true, the function returns n. This condition is used to ensure that the recursive call stops when n is less than or equal to 1.

Otherwise, if n is greater than 1, the function returns the result of the function's recursive call for n-1 plus the function's recursive call for n-2. This step follows the definition of the Fibonacci sequence, where each number is the sum of the two preceding numbers.

The recursive call continues until the basic condition is met, i.e. when n is less than or equal to 1. At this point, all recursive calls resolve and return their result to the previous recursive call, following the definition of the Fibonacci sequence.

Finally, the final result of the Fibonacci number at index n is returned.



