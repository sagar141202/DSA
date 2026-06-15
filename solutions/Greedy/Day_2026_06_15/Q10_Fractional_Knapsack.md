# Fractional Knapsack

## Problem Statement
The fractional knapsack problem is a problem in combinatorial optimization. Given a set of items, each with a weight and a value, determine the subset of these items to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be divided, meaning that a fraction of an item can be included in the collection. The problem has the following constraints: 
- Each item has a non-negative weight and value.
- The knapsack has a non-negative capacity.
- The goal is to maximize the total value while not exceeding the knapsack capacity.

## Approach
The algorithm for solving the fractional knapsack problem is based on a greedy strategy. It sorts the items by their value-to-weight ratio in descending order. Then it iterates over the sorted items, including as much of each item as possible without exceeding the knapsack capacity. If an item cannot be fully included, a fraction of it is included to fill the remaining capacity.

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

double fractionalKnapsack(int capacity, vector<int>& weights, vector<int>& values, int n) {
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
    int n;
    cin >> n;
    vector<int> weights(n);
    vector<int> values(n);
    for (int i = 0; i < n; i++) {
        cin >> weights[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> values[i];
    }
    int capacity;
    cin >> capacity;
    
    double maxValue = fractionalKnapsack(capacity, weights, values, n);
    cout << maxValue << endl;
    
    return 0;
}
```

## Test Cases
```
Input: 
3
10 20 30
60 100 120
50
Output: 
230.0
```

## Key Takeaways
- The fractional knapsack problem can be solved using a greedy algorithm that sorts items by their value-to-weight ratio.
- The algorithm iterates over the sorted items, including as much of each item as possible without exceeding the knapsack capacity.
- If an item cannot be fully included, a fraction of it is included to fill the remaining capacity, maximizing the total value.