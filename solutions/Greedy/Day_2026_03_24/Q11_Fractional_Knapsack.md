# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be divided into fractions, allowing for more flexible solutions. For example, if an item has a weight of 10 and a value of 60, you can choose to take 0.5 of this item, which would have a weight of 5 and a value of 30. The goal is to maximize the total value while not exceeding the weight limit.

## Approach
The algorithm sorts the items by their value-to-weight ratio in descending order. It then iterates over the sorted items, adding as much of each item as possible to the knapsack without exceeding the weight limit. This approach ensures that the total value is maximized.

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

double fractionalKnapsack(int capacity, vector<Item>& items) {
    double maxValue = 0.0;
    // Calculate the value-to-weight ratio for each item
    for (auto& item : items) {
        item.ratio = (double)item.value / item.weight;
    }
    // Sort the items by their value-to-weight ratio in descending order
    sort(items.begin(), items.end(), compareItems);
    // Iterate over the sorted items and add as much of each item as possible to the knapsack
    for (auto& item : items) {
        if (capacity >= item.weight) {
            // Take the whole item
            maxValue += item.value;
            capacity -= item.weight;
        } else {
            // Take a fraction of the item
            double fraction = (double)capacity / item.weight;
            maxValue += item.value * fraction;
            break;
        }
    }
    return maxValue;
}

int main() {
    int capacity = 50;
    vector<Item> items = {{10, 60}, {20, 100}, {30, 120}};
    double maxValue = fractionalKnapsack(capacity, items);
    cout << "The maximum value is: " << maxValue << endl;
    return 0;
}
```

## Test Cases
```
Input: capacity = 50, items = [(10, 60), (20, 100), (30, 120)]
Output: The maximum value is: 240.0
```

## Key Takeaways
- The fractional knapsack problem can be solved using a greedy approach by sorting the items by their value-to-weight ratio.
- The algorithm has a time complexity of O(n log n) due to the sorting step.
- The space complexity is O(n) for storing the items and their ratios.