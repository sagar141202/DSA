# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the subset of these items to include in a knapsack of limited capacity that maximizes the total value. The items can be divided into fractions, allowing for a fractional amount of an item to be included in the knapsack. The goal is to maximize the total value while not exceeding the knapsack capacity. For example, given items with weights [10, 20, 30] and values [60, 100, 120], and a knapsack capacity of 50, the optimal solution may involve including fractions of the items to achieve the maximum value.

## Approach
The algorithm sorts the items based on their value-to-weight ratio in descending order. It then iterates through the sorted items, adding them to the knapsack if they fit entirely, or adding a fraction of the item if it doesn't fit entirely but still has value. This greedy approach ensures the maximum value is achieved.

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

double fractionalKnapsack(int capacity, vector<int>& weights, vector<int>& values, int n) {
    vector<Item> items(n);
    for (int i = 0; i < n; i++) {
        items[i].weight = weights[i];
        items[i].value = values[i];
        items[i].ratio = (double)values[i] / weights[i];
    }

    sort(items.begin(), items.end(), compareItems);

    double maxValue = 0.0;
    for (int i = 0; i < n; i++) {
        if (capacity >= items[i].weight) {
            maxValue += items[i].value;
            capacity -= items[i].weight;
        } else {
            double fraction = (double)capacity / items[i].weight;
            maxValue += items[i].value * fraction;
            break;
        }
    }

    return maxValue;
}

int main() {
    int n = 3;
    vector<int> weights = {10, 20, 30};
    vector<int> values = {60, 100, 120};
    int capacity = 50;

    double maxValue = fractionalKnapsack(capacity, weights, values, n);
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
- The fractional knapsack problem can be solved using a greedy approach by sorting items based on their value-to-weight ratio.
- The algorithm iterates through the sorted items, adding them to the knapsack if they fit entirely, or adding a fraction of the item if it doesn't fit entirely but still has value.
- The time complexity of the algorithm is O(n log n) due to the sorting operation, and the space complexity is O(n) for storing the items.