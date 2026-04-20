# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be divided into fractions, allowing for more flexibility in the solution. The goal is to maximize the total value while not exceeding the weight limit. For example, if we have items with weights [10, 20, 30] and values [60, 100, 120], and a weight limit of 50, we should choose the items that give the maximum total value without exceeding the weight limit.

## Approach
The algorithm uses a greedy approach, sorting the items by their value-to-weight ratio and then selecting the items with the highest ratio until the weight limit is reached. This ensures that the most valuable items are chosen first, maximizing the total value.

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

double fractionalKnapsack(int capacity, int weights[], int values[], int n) {
    Item items[n];
    for (int i = 0; i < n; i++) {
        items[i].weight = weights[i];
        items[i].value = values[i];
        items[i].ratio = (double)values[i] / weights[i];
    }

    sort(items, items + n, compareItems);

    double totalValue = 0.0;
    for (int i = 0; i < n; i++) {
        if (capacity >= items[i].weight) {
            capacity -= items[i].weight;
            totalValue += items[i].value;
        } else {
            double fraction = (double)capacity / items[i].weight;
            totalValue += items[i].value * fraction;
            break;
        }
    }

    return totalValue;
}

int main() {
    int weights[] = {10, 20, 30};
    int values[] = {60, 100, 120};
    int capacity = 50;
    int n = sizeof(values) / sizeof(values[0]);
    double maxValue = fractionalKnapsack(capacity, weights, values, n);
    cout << "The maximum value of items that can be carried: " << maxValue << endl;
    return 0;
}
```

## Test Cases
```
Input: weights = [10, 20, 30], values = [60, 100, 120], capacity = 50
Output: The maximum value of items that can be carried: 240.0
```

## Key Takeaways
- The greedy approach is used to solve the fractional knapsack problem by sorting the items based on their value-to-weight ratio.
- The algorithm iterates over the sorted items and selects the items with the highest ratio until the weight limit is reached.
- The fractional knapsack problem allows for dividing items into fractions, making it more flexible than the 0/1 knapsack problem.