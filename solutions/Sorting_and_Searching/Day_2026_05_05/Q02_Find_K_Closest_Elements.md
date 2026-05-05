# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the ones with the smallest values. The array `arr` contains distinct integers and is sorted in ascending order. The integer `k` is positive and does not exceed the length of the array.

## Approach
The algorithm uses a two-pointer technique to find the closest elements. It calculates the absolute difference between each element and the target, then uses a priority queue or sorting to find the `k` smallest differences. Alternatively, it can use a binary search approach to find the closest element, then expand outwards to find the `k` closest elements.

## Complexity
- Time: O(n log n) for sorting or O(log n + k) for binary search
- Space: O(k) for storing the result

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findKClosestElements(vector<int>& arr, int k, int x) {
    // Calculate absolute differences and store in a vector of pairs
    vector<pair<int, int>> diff;
    for (int i = 0; i < arr.size(); i++) {
        diff.push_back({abs(arr[i] - x), arr[i]});
    }
    
    // Sort the vector based on the differences
    sort(diff.begin(), diff.end());
    
    // Store the k closest elements in a vector
    vector<int> result;
    for (int i = 0; i < k; i++) {
        result.push_back(diff[i].second);
    }
    
    // Sort the result vector in ascending order
    sort(result.begin(), result.end());
    
    return result;
}

// Alternatively, using binary search
vector<int> findKClosestElementsBinarySearch(vector<int>& arr, int k, int x) {
    int left = 0, right = arr.size() - k;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (x - arr[mid] > arr[mid + k] - x) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return vector<int>(arr.begin() + left, arr.begin() + left + k);
}
```

## Test Cases
```
Input: arr = [1, 2, 3, 4, 5], k = 2, x = 3
Output: [2, 3]
Input: arr = [1, 5, 10, 15, 20], k = 3, x = 8
Output: [1, 5, 10]
```

## Key Takeaways
- Use a two-pointer technique or binary search to efficiently find the closest elements.
- Consider using a priority queue or sorting to handle cases with multiple closest elements.
- The binary search approach can be more efficient for large arrays and small values of `k`.