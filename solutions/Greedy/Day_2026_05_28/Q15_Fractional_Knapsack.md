# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the subset of these items to include in a knapsack of limited capacity such that the total value is maximized. The items can be divided into fractions, allowing for a more optimal solution. The problem has the following constraints: the knapsack capacity is a positive integer, the weights and values of the items are positive integers, and the number of items is a positive integer. For example, given a knapsack capacity of 10 and items with weights and values of (3, 60), (2, 100), and (4, 120), the goal is to maximize the total value while staying within the knapsack capacity.

## Approach
The algorithm sorts the items by their value-to-weight ratio in descending order and then iterates over the sorted items, adding as much of each item as possible to the knapsack without exceeding the capacity. This greedy approach ensures that the total value is maximized.

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

double fractionalKnapsack(int capacity, vector<int> weights, vector<int> values) {
    int n = weights.size();
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
    int capacity = 10;
    vector<int> weights = {3, 2, 4};
    vector<int> values = {60, 100, 120};
    cout << fractionalKnapsack(capacity, weights, values) << endl;
    return 0;
}
```

## Test Cases
```
Input: capacity = 10, weights = [3, 2, 4], values = [60, 100, 120]
Output: 240.0
```

## Key Takeaways
- The greedy algorithm is used to solve the fractional knapsack problem by sorting the items based on their value-to-weight ratio.
- The time complexity of the solution is O(n log n) due to the sorting operation.
- The space complexity is O(n) as we need to store the items and their ratios.