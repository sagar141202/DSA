# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be divided into fractions, allowing for a fractional amount of each item to be included. The goal is to maximize the total value of the items included without exceeding the weight limit.

## Approach
The algorithm sorts the items by their value-to-weight ratio in descending order, then iterates over the sorted items, including as much of each item as possible without exceeding the weight limit. This greedy approach ensures that the most valuable items are included first.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Item {
    double weight;
    double value;
};

bool compareItems(Item a, Item b) {
    return (a.value / a.weight) > (b.value / b.weight);
}

double fractionalKnapsack(int W, Item arr[], int n) {
    // Sort items by value-to-weight ratio
    sort(arr, arr + n, compareItems);

    double totalValue = 0.0;

    // Iterate over sorted items
    for (int i = 0; i < n; i++) {
        // If the current item can be fully included, include it
        if (arr[i].weight <= W) {
            totalValue += arr[i].value;
            W -= arr[i].weight;
        } else {
            // Otherwise, include a fraction of the current item
            double fraction = W / arr[i].weight;
            totalValue += arr[i].value * fraction;
            break;
        }
    }

    return totalValue;
}

int main() {
    int W = 50; // weight limit
    Item arr[] = {{10, 60}, {20, 100}, {30, 120}};
    int n = sizeof(arr) / sizeof(arr[0]);

    double maxValue = fractionalKnapsack(W, arr, n);
    cout << "Maximum value: " << maxValue << endl;

    return 0;
}
```

## Test Cases
```
Input: W = 50, arr = [(10, 60), (20, 100), (30, 120)]
Output: Maximum value: 240.0
```

## Key Takeaways
- The fractional knapsack problem can be solved using a greedy approach, which sorts items by their value-to-weight ratio and includes as much of each item as possible without exceeding the weight limit.
- The time complexity of the algorithm is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the items.
- The algorithm can be used to solve real-world problems, such as maximizing the value of items to be included in a knapsack with limited capacity.