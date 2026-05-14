# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. The closest elements are defined as the elements with the smallest absolute difference to `x`. If there are multiple elements with the same smallest absolute difference, the elements with the smaller value should come first. For example, given `arr = [1, 2, 3, 4, 5]`, `k = 4`, and `x = 3`, the output should be `[1, 2, 3, 4]`. The array `arr` has a length of `n` where `1 <= n <= 10^5`, `1 <= k <= n`, and `x` is a 32-bit integer.

## Approach
The solution uses a two-pointer technique to find the optimal subarray of length `k` with the smallest absolute difference to `x`. The approach involves initializing two pointers at the start and end of the array and then moving them based on the absolute difference to `x`. This process continues until the optimal subarray is found.

## Complexity
- Time: O(log(n - k) + k)
- Space: O(k)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<int> findKClosestElements(vector<int>& arr, int k, int x) {
    int left = 0, right = arr.size() - k;
    while (left < right) {
        int mid = left + (right - left) / 2;
        // Check if x - arr[mid] > arr[mid + k] - x
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
Output: [1, 5, 10]
```

## Key Takeaways
- Use two-pointer technique to find the optimal subarray of length `k` with the smallest absolute difference to `x`.
- Initialize two pointers at the start and end of the array and move them based on the absolute difference to `x`.
- The time complexity of the solution is O(log(n - k) + k) due to the binary search and the space complexity is O(k) for storing the result.