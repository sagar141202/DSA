# Fractional Knapsack

## Problem Statement
The fractional knapsack problem is a problem in combinatorial optimization. Given a set of items, each with a weight and a value, determine the subset of these items to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be divided, meaning that a fraction of an item can be included in the knapsack. The goal is to maximize the total value while not exceeding the weight limit. For example, if we have items with weights [10, 20, 30] and values [60, 100, 120], and a knapsack capacity of 50, we need to find the optimal subset of these items (including fractions) to include in the knapsack to maximize the total value.

## Approach
The algorithm sorts the items by their value-to-weight ratio in descending order. Then, it iterates over the sorted items, adding them to the knapsack if possible, or adding a fraction of the item if it would exceed the capacity.

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

bool compareItems(const Item& a, const Item& b) {
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
- The fractional knapsack problem can be solved using a greedy approach by sorting items by their value-to-weight ratio.
- The time complexity is O(n log n) due to the sorting step.
- The space complexity is O(n) for storing the items and their ratios.