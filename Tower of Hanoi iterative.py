# Sarai Ayon
# 5/7/2024
# CS 240 Data Structures and Algorithms
# Miterm Project - Tower of Hanoi iterative 


def tower_of_hanoi(n):
    # Initialize the source, auxiliary, and destination pegs
    source = [i for i in reversed(range(1, n+1))]
    auxiliary = []
    destination = []

    # Calculate the total number of moves required
    total_moves = pow(2, n) - 1

    # If the number of disks is even, swap the source and auxiliary pegs
    if n % 2 == 0:
        source, auxiliary = auxiliary, source

    # Perform the Tower of Hanoi algorithm iteratively
    for i in range(1, total_moves + 1):
        if i % 3 == 1:
            move_disk(source, destination)
        elif i % 3 == 2:
            move_disk(source, auxiliary)
        elif i % 3 == 0:
            move_disk(auxiliary, destination)

        # Print the state of the pegs after each move
        print('Source:', source)
        print('Auxiliary:', auxiliary)
        print('Destination:', destination)
        print('---')

def move_disk(from_peg, to_peg):
    # Move the top disk from the "from_peg" to the "to_peg" if it is a valid move
    if len(from_peg) > 0 and (len(to_peg) == 0 or to_peg[-1] > from_peg[-1]):
        to_peg.append(from_peg.pop())
    elif len(to_peg) > 0 and (len(from_peg) == 0 or from_peg[-1] > to_peg[-1]):
        from_peg.append(to_peg.pop())

# Test the tower_of_hanoi function with 6 disks
tower_of_hanoi(6)

