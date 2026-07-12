# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be divided into fractions, allowing for a fractional amount of an item to be included in the collection. For example, if an item has a weight of 5 and a value of 10, we can include 0.5 of this item in the collection, which would contribute 2.5 to the total weight and 5 to the total value. The goal is to maximize the total value while not exceeding the weight limit.

## Approach
The algorithm sorts the items by their value-to-weight ratio in descending order, then iterates through the sorted items, adding as much of each item as possible to the collection without exceeding the weight limit. This greedy approach ensures that the total value is maximized.

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
            capacity -= items[i].weight;
            maxValue += items[i].value;
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
    vector<int> weights(n), values(n);
    for (int i = 0; i < n; i++) {
        cin >> weights[i] >> values[i];
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
10 60
20 100
30 120
50
Output:
240.0
```

## Key Takeaways
- The fractional knapsack problem can be solved using a greedy approach, which involves sorting the items by their value-to-weight ratio and then adding as much of each item as possible to the collection.
- The time complexity of the solution is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the items.
- The solution can be applied to real-world problems, such as resource allocation and portfolio optimization, where the goal is to maximize the total value while not exceeding a given limit.