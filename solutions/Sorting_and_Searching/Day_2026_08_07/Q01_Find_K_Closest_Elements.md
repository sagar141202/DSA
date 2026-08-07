# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the ones with the smallest values. The array `arr` contains distinct integers and is sorted in ascending order. The integer `k` is positive and less than or equal to the length of `arr`. The target value `x` can be any integer.

## Approach
We will use a two-pointer technique to find the closest elements. The idea is to maintain two pointers, one at the start and one at the end of the subarray, and move them based on the comparison of the elements with the target value. We will prioritize the smaller element when the distances are equal.

## Complexity
- Time: O(log(n) + k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findClosestElements(vector<int>& arr, int k, int x) {
    int left = 0, right = arr.size() - k;
    while (left < right) {
        int mid = left + (right - left) / 2;
        // If x - arr[mid] > arr[mid + k] - x, move the left pointer
        if (x - arr[mid] > arr[mid + k] - x) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    vector<int> result(arr.begin() + left, arr.begin() + left + k);
    return result;
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
- The two-pointer technique can be used to efficiently find the closest elements in a sorted array.
- Prioritizing the smaller element when distances are equal ensures that the result is unique and correct.
- The time complexity of O(log(n) + k) is achieved by using a binary search approach to find the closest elements.