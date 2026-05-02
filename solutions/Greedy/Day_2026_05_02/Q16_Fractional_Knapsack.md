# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be divided into fractions, allowing for a fractional number of items to be included in the collection. The problem has the following constraints: the number of items (n) is between 1 and 1000, the weight limit (W) is between 1 and 1000, the weight of each item (w) is between 1 and 1000, and the value of each item (v) is between 1 and 1000. For example, given items with weights [10, 20, 30] and values [60, 100, 120] and a weight limit of 50, the maximum value that can be achieved is 240.

## Approach
The algorithm sorts the items based on their value-to-weight ratio, then iterates over the sorted items, including as much of each item as possible without exceeding the weight limit. This greedy approach ensures the maximum value is achieved. The key insight is to prioritize items with higher value-to-weight ratios. The solution has a simple and efficient implementation. It can be solved using a priority queue or a simple sort.

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

    // Sort the items based on their value-to-weight ratio
    sort(arr, arr + n, compareItems);

    double totalValue = 0.0;

    // Iterate over the sorted items
    for (int i = 0; i < n; i++) {
        if (W >= arr[i].weight) {
            // Include the entire item
            W -= arr[i].weight;
            totalValue += arr[i].value;
        } else {
            // Include a fraction of the item
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
    cout << "Maximum value: " << maxValue << endl;

    return 0;
}
```

## Test Cases
```
Input: W = 50, arr = [(10, 60), (20, 100), (30, 120)]
Output: 240.0
```

## Key Takeaways
- The problem can be solved using a greedy approach by prioritizing items with higher value-to-weight ratios.
- The time complexity of the solution is O(n log n) due to the sorting step.
- The space complexity is O(n) for storing the items and their ratios.