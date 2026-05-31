# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the ones with the smallest values. For example, given `arr = [1, 2, 3, 4, 5]`, `k = 4`, and `x = 3`, the output should be `[1, 2, 3, 4]`. The array `arr` has a length of `n`, where `1 <= n <= 10^4`, `1 <= k <= n`, and `x` is an integer.

## Approach
We will use a two-pointer technique to find the closest elements. The idea is to maintain two pointers, one at the start and one at the end of the window, and move them based on the distance from the target value. We will use the `lower_bound` function to find the closest element to the target value. Then, we will expand the window to the left and right based on the distance from the target value.

## Complexity
- Time: O(log n + k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findClosestElements(vector<int>& arr, int k, int x) {
    // Find the insertion point of x in arr to determine the closest elements
    auto it = lower_bound(arr.begin(), arr.end(), x);
    
    // Initialize two pointers, one at the insertion point and one at the start of the window
    int left = it - arr.begin();
    int right = left;
    
    // Move the pointers based on the distance from the target value
    while (right - left < k) {
        if (left == 0) {
            right++;
        } else if (right == arr.size()) {
            left--;
        } else if (x - arr[left - 1] <= arr[right] - x) {
            left--;
        } else {
            right++;
        }
    }
    
    // Return the k closest elements
    return vector<int>(arr.begin() + left, arr.begin() + right);
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
- Use a two-pointer technique to find the closest elements.
- The `lower_bound` function can be used to find the insertion point of the target value in the sorted array.
- Move the pointers based on the distance from the target value to find the k closest elements.