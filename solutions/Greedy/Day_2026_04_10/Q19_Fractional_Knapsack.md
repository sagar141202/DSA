# Fractional Knapsack

## Problem Statement
The fractional knapsack problem is a problem in combinatorial optimization. Given a set of items, each with a weight and a value, determine the subset of these items to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be divided, meaning that a fraction of an item can be included in the knapsack. The goal is to maximize the total value while not exceeding the weight limit.

## Approach
The algorithm sorts the items by their value-to-weight ratio in descending order. It then iterates over the sorted items, adding as much of each item as possible to the knapsack without exceeding the weight limit. This greedy approach ensures that the total value is maximized.

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
};

bool compareItems(const Item &a, const Item &b) {
    double ratioA = (double)a.value / a.weight;
    double ratioB = (double)b.value / b.weight;
    return ratioA > ratioB;
}

double fractionalKnapsack(int capacity, Item items[], int n) {
    // Sort items by value-to-weight ratio in descending order
    sort(items, items + n, compareItems);

    double maxValue = 0.0;

    // Iterate over the sorted items
    for (int i = 0; i < n; i++) {
        // If the current item can fit entirely in the knapsack, add it
        if (capacity >= items[i].weight) {
            capacity -= items[i].weight;
            maxValue += items[i].value;
        } else {
            // If the current item cannot fit entirely, add a fraction of it
            double fraction = (double)capacity / items[i].weight;
            maxValue += items[i].value * fraction;
            break;
        }
    }

    return maxValue;
}

int main() {
    int n;
    cout << "Enter the number of items: ";
    cin >> n;

    Item items[n];
    for (int i = 0; i < n; i++) {
        cin >> items[i].weight >> items[i].value;
    }

    int capacity;
    cout << "Enter the knapsack capacity: ";
    cin >> capacity;

    double maxValue = fractionalKnapsack(capacity, items, n);
    cout << "Maximum value: " << maxValue << endl;

    return 0;
}
```

## Test Cases
```
Input: 
Number of items: 3
Item 1: weight = 10, value = 60
Item 2: weight = 20, value = 100
Item 3: weight = 30, value = 120
Knapsack capacity: 50
Output: 
Maximum value: 240.0

Input: 
Number of items: 2
Item 1: weight = 10, value = 60
Item 2: weight = 20, value = 100
Knapsack capacity: 15
Output: 
Maximum value: 90.0
```

## Key Takeaways
- The fractional knapsack problem can be solved using a greedy approach that sorts items by their value-to-weight ratio.
- The algorithm iterates over the sorted items, adding as much of each item as possible to the knapsack without exceeding the weight limit.
- The time complexity of the algorithm is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the items.