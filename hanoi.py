import time

def hanoi_simulation_with_timing(n):
    """
    Simulate the Towers of Hanoi game, record the number of moves, and the time taken to complete the simulation.
    :param n: int - number of disks
    :return: tuple - (number of disks, number of moves, time taken)
    """
    moves = 0  # Counter for the number of moves

    # Inner function to simulate the moves and count them
    def move_disks(n, source, target, auxiliary):
        nonlocal moves
        if n == 1:
            moves += 1
            return
        move_disks(n-1, source, auxiliary, target)
        moves += 1
        move_disks(n-1, auxiliary, target, source)

    start_time = time.time()  # Start the timer
    move_disks(n, 'A', 'C', 'B')
    end_time = time.time()  # End the timer

    # Return a tuple containing the number of disks, number of moves, and time taken
    return n, moves, end_time - start_time

# Simulate Towers of Hanoi for 1 to 3 disks and print the results in a tabular format
results = []
for i in range(1, 35):
    results.append(hanoi_simulation_with_timing(i))

# Format and print the table
table_header = f"{'# Disks':<10}                  {'# Moves':<10}                           {'Time (s)':<10}"
print(table_header)
print('-' * len(table_header))
for result in results:
    print(f"{result[0]:<10}                       {result[1]:<10}                           {result[2]:<10.6f}")