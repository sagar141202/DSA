# Find K Closest Elements

## Problem Statement
Given a sorted array, find the K closest elements to a given target. The closest elements are defined as the elements with the smallest absolute difference to the target. If there are multiple elements with the same absolute difference, the smaller element is considered closer. The array is 1-indexed, and the target is a real number. For example, given the array [1, 2, 3, 4, 5] and the target 3, the 3 closest elements are [2, 3, 4]. If the target is 3.7, the 3 closest elements are [3, 4, 5].

## Approach
We can use a two-pointer technique to find the K closest elements. First, we find the closest element to the target using binary search. Then, we expand outwards from this element, adding elements to the result list until we have K elements.

## Complexity
- Time: O(logN + K)
- Space: O(K)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findClosestElements(vector<int>& arr, int k, int x) {
    // Find the closest element to the target using binary search
    int left = 0, right = arr.size() - k;
    while (left < right) {
        int mid = left + (right - left) / 2;
        // If the target is closer to the middle element than the middle + k element, move the right pointer
        if (x - arr[mid] > arr[mid + k] - x) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    // Return the K closest elements
    return vector<int>(arr.begin() + left, arr.begin() + left + k);
}
```

## Test Cases
```
Input: arr = [1, 2, 3, 4, 5], k = 3, x = 3.7
Output: [3, 4, 5]
Input: arr = [1, 2, 3, 4, 5], k = 3, x = 3
Output: [2, 3, 4]
```

## Key Takeaways
- The two-pointer technique can be used to find the K closest elements in a sorted array.
- Binary search can be used to find the closest element to the target in O(logN) time.
- The time complexity of the solution is O(logN + K), where N is the size of the array and K is the number of closest elements to find.