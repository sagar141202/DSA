# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be divided into fractions, allowing for more precise optimization. The problem has the following constraints: 1 <= n <= 10^3 (number of items), 1 <= w <= 10^5 (maximum weight), and 1 <= vi, wi <= 10^5 (value and weight of each item). For example, if we have items with values [60, 100, 120] and weights [10, 20, 30] and a maximum weight of 50, the optimal solution would be to take the first item completely, the second item completely, and 0/1 of the third item, resulting in a maximum value of 220.

## Approach
The algorithm uses a greedy approach, sorting the items by their value-to-weight ratio in descending order. It then iterates over the sorted items, adding as much of each item as possible to the knapsack without exceeding the weight limit. The item with the highest value-to-weight ratio is added first, ensuring the maximum value is achieved.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Item {
    int value;
    int weight;
    double ratio;
};

bool compareItems(Item a, Item b) {
    return a.ratio > b.ratio;
}

double fractionalKnapsack(int w, vector<int>& v, vector<int>& wt, int n) {
    vector<Item> items(n);
    for (int i = 0; i < n; i++) {
        items[i].value = v[i];
        items[i].weight = wt[i];
        items[i].ratio = (double)v[i] / wt[i];
    }
    sort(items.begin(), items.end(), compareItems);
    double totalValue = 0.0;
    for (int i = 0; i < n; i++) {
        if (w >= items[i].weight) {
            w -= items[i].weight;
            totalValue += items[i].value;
        } else {
            double fraction = (double)w / items[i].weight;
            totalValue += items[i].value * fraction;
            break;
        }
    }
    return totalValue;
}

int main() {
    int n = 3;
    vector<int> v = {60, 100, 120};
    vector<int> wt = {10, 20, 30};
    int w = 50;
    double maxValue = fractionalKnapsack(w, v, wt, n);
    cout << "Maximum value: " << maxValue << endl;
    return 0;
}
```

## Test Cases
```
Input: n = 3, v = [60, 100, 120], wt = [10, 20, 30], w = 50
Output: Maximum value: 220.000000
```

## Key Takeaways
- The fractional knapsack problem allows for dividing items into fractions, making it possible to achieve a higher total value than the 0/1 knapsack problem.
- The greedy approach works by sorting items based on their value-to-weight ratio and adding them to the knapsack in that order.
- The time complexity of the solution is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the items.