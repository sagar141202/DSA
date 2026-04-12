# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the subset of these items to include in a knapsack of limited capacity such that the total value is maximized. The items can be divided into fractions, allowing for a fractional portion of an item to be included in the knapsack. The problem has the following constraints: 
- The knapsack has a capacity of W.
- There are n items, each with a weight wi and a value vi.
- The goal is to maximize the total value of the items included in the knapsack without exceeding its capacity.

## Approach
The algorithm uses a greedy approach, sorting the items based on their value-to-weight ratio and then including them in the knapsack in that order. The item with the highest ratio is included first, and if it doesn't fit entirely, a fraction of it is included.

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

double fractionalKnapsack(int W, vector<int> weights, vector<int> values, int n) {
    vector<Item> items(n);
    for (int i = 0; i < n; i++) {
        items[i].weight = weights[i];
        items[i].value = values[i];
        items[i].ratio = (double)values[i] / weights[i];
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
    int W = 50;
    vector<int> weights = {10, 20, 30};
    vector<int> values = {60, 100, 120};

    double maxValue = fractionalKnapsack(W, weights, values, n);
    cout << "Maximum value: " << maxValue << endl;

    return 0;
}
```

## Test Cases
```
Input: 
n = 3
W = 50
weights = [10, 20, 30]
values = [60, 100, 120]
Output: 
Maximum value: 240.0
```

## Key Takeaways
- The greedy approach works because the problem has the optimal substructure property, meaning that the optimal solution can be constructed from the optimal solutions of its subproblems.
- The value-to-weight ratio is used to determine the order in which the items are included in the knapsack.
- The algorithm has a time complexity of O(n log n) due to the sorting step, and a space complexity of O(n) for storing the items.