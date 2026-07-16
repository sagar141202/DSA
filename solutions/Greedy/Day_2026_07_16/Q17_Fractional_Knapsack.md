# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the subset of these items to include in a knapsack of limited capacity that maximizes the total value. The items can be divided into fractions, allowing for more flexibility in the solution. The goal is to find the optimal subset of items that maximizes the total value while not exceeding the knapsack capacity. For example, if we have items with weights [10, 20, 30] and values [60, 100, 120] and a knapsack capacity of 50, the optimal solution would involve taking a fraction of the items to maximize the total value.

## Approach
The algorithm sorts the items based on their value-to-weight ratio in descending order. It then iterates over the sorted items, adding them to the knapsack if they fit entirely, or taking a fraction of the item if it doesn't fit. This greedy approach ensures that the most valuable items are prioritized.

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
- The fractional knapsack problem allows for fractional items, making it different from the 0/1 knapsack problem.
- Sorting items based on their value-to-weight ratio is crucial for the greedy approach to work.
- The algorithm iterates over the sorted items, adding them to the knapsack or taking a fraction of the item if it doesn't fit entirely.