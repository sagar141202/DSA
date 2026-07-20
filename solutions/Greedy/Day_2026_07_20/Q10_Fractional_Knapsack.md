# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the number of items to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be taken fractionally, meaning that if an item's weight is more than the remaining capacity, a fraction of the item can be taken to fill the remaining capacity. The problem has the following constraints: 
- The capacity of the knapsack (W) is a positive integer.
- The number of items (n) is a positive integer.
- The weight of each item (w_i) is a positive integer.
- The value of each item (v_i) is a positive integer.
- The goal is to maximize the total value while keeping the total weight less than or equal to W.

## Approach
The algorithm uses a greedy approach by sorting the items based on their value-to-weight ratio in descending order. It then iterates over the sorted items, adding them to the knapsack if possible, or adding a fraction of the item if it exceeds the remaining capacity. The item with the highest value-to-weight ratio is chosen first to maximize the total value.

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

double fractionalKnapsack(int W, vector<int>& w, vector<int>& v, int n) {
    vector<Item> items(n);
    for (int i = 0; i < n; i++) {
        items[i].weight = w[i];
        items[i].value = v[i];
        items[i].ratio = (double)v[i] / w[i];
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
    int n = 3;
    int W = 50;
    vector<int> w = {10, 20, 30};
    vector<int> v = {60, 100, 120};

    double maxValue = fractionalKnapsack(W, w, v, n);
    cout << "Maximum value: " << maxValue << endl;

    return 0;
}
```

## Test Cases
```
Input: W = 50, n = 3, w = [10, 20, 30], v = [60, 100, 120]
Output: Maximum value: 240.0
```

## Key Takeaways
- The fractional knapsack problem can be solved using a greedy approach by sorting the items based on their value-to-weight ratio.
- The algorithm has a time complexity of O(n log n) due to the sorting step.
- The algorithm has a space complexity of O(n) for storing the items and their ratios.