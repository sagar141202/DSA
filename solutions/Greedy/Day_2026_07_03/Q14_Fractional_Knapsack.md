# Fractional Knapsack

## Problem Statement
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The items can be divided into fractions, allowing for more flexibility in the solution. The goal is to maximize the total value while not exceeding the weight limit. For example, given items with weights [10, 20, 30] and values [60, 100, 120], and a weight limit of 50, the optimal solution would be to take the first item (weight 10, value 60) and 2/3 of the second item (weight 20 * 2/3 = 13.33, value 100 * 2/3 = 66.67), resulting in a total weight of 23.33 and a total value of 126.67.

## Approach
The algorithm sorts the items based on their value-to-weight ratio, then iterates through the sorted items, taking as much of each item as possible without exceeding the weight limit. This greedy approach ensures that the total value is maximized.

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

double fractionalKnapsack(int W, vector<int>& wt, vector<int>& val, int n) {
    vector<Item> items(n);
    for (int i = 0; i < n; i++) {
        items[i].weight = wt[i];
        items[i].value = val[i];
        items[i].ratio = (double)val[i] / wt[i];
    }

    sort(items.begin(), items.end(), compareItems);

    double totalValue = 0.0;
    for (int i = 0; i < n; i++) {
        if (W >= items[i].weight) {
            W -= items[i].weight;
            totalValue += items[i].value;
        } else {
            double fraction = (double)W / items[i].weight;
            totalValue += items[i].value * fraction;
            break;
        }
    }

    return totalValue;
}

int main() {
    int W = 50; // weight limit
    vector<int> val = {60, 100, 120}; // values
    vector<int> wt = {10, 20, 30}; // weights
    int n = val.size(); // number of items

    double maxValue = fractionalKnapsack(W, wt, val, n);
    cout << "Maximum value: " << maxValue << endl;

    return 0;
}
```

## Test Cases
```
Input: W = 50, val = [60, 100, 120], wt = [10, 20, 30]
Output: Maximum value: 240.0
```

## Key Takeaways
- The fractional knapsack problem can be solved using a greedy approach, sorting the items by their value-to-weight ratio and taking as much of each item as possible without exceeding the weight limit.
- The time complexity of this solution is O(n log n) due to the sorting step.
- The space complexity is O(n) as we need to store the items and their ratios.