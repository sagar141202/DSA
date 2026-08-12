# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the subset of these items to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be taken fractionally, meaning if an item's weight is more than the remaining capacity, a fraction of the item can be taken. The problem has the following constraints: 1 <= number of items <= 1000, 1 <= weight of each item <= 1000, 1 <= value of each item <= 1000, and 1 <= capacity of knapsack <= 1000. For example, if we have items with weights [10, 20, 30] and values [60, 100, 120] and a knapsack capacity of 50, we should select items to maximize the total value while not exceeding the capacity.

## Approach
The algorithm sorts the items based on their value-to-weight ratio in descending order. It then iterates through the sorted items, taking as much of each item as possible without exceeding the capacity. This greedy approach ensures the maximum value is obtained.

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
- The problem is solved using a greedy algorithm that sorts items by their value-to-weight ratio.
- The algorithm iterates through the sorted items, taking as much of each item as possible without exceeding the capacity.
- The time complexity of the algorithm is O(n log n) due to the sorting step.