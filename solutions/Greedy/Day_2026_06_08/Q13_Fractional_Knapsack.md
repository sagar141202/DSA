# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the subset of these items to include in a knapsack of limited capacity that maximizes the total value. The items can be divided into fractions, allowing for a fractional amount of an item to be included. The problem has the following constraints: each item has a non-negative weight and value, and the knapsack has a non-negative capacity. For example, if we have items with weights [10, 20, 30] and values [60, 100, 120], and a knapsack capacity of 50, we want to find the optimal subset of items to include to maximize the total value.

## Approach
The algorithm works by sorting the items based on their value-to-weight ratio, then iteratively adding the items with the highest ratio to the knapsack until it is full. This greedy approach ensures that we maximize the total value. We use a priority queue to store the items, where the priority is the value-to-weight ratio.

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

double fractionalKnapsack(int capacity, vector<int>& weights, vector<int>& values) {
    int n = weights.size();
    vector<Item> items(n);
    for (int i = 0; i < n; i++) {
        items[i].weight = weights[i];
        items[i].value = values[i];
        items[i].ratio = (double)values[i] / weights[i];
    }

    sort(items.begin(), items.end(), compareItems);

    double totalValue = 0.0;
    for (int i = 0; i < n; i++) {
        if (capacity >= items[i].weight) {
            capacity -= items[i].weight;
            totalValue += items[i].value;
        } else {
            double fraction = (double)capacity / items[i].weight;
            totalValue += items[i].value * fraction;
            break;
        }
    }

    return totalValue;
}

int main() {
    int capacity = 50;
    vector<int> weights = {10, 20, 30};
    vector<int> values = {60, 100, 120};

    double maxValue = fractionalKnapsack(capacity, weights, values);
    cout << "Maximum value: " << maxValue << endl;

    return 0;
}
```

## Test Cases
```
Input: capacity = 50, weights = [10, 20, 30], values = [60, 100, 120]
Output: Maximum value: 240.0
```

## Key Takeaways
- The fractional knapsack problem can be solved using a greedy approach by sorting the items based on their value-to-weight ratio.
- The time complexity of the solution is O(n log n) due to the sorting step.
- The space complexity is O(n) for storing the items and their ratios.