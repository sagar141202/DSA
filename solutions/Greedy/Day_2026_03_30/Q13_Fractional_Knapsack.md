# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the subset of these items to include in a knapsack of limited capacity that maximizes the total value. The items can be taken fractionally, i.e., we can take a fraction of an item. The problem has the following constraints: we have 'n' items, each item has a weight 'w_i' and a value 'v_i', and the maximum capacity of the knapsack is 'W'. The goal is to find the optimal subset of items to include in the knapsack to maximize the total value without exceeding the knapsack capacity.

## Approach
The algorithm sorts the items based on their value-to-weight ratio in descending order. Then, it iterates through the sorted items and adds them to the knapsack until the capacity is full. If an item cannot be added completely, it is added fractionally to fill the remaining capacity. This greedy approach ensures that the total value is maximized.

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

double fractionalKnapsack(int W, vector<int> wt, vector<int> val, int n) {
    vector<Item> items(n);
    for (int i = 0; i < n; i++) {
        items[i].weight = wt[i];
        items[i].value = val[i];
        items[i].ratio = (double)val[i] / wt[i];
    }

    sort(items.begin(), items.end(), compareItems);

    double maxValue = 0.0;
    for (int i = 0; i < n; i++) {
        if (W >= items[i].weight) {
            maxValue += items[i].value;
            W -= items[i].weight;
        } else {
            double fraction = (double)W / items[i].weight;
            maxValue += items[i].value * fraction;
            break;
        }
    }

    return maxValue;
}

int main() {
    int n = 3;
    vector<int> val = {60, 100, 120};
    vector<int> wt = {10, 20, 30};
    int W = 50;

    double maxValue = fractionalKnapsack(W, wt, val, n);
    cout << "Maximum value: " << maxValue << endl;

    return 0;
}
```

## Test Cases
```
Input: n = 3, val = [60, 100, 120], wt = [10, 20, 30], W = 50
Output: Maximum value: 240.0
```

## Key Takeaways
- The Fractional Knapsack problem can be solved using a greedy approach by sorting the items based on their value-to-weight ratio.
- The algorithm iterates through the sorted items and adds them to the knapsack until the capacity is full, adding items fractionally if necessary.
- The time complexity of the algorithm is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the items.