# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the ones with the smallest values. The array `arr` contains distinct integers and is sorted in ascending order. The integer `k` is positive and does not exceed the length of the array. The target value `x` can be any integer.

## Approach
The algorithm uses a two-pointer technique to find the closest elements. It maintains two pointers, one at the start and one at the end of the potential closest elements range. The pointers are adjusted based on the comparison of the target value with the middle element of the range.

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
        // If x is closer to the middle element of the left half, move the right pointer
        if (x - arr[mid] > arr[mid + k] - x) {
            left = mid + 1;
        } 
        // If x is closer to the middle element of the right half, move the left pointer
        else {
            right = mid;
        }
    }
    // Return the k closest elements
    return vector<int>(arr.begin() + left, arr.begin() + left + k);
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    int k = 2;
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
Input: arr = [1, 2, 3, 4, 5], k = 2, x = 3
Output: [2, 3]
Input: arr = [1, 5, 10, 15, 20], k = 3, x = 8
Output: [1, 5, 10]
```

## Key Takeaways
- The two-pointer technique is useful for finding the closest elements in a sorted array.
- The time complexity is O(log(n) + k) due to the binary search and the iteration over the k closest elements.
- The space complexity is O(k) for storing the k closest elements.