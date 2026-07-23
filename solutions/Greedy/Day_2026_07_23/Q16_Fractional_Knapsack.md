# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the subset of these items to include in a knapsack of limited capacity that maximizes the total value. The items can be divided into fractions, allowing for a fractional amount of an item to be included in the knapsack. The goal is to find the optimal subset of items that maximizes the total value without exceeding the knapsack's capacity.

## Approach
The algorithm sorts the items by their value-to-weight ratio in descending order. It then iterates over the sorted items, adding as much of each item as possible to the knapsack without exceeding its capacity. This greedy approach ensures that the maximum value is achieved.

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
};

bool compareItems(const Item& a, const Item& b) {
    return (a.value / a.weight) > (b.value / b.weight);
}

double fractionalKnapsack(double capacity, vector<Item>& items) {
    // Sort items by value-to-weight ratio in descending order
    sort(items.begin(), items.end(), compareItems);

    double maxValue = 0.0;
    for (const auto& item : items) {
        if (capacity >= item.weight) {
            // Add the whole item to the knapsack
            maxValue += item.value;
            capacity -= item.weight;
        } else {
            // Add a fraction of the item to the knapsack
            double fraction = capacity / item.weight;
            maxValue += item.value * fraction;
            break;
        }
    }

    return maxValue;
}

int main() {
    int n;
    double capacity;
    cout << "Enter the number of items: ";
    cin >> n;
    cout << "Enter the capacity of the knapsack: ";
    cin >> capacity;

    vector<Item> items(n);
    for (int i = 0; i < n; ++i) {
        cout << "Enter the weight and value of item " << i + 1 << ": ";
        cin >> items[i].weight >> items[i].value;
    }

    double maxValue = fractionalKnapsack(capacity, items);
    cout << "Maximum value: " << maxValue << endl;

    return 0;
}
```

## Test Cases
```
Input: 
Enter the number of items: 3
Enter the capacity of the knapsack: 50
Enter the weight and value of item 1: 10 60
Enter the weight and value of item 2: 20 100
Enter the weight and value of item 3: 30 120
Output: 
Maximum value: 240.0
```

## Key Takeaways
- The fractional knapsack problem can be solved using a greedy approach by sorting items by their value-to-weight ratio.
- The algorithm iterates over the sorted items, adding as much of each item as possible to the knapsack without exceeding its capacity.
- The time complexity of the algorithm is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the items.