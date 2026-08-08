# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the subset of items to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be taken fractionally, i.e., we can take a fraction of an item. The goal is to maximize the total value while not exceeding the weight limit.

## Approach
The algorithm sorts the items by their value-to-weight ratio in descending order and then iterates over the sorted items, adding them to the knapsack until the weight limit is reached. If an item can't be added fully, a fraction of it is added to fill the remaining capacity.

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
    // Calculate the value-to-weight ratio for each item
    for (int i = 0; i < n; i++) {
        arr[i].ratio = (double)arr[i].value / arr[i].weight;
    }

    // Sort the items by their value-to-weight ratio in descending order
    sort(arr, arr + n, compareItems);

    double totalValue = 0.0;

    // Iterate over the sorted items and add them to the knapsack
    for (int i = 0; i < n; i++) {
        if (W >= arr[i].weight) {
            // If the item can be added fully, add it and update the remaining capacity
            W -= arr[i].weight;
            totalValue += arr[i].value;
        } else {
            // If the item can't be added fully, add a fraction of it to fill the remaining capacity
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
Input: W = 50, arr = [(10, 60), (20, 100), (30, 120)]
Output: Maximum value: 240.0
```

## Key Takeaways
- The fractional knapsack problem can be solved using a greedy approach by sorting the items by their value-to-weight ratio.
- The algorithm iterates over the sorted items and adds them to the knapsack until the weight limit is reached.
- If an item can't be added fully, a fraction of it is added to fill the remaining capacity.