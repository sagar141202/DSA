# Find K Closest Elements

## Problem Statement
Given a sorted array `nums` and two integers `k` and `x`, find the `k` closest elements to `x` in the array. The closest elements are defined as the elements with the smallest absolute difference to `x`. If there are multiple elements with the same absolute difference, the smaller element is considered closer. The function should return the `k` closest elements in sorted order.

## Approach
The approach is to use a two-pointer technique to find the closest elements. We maintain two pointers, one at the start and one at the end of the array, and move them towards each other based on the absolute difference between the elements and `x`. We use a priority queue or sorting to get the `k` closest elements.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findClosestElements(vector<int>& nums, int k, int x) {
    // Calculate the absolute difference between each element and x
    vector<pair<int, int>> diff;
    for (int i = 0; i < nums.size(); i++) {
        diff.push_back({abs(nums[i] - x), nums[i]});
    }
    
    // Sort the differences and get the k closest elements
    sort(diff.begin(), diff.end());
    vector<int> closest;
    for (int i = 0; i < k; i++) {
        closest.push_back(diff[i].second);
    }
    
    // Sort the closest elements in ascending order
    sort(closest.begin(), closest.end());
    return closest;
}
```

## Test Cases
```
Input: nums = [1, 2, 3, 4, 5], k = 4, x = 3
Output: [1, 2, 3, 4]
Input: nums = [1, 5, 10, 15, 20], k = 3, x = 8
Output: [5, 10, 15]
```

## Key Takeaways
- Use a two-pointer technique or sorting to find the closest elements.
- Calculate the absolute difference between each element and the target value.
- Use a priority queue or sorting to get the k closest elements in sorted order.