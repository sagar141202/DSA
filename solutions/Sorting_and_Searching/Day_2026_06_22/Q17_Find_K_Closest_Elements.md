# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the ones with the smallest values. The array `arr` contains distinct integers and is sorted in ascending order. The input array will have at least `k` elements.

## Approach
We will use a two-pointer technique to find the closest elements. We will calculate the absolute difference between each element and the target value `x` and then use a priority queue or sorting to find the `k` closest elements.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findClosestElements(vector<int>& arr, int k, int x) {
    // Calculate the absolute difference between each element and the target value x
    vector<pair<int, int>> diff;
    for (int i = 0; i < arr.size(); i++) {
        diff.push_back({abs(arr[i] - x), arr[i]});
    }
    
    // Sort the differences and corresponding elements
    sort(diff.begin(), diff.end());
    
    // Select the k closest elements
    vector<int> closest;
    for (int i = 0; i < k; i++) {
        closest.push_back(diff[i].second);
    }
    
    // Sort the closest elements in ascending order
    sort(closest.begin(), closest.end());
    
    return closest;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    int k = 4;
    int x = 3;
    vector<int> result = findClosestElements(arr, k, x);
    for (int num : result) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: arr = [1, 2, 3, 4, 5], k = 4, x = 3
Output: [1, 2, 3, 4]
Input: arr = [1, 5, 10, 15, 20], k = 3, x = 8
Output: [1, 5, 10]
```

## Key Takeaways
- Use a two-pointer technique or sorting to find the closest elements.
- Calculate the absolute difference between each element and the target value to determine the closest elements.
- Use a priority queue or sorting to efficiently find the k closest elements.