# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. The closest elements are defined as the `k` elements with the smallest absolute difference to `x`. If there are multiple elements with the same smallest absolute difference, the ones with the smaller index should be chosen. For example, given the array `arr = [1, 2, 3, 4, 5]`, `k = 4`, and `x = 3`, the output should be `[1, 2, 3, 4]`.

## Approach
The algorithm uses a two-pointer technique to find the `k` closest elements. It first finds the index of the closest element to `x` using binary search, and then expands outwards to find the remaining `k-1` closest elements. The time complexity is optimized by using binary search to find the initial closest element.

## Complexity
- Time: O(log n + k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findKClosestElements(vector<int>& arr, int k, int x) {
    // Find the index of the closest element to x using binary search
    int left = 0, right = arr.size() - k;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (x - arr[mid] > arr[mid + k] - x) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    // Return the k closest elements
    return vector<int>(arr.begin() + left, arr.begin() + left + k);
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    int k = 4;
    int x = 3;
    vector<int> result = findKClosestElements(arr, k, x);
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
- Use binary search to find the index of the closest element to `x` in the array.
- Expand outwards from the closest element to find the remaining `k-1` closest elements.
- The time complexity is optimized by using binary search to find the initial closest element.