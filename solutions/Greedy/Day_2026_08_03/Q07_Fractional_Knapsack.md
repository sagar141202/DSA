# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the subset of these items to include in a knapsack of limited capacity that maximizes the total value. The items can be divided into fractions, allowing for a fractional amount of an item to be included in the knapsack. The goal is to find the optimal subset of items to include, with the possibility of including only a fraction of an item, such that the total value is maximized without exceeding the knapsack's capacity. The problem has the following constraints: there are n items, each item i has a weight wi and a value vi, and the knapsack has a capacity W.

## Approach
The algorithm uses a greedy approach, sorting the items by their value-to-weight ratio in descending order. It then iterates over the sorted items, adding as much of each item as possible to the knapsack without exceeding its capacity. The item with the highest value-to-weight ratio is added first, and so on, until the knapsack is full.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Item {
    double weight;
    double value;
    double ratio;
};

bool compareItems(Item a, Item b) {
    return a.ratio > b.ratio;
}

double fractionalKnapsack(vector<Item>& items, double capacity) {
    // Calculate the value-to-weight ratio for each item
    for (auto& item : items) {
        item.ratio = item.value / item.weight;
    }

    // Sort the items by their value-to-weight ratio in descending order
    sort(items.begin(), items.end(), compareItems);

    double totalValue = 0.0;
    for (auto& item : items) {
        if (capacity >= item.weight) {
            // Add the entire item to the knapsack
            capacity -= item.weight;
            totalValue += item.value;
        } else {
            // Add a fraction of the item to the knapsack
            double fraction = capacity / item.weight;
            totalValue += item.value * fraction;
            break;
        }
    }

    return totalValue;
}

int main() {
    int n;
    cin >> n;

    vector<Item> items(n);
    for (auto& item : items) {
        cin >> item.weight >> item.value;
    }

    double capacity;
    cin >> capacity;

    double maxValue = fractionalKnapsack(items, capacity);
    cout << maxValue << endl;

    return 0;
}
```

## Test Cases
```
Input:
3
10 60
20 100
30 120
50
Output:
240.0
```

## Key Takeaways
- The greedy approach works because the items are sorted by their value-to-weight ratio, ensuring that the most valuable items are added to the knapsack first.
- The algorithm has a time complexity of O(n log n) due to the sorting step, and a space complexity of O(n) for storing the items.
- The fractional knapsack problem allows for a more optimal solution than the 0/1 knapsack problem, as it can include fractions of items in the knapsack.