# Fractional Knapsack

## Problem Statement
The Fractional Knapsack problem is a classic problem in computer science and operations research. Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be divided into fractions, allowing for a more optimal solution than the 0/1 Knapsack problem. The problem has the following constraints: there are n items, each item has a weight wi and a value vi, the knapsack has a capacity W, and the goal is to maximize the total value while keeping the total weight within the capacity.

## Approach
The algorithm uses a greedy approach by sorting the items based on their value-to-weight ratio. It then selects items with the highest ratio until the knapsack is full. If an item cannot fit entirely in the knapsack, a fraction of it is taken to fill the remaining capacity.

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

    // Sort the items based on the ratio
    sort(arr, arr + n, compareItems);

    double maxValue = 0.0;
    for (int i = 0; i < n; i++) {
        if (arr[i].weight <= W) {
            // If the item can fit entirely, take it
            maxValue += arr[i].value;
            W -= arr[i].weight;
        } else {
            // If the item cannot fit entirely, take a fraction
            double fraction = (double)W / arr[i].weight;
            maxValue += arr[i].value * fraction;
            break;
        }
    }

    return maxValue;
}

int main() {
    int W = 50; // knapsack capacity
    Item arr[] = {{10, 60}, {20, 100}, {30, 120}};
    int n = sizeof(arr) / sizeof(arr[0]);

    double maxValue = fractionalKnapsack(W, arr, n);
    cout << "The maximum value of items that can be carried: " << maxValue << endl;

    return 0;
}
```

## Test Cases
```
Input: W = 50, arr = [{10, 60}, {20, 100}, {30, 120}]
Output: The maximum value of items that can be carried: 240.0
```

## Key Takeaways
- The Fractional Knapsack problem can be solved using a greedy approach by sorting the items based on their value-to-weight ratio.
- The algorithm has a time complexity of O(n log n) due to the sorting step.
- The problem allows for fractional items, which can lead to a more optimal solution than the 0/1 Knapsack problem.