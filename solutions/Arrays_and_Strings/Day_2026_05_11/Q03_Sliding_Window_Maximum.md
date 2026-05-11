# Sliding Window Maximum

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the maximum value in each subarray of size `k`. The subarray can start at any index in `nums` and must contain `k` consecutive elements. For example, if `nums = [1, 3, -1, -3, 5, 3, 6, 7]` and `k = 3`, the output should be `[3, 3, 5, 5, 6, 7]`.

## Approach
The algorithm uses a deque to store the indices of the elements in the current window. It maintains the deque in such a way that the front always contains the index of the maximum element in the current window. The deque is updated by removing the elements that are out of the current window and the elements that are smaller than the current element.

## Complexity
- Time: O(n)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    // Create a deque to store the indices of the elements in the current window
    deque<int> dq;
    // Create a vector to store the maximum values
    vector<int> maxValues;
    
    // Iterate over the array
    for (int i = 0; i < nums.size(); i++) {
        // Remove the elements that are out of the current window
        while (!dq.empty() && dq.front() < i - k + 1) {
            dq.pop_front();
        }
        
        // Remove the elements that are smaller than the current element
        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }
        
        // Add the current element to the deque
        dq.push_back(i);
        
        // Add the maximum value to the result vector
        if (i >= k - 1) {
            maxValues.push_back(nums[dq.front()]);
        }
    }
    
    return maxValues;
}
```

## Test Cases
```
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]
```

## Key Takeaways
- Use a deque to store the indices of the elements in the current window.
- Maintain the deque in such a way that the front always contains the index of the maximum element in the current window.
- Update the deque by removing the elements that are out of the current window and the elements that are smaller than the current element.