# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be divided into fractions, allowing for a fractional amount of an item to be included in the collection. The problem has the following constraints: 1 <= number of items <= 1000, 1 <= weight and value of each item <= 1000, and 1 <= capacity of the knapsack <= 1000000. For example, if we have items with weights [10, 20, 30] and values [60, 100, 120], and a knapsack capacity of 50, the optimal solution would be to include the first item completely (weight 10, value 60), and then include 2/3 of the second item (weight 20 * 2/3 = 13.33, value 100 * 2/3 = 66.67), resulting in a total weight of 23.33 and a total value of 126.67.

## Approach
The algorithm sorts the items based on their value-to-weight ratio in descending order. Then, it iterates through the sorted items, including as much of each item as possible without exceeding the knapsack capacity. This greedy approach ensures that the total value is maximized.

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
            maxValue += items[i].ratio * capacity;
            break;
        }
    }
    return maxValue;
}

int main() {
    int capacity = 50;
    vector<int> weights = {10, 20, 30};
    vector<int> values = {60, 100, 120};
    cout << fractionalKnapsack(capacity, weights, values) << endl;
    return 0;
}
```

## Test Cases
```
Input: capacity = 50, weights = [10, 20, 30], values = [60, 100, 120]
Output: 240.0
```

## Key Takeaways
- The fractional knapsack problem can be solved using a greedy approach that sorts the items based on their value-to-weight ratio.
- The algorithm iterates through the sorted items, including as much of each item as possible without exceeding the knapsack capacity.
- The time complexity of the algorithm is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the items.