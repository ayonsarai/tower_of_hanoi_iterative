Hanoi's Tower- Iterative

The code starts by calculating the total number of moves required to solve the Tower of Hanoi puzzle. This is done using the formula total_moves = pow(2, n) - 1, where n is the number of disks.

If the number of disks is even, the code swaps the source and auxiliary pegs. This is done to ensure that the correct pegs are used for each move.

The code then enters a loop that iterates total_moves number of times. This loop represents each move in the Tower of Hanoi puzzle.

Inside the loop, the code determines which pegs to move the disk from and to, based on the current move number. This is done using the modulus operator %. If the move number is divisible by 3 with a remainder of 1, 
the disk is moved from the source peg to the destination peg. If the remainder is 2, the disk is moved from the source peg to the auxiliary peg. If the remainder is 0, the disk is moved from the auxiliary peg to the destination peg.

After each move, the code prints the state of the pegs (source, auxiliary, and destination) to show the progress of the puzzle.

The code also defines a helper function move_disk(from_peg, to_peg) that moves the top disk from one peg to another. This function checks if the move is valid by comparing the sizes of the disks on the pegs.

Finally, the code calls the tower_of_hanoi function with a parameter of 6 to test the Tower of Hanoi algorithm with 6 disks. **this number can be changed for testing

This uses iteration and a series of conditional statements to solve the Tower of Hanoi puzzle step by step, while keeping track of the state of the pegs after each move.




Time Complexity: The time complexity of the Tower of Hanoi problem is O(2^n), where n is the number of disks. This is because for each disk, we have to make 2^n - 1 moves, 
which results in a total of (2^n - 1) + (2^n - 2) + ... + 2 + 1 moves, which simplifies to O(2^n).

Space Complexity:The space complexity of the iterative solution is O(n), where n is the number of disks. This is because we are storing the disks in three different pegs (source, auxiliary, and destination), and each peg can hold up to n disks.
However, at any given time, each disk is only on one peg, so the total space used is proportional to the number of disks.

Advantages:
Iterative solutions are often more efficient in terms of both time and space, as they avoid the overhead of function calls and stack space.
They are generally better suited for problems where the iterative nature is more straightforward and there is no need to maintain a call stack.

Disadvantages:
Iterative solutions may sometimes be less intuitive or harder to understand, especially for complex problems or those involving recursive structures like trees.
They can lead to less readable code compared to recursive solutions for certain problems.
