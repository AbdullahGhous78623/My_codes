class Knapsack:
    """
    A class to solve the 0/1 Knapsack Problem using recursion and dynamic programming.
    """

    def __init__(self, weights, values, capacity):
        """
        Initialize the Knapsack problem with weights, values, and capacity.

        :param weights: List of item weights
        :param values: List of item values
        :param capacity: Maximum capacity of the knapsack
        """
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.n = len(weights)
        self.dp = [[-1 for _ in range(capacity + 1)] for _ in range(self.n + 1)]

    def recursive_knapsack(self, n, capacity):
        """
        Solve the Knapsack problem using recursion.

        :param n: Number of items
        :param capacity: Remaining capacity of the knapsack
        :return: Maximum value achievable
        """
        if n == 0 or capacity == 0:
            return 0
        if self.weights[n - 1] > capacity:
            return self.recursive_knapsack(n - 1, capacity)
        else:
            return max(
                self.values[n - 1] + self.recursive_knapsack(n - 1, capacity - self.weights[n - 1]),
                self.recursive_knapsack(n - 1, capacity)
            )

    def dynamic_knapsack(self):
        """
        Solve the Knapsack problem using dynamic programming.

        :return: Maximum value achievable
        """
        for i in range(self.n + 1):
            for w in range(self.capacity + 1):
                if i == 0 or w == 0:
                    self.dp[i][w] = 0
                elif self.weights[i - 1] <= w:
                    self.dp[i][w] = max(
                        self.values[i - 1] + self.dp[i - 1][w - self.weights[i - 1]],
                        self.dp[i - 1][w]
                    )
                else:
                    self.dp[i][w] = self.dp[i - 1][w]
        return self.dp[self.n][self.capacity]

    def print_selected_items(self):
        """
        Print the items selected in the optimal solution.
        """
        w = self.capacity
        selected_items = []
        for i in range(self.n, 0, -1):
            if self.dp[i][w] != self.dp[i - 1][w]:
                selected_items.append(i - 1)
                w -= self.weights[i - 1]
        print("Selected items (index):", selected_items)


def main():
    """
    Main function to demonstrate the Knapsack problem solution.
    """
    weights = [2, 3, 4, 5]  # Weights of the items
    values = [3, 4, 5, 6]   # Values of the items
    capacity = 5            # Capacity of the knapsack

    knapsack = Knapsack(weights, values, capacity)

    # Recursive approach
    print("Maximum value (recursive):", knapsack.recursive_knapsack(len(weights), capacity))

    # Dynamic programming approach
    print("Maximum value (dynamic programming):", knapsack.dynamic_knapsack())

    # Print selected items
    knapsack.print_selected_items()


if __name__ == "__main__":
    main()