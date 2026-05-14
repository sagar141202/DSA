# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the subset of these items to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be taken fractionally, meaning if an item's weight exceeds the remaining capacity, a fraction of the item can be included. The problem has the following constraints: 
- The number of items (n) is a positive integer.
- The capacity of the knapsack (W) is a positive integer.
- The weight (w) and value (v) of each item are positive integers.
- The goal is to maximize the total value without exceeding the capacity.
- For example, given items [(60, 10), (100, 20), (120, 30)] and a capacity of 50, the solution would be to take the first item completely (value 60, weight 10) and then take 40/20 = 2 of the second item, resulting in a total value of 60 + 100 * (40/20) = 160.

## Approach
The algorithm sorts the items by their value-to-weight ratio in descending order. It then iterates over the sorted items, adding them to the knapsack if possible. If an item's weight exceeds the remaining capacity, a fraction of the item is added. This greedy approach ensures the maximum value is achieved.

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
    double totalValue = 0.0;

    // Calculate the value-to-weight ratio for each item
    for (int i = 0; i < n; i++) {
        arr[i].ratio = (double)arr[i].value / arr[i].weight;
    }

    // Sort items by their value-to-weight ratio in descending order
    sort(arr, arr + n, compareItems);

    // Iterate over the sorted items and add them to the knapsack
    for (int i = 0; i < n; i++) {
        if (arr[i].weight <= W) {
            W -= arr[i].weight;
            totalValue += arr[i].value;
        } else {
            double fraction = (double)W / arr[i].weight;
            totalValue += arr[i].value * fraction;
            break;
        }
    }

    return totalValue;
}

int main() {
    int W = 50;
    Item arr[] = {{10, 60}, {20, 100}, {30, 120}};
    int n = sizeof(arr) / sizeof(arr[0]);

    double maxValue = fractionalKnapsack(W, arr, n);
    cout << "The maximum value of items that can be carried: " << maxValue << endl;

    return 0;
}
```

## Test Cases
```
Input: 
  - Capacity (W): 50
  - Items: [(10, 60), (20, 100), (30, 120)]
Output: 
  - Maximum value: 240.0
```

## Key Takeaways
- The fractional knapsack problem allows for fractional inclusion of items, making it different from the 0/1 knapsack problem.
- Sorting items by their value-to-weight ratio is crucial for achieving the maximum value.
- The greedy approach ensures that the solution is optimal, as the items with the highest value-to-weight ratio are added first.