# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the subset of these items to include in a knapsack of limited capacity that maximizes the total value. The items can be taken fractionally, meaning that if an item doesn't fit whole into the knapsack, a fraction of it can be taken. The goal is to find the optimal subset of items that results in the highest total value without exceeding the knapsack's capacity.

## Approach
The algorithm sorts the items by their value-to-weight ratio in descending order and then iterates over the sorted items, adding as much of each item as possible to the knapsack without exceeding its capacity. This greedy approach ensures that the maximum value is achieved.

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

bool compareItems(const Item &a, const Item &b) {
    return a.ratio > b.ratio;
}

double fractionalKnapsack(int capacity, vector<int> &weights, vector<int> &values, int n) {
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
    cout << "Enter the number of items: ";
    cin >> n;

    vector<int> weights(n);
    vector<int> values(n);

    cout << "Enter the weights and values of the items: " << endl;
    for (int i = 0; i < n; i++) {
        cin >> weights[i] >> values[i];
    }

    int capacity;
    cout << "Enter the capacity of the knapsack: ";
    cin >> capacity;

    double maxValue = fractionalKnapsack(capacity, weights, values, n);
    cout << "The maximum value that can be achieved is: " << maxValue << endl;

    return 0;
}
```

## Test Cases
```
Input: 
Number of items: 3
Weights and values: 10 60, 20 100, 30 120
Capacity: 50
Output: The maximum value that can be achieved is: 240.0

Input: 
Number of items: 2
Weights and values: 10 60, 20 100
Capacity: 10
Output: The maximum value that can be achieved is: 30.0
```

## Key Takeaways
- The fractional knapsack problem can be solved using a greedy algorithm that sorts the items by their value-to-weight ratio.
- The algorithm iterates over the sorted items and adds as much of each item as possible to the knapsack without exceeding its capacity.
- The time complexity of the algorithm is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the items.