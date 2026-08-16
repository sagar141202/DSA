# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the ones with the smallest values. The array `arr` contains distinct integers and is sorted in ascending order. For example, given `arr = [1, 2, 3, 4, 5]`, `k = 4`, and `x = 3`, the output should be `[1, 2, 3, 4]`.

## Approach
The algorithm uses a two-pointer technique to find the closest elements. It maintains two pointers, one at the start and one at the end of the subarray, and moves them based on the comparison of the elements with the target value. The closest elements are then returned as a subarray.

## Complexity
- Time: O(log(n) + k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        // Find the insertion point of x in the array
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
        // Return the k closest elements
        return vector<int>(arr.begin() + left, arr.begin() + left + k);
    }
};

int main() {
    Solution solution;
    vector<int> arr = {1, 2, 3, 4, 5};
    int k = 4;
    int x = 3;
    vector<int> result = solution.findClosestElements(arr, k, x);
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
- The two-pointer technique is useful for finding the closest elements in a sorted array.
- The time complexity is O(log(n) + k) due to the binary search and the space complexity is O(k) for storing the result.
- The algorithm handles edge cases where the target value is less than the smallest element or greater than the largest element in the array.