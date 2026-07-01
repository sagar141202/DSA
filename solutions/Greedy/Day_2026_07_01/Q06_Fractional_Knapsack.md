# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be divided into fractions, allowing for a fractional amount of an item to be included in the collection. The problem has the following constraints: 
- The weights and values of the items are non-negative.
- The weight limit of the knapsack is a non-negative integer.
- The number of items is a positive integer.

## Approach
The algorithm sorts the items based on their value-to-weight ratio in descending order, then iterates over the sorted items, including as much of each item as possible without exceeding the weight limit. The greedy choice is to always choose the item with the highest value-to-weight ratio.

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

    double totalValue = 0.0;
    for (int i = 0; i < n; i++) {
        if (W >= items[i].weight) {
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
Input: 
n = 3
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
Output: 
Maximum value: 240.0
```

## Key Takeaways
- The problem can be solved using a greedy approach by sorting the items based on their value-to-weight ratio.
- The algorithm has a time complexity of O(n log n) due to the sorting step.
- The algorithm has a space complexity of O(n) for storing the items.