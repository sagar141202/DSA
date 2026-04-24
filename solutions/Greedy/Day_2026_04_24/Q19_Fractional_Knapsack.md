# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the subset of these items to include in a knapsack of limited capacity such that the total value is maximized. The knapsack has a capacity of W and the items are (w1, v1), (w2, v2), ..., (wn, vn) where wi is the weight of the ith item and vi is its value. The goal is to maximize the total value while not exceeding the knapsack capacity. The items can be taken fractionally, meaning if an item doesn't fit fully, a fraction of it can be taken.

## Approach
The algorithm sorts the items by their value-to-weight ratio in descending order. It then iterates over the sorted items, adding them to the knapsack if possible. If an item doesn't fit fully, a fraction of it is taken to fill the remaining capacity. This greedy approach ensures the maximum value is achieved.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Structure to represent an item
struct Item {
    int weight;
    int value;
    double ratio;
};

// Comparison function for sorting items
bool compareItems(const Item &a, const Item &b) {
    return a.ratio > b.ratio;
}

double fractionalKnapsack(int W, vector<int> &wt, vector<int> &val, int n) {
    // Create a vector of items
    vector<Item> items(n);
    for (int i = 0; i < n; i++) {
        items[i].weight = wt[i];
        items[i].value = val[i];
        items[i].ratio = (double)val[i] / wt[i];
    }

    // Sort the items by their value-to-weight ratio
    sort(items.begin(), items.end(), compareItems);

    double totalValue = 0.0;
    for (int i = 0; i < n; i++) {
        if (W >= items[i].weight) {
            // Item can be taken fully
            W -= items[i].weight;
            totalValue += items[i].value;
        } else {
            // Item can't be taken fully, take a fraction
            double fraction = (double)W / items[i].weight;
            totalValue += items[i].value * fraction;
            break;
        }
    }

    return totalValue;
}

int main() {
    int W = 50; // Knapsack capacity
    vector<int> val = {60, 100, 120};
    vector<int> wt = {10, 20, 30};
    int n = val.size();

    double maxValue = fractionalKnapsack(W, wt, val, n);
    cout << "Maximum value: " << maxValue << endl;

    return 0;
}
```

## Test Cases
```
Input: W = 50, val = [60, 100, 120], wt = [10, 20, 30]
Output: Maximum value: 240.0
```

## Key Takeaways
- The greedy algorithm works by choosing the item with the highest value-to-weight ratio at each step.
- The items are sorted by their value-to-weight ratio in descending order to ensure the maximum value is achieved.
- If an item doesn't fit fully, a fraction of it is taken to fill the remaining capacity, maximizing the total value.