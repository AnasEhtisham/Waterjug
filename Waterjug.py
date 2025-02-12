def water_jug_problem(capacityA, capacityB, target):
    # Initialize the queue with the initial state (0, 0) and a set to track visited states
    queue = [(0, 0)]  # Using a regular list as a queue
    visited = set()
    visited.add((0, 0))

    # List to store the steps to reach the target
    steps = []

    while queue:
        currentA, currentB = queue.pop(0)  # Pop from the front of the list

        # If we reach the target in either jug, print the result
        if currentA == target or currentB == target:
            steps.append((currentA, currentB))
            print("Steps to reach the target:")
            for step in steps:
                print(step)
            print("\nTarget achieved.")
            return

        # List of possible states from the current state
        possible_states = [
            (capacityA, currentB),  # Fill jug A
            (currentA, capacityB),  # Fill jug B
            (0, currentB),          # Empty jug A
            (currentA, 0),          # Empty jug B
            (min(currentA + currentB, capacityA), currentB - (min(currentA + currentB, capacityA) - currentA)),  # Pour B to A
            (currentA - (min(currentA + currentB, capacityB) - currentB), min(currentA + currentB, capacityB)),  # Pour A to B
        ]

        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
                steps.append(state)

    # If we reach here, the target cannot be achieved
    print("No solution possible with the given jug capacities.")

def main():
    # User inputs for jug capacities and target amount
    capacityA = int(input("Enter the capacity of Jug A: "))
    capacityB = int(input("Enter the capacity of Jug B: "))
    target = int(input("Enter the desired amount of water (Output Jug): "))

    # Call the function to solve the problem
    water_jug_problem(capacityA, capacityB, target)

if __name__ == "__main__":
    main()
