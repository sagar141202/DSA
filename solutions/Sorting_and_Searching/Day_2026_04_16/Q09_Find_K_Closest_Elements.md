# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the ones with the smallest values. The array `arr` contains distinct integers and is sorted in ascending order. The integer `k` is a positive integer and `x` is a real number.

## Approach
The algorithm uses a two-pointer technique to find the closest elements. It maintains two pointers, one at the start and one at the end of the potential closest elements range. The closest elements are then selected based on their absolute difference with the target `x`. This approach ensures that the `k` closest elements are found efficiently.

## Complexity
- Time: O(log(n) + k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findClosestElements(vector<int>& arr, int k, int x) {
    // Find the insertion point for x in arr to determine the closest elements range
    int left = 0, right = arr.size() - k;
    while (left < right) {
        int mid = left + (right - left) / 2;
        // If x is greater than the middle element, move the left pointer
        if (x - arr[mid] > arr[mid + k] - x) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    // Return the k closest elements
    return vector<int>(arr.begin() + left, arr.begin() + left + k);
}
```

## Test Cases
```
Input: arr = [1, 2, 3, 4, 5], k = 4, x = 3
Output: [1, 2, 3, 4]
Input: arr = [1, 5, 10, 15, 20], k = 3, x = 8
Output: [5, 10, 15]
```

## Key Takeaways
- The two-pointer technique is useful for finding the closest elements in a sorted array.
- The time complexity is O(log(n) + k) due to the binary search and the selection of the closest elements.
- The space complexity is O(k) for storing the result.