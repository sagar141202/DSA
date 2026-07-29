# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be divided into fractions, allowing for a fractional amount of an item to be included in the collection. The problem has the following constraints: 1 ≤ n ≤ 1000 (number of items), 1 ≤ w ≤ 1000 (maximum weight), and 1 ≤ vi, wi ≤ 1000 (value and weight of each item). For example, given items with values [60, 100, 120] and weights [10, 20, 30] and a maximum weight of 50, the optimal solution is to include the first item completely, the second item completely, and 2/3 of the third item.

## Approach
The algorithm uses a greedy approach, sorting the items by their value-to-weight ratio in descending order and then including as much of each item as possible. The item with the highest ratio is included first, and then the next item is included until the weight limit is reached. This approach ensures that the total value is maximized.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Item {
    int value;
    int weight;
    double ratio;
};

bool compareItems(Item a, Item b) {
    return a.ratio > b.ratio;
}

double fractionalKnapsack(int W, vector<int> &wt, vector<int> &val, int n) {
    vector<Item> items(n);
    for (int i = 0; i < n; i++) {
        items[i].value = val[i];
        items[i].weight = wt[i];
        items[i].ratio = (double)val[i] / wt[i];
    }
    sort(items.begin(), items.end(), compareItems);
    double totalValue = 0.0;
    for (int i = 0; i < n; i++) {
        if (items[i].weight <= W) {
            W -= items[i].weight;
            totalValue += items[i].value;
        } else {
            double fraction = (double)W / items[i].weight;
            totalValue += items[i].value * fraction;
            break;
        }
    }
    return totalValue;
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
- The greedy approach is used to solve the fractional knapsack problem.
- The items are sorted by their value-to-weight ratio in descending order.
- The item with the highest ratio is included first, and then the next item is included until the weight limit is reached.