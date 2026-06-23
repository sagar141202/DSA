# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the subset of these items to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be taken fractionally, meaning if an item's weight exceeds the remaining capacity, a fraction of the item can be included.

## Approach
The algorithm sorts the items by value-to-weight ratio in descending order, then iterates over the sorted items, including as much of each item as possible without exceeding the weight limit. This greedy approach ensures the maximum value is achieved.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Item {
    int weight;
    int value;
    double ratio;
};

bool compareItems(Item a, Item b) {
    return a.ratio > b.ratio;
}

double fractionalKnapsack(int W, Item arr[], int n) {
    // Calculate value-to-weight ratio for each item
    for (int i = 0; i < n; i++) {
        arr[i].ratio = (double)arr[i].value / arr[i].weight;
    }

    // Sort items by value-to-weight ratio in descending order
    sort(arr, arr + n, compareItems);

    double totalValue = 0.0;

    // Iterate over the sorted items
    for (int i = 0; i < n; i++) {
        if (arr[i].weight <= W) {
            // If the item's weight is less than or equal to the remaining capacity,
            // include the entire item
            totalValue += arr[i].value;
            W -= arr[i].weight;
        } else {
            // If the item's weight exceeds the remaining capacity, include a fraction
            // of the item
            double fraction = (double)W / arr[i].weight;
            totalValue += arr[i].value * fraction;
            break;
        }
    }

    return totalValue;
}

int main() {
    int W = 50; // Weight limit
    Item arr[] = {{10, 60}, {20, 100}, {30, 120}};
    int n = sizeof(arr) / sizeof(arr[0]);

    double maxValue = fractionalKnapsack(W, arr, n);
    cout << "Maximum value: " << maxValue << endl;

    return 0;
}
```

## Test Cases
```
Input: W = 50, items = [(10, 60), (20, 100), (30, 120)]
Output: Maximum value: 240.0
```

## Key Takeaways
- The fractional knapsack problem can be solved using a greedy approach by sorting items by their value-to-weight ratio.
- The algorithm iterates over the sorted items, including as much of each item as possible without exceeding the weight limit.
- The time complexity of the algorithm is O(n log n) due to the sorting step, where n is the number of items.