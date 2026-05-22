# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be divided into fractions, allowing for a fractional amount of each item to be included. The problem has the following constraints: there are n items, each item has a weight wi and a value vi, and the maximum weight capacity of the knapsack is W. The goal is to maximize the total value while not exceeding the weight capacity.

## Approach
The algorithm uses a greedy approach by sorting the items based on their value-to-weight ratio. It then iterates over the sorted items, including as much of each item as possible without exceeding the weight capacity. The item with the highest value-to-weight ratio is included first.

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

double fractionalKnapsack(int W, vector<int>& wt, vector<int>& val, int n) {
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
            maxValue += items[i].ratio * W;
            break;
        }
    }

    return maxValue;
}

int main() {
    int W = 50;
    vector<int> wt = {10, 20, 30};
    vector<int> val = {60, 100, 120};
    int n = wt.size();

    double maxValue = fractionalKnapsack(W, wt, val, n);
    cout << "Maximum value: " << maxValue << endl;

    return 0;
}
```

## Test Cases
```
Input: 
W = 50
wt = [10, 20, 30]
val = [60, 100, 120]
n = 3

Output: 
Maximum value: 240.0
```

## Key Takeaways
- The fractional knapsack problem can be solved using a greedy approach by sorting the items based on their value-to-weight ratio.
- The items with the highest value-to-weight ratio are included first to maximize the total value.
- The algorithm has a time complexity of O(n log n) due to the sorting operation.