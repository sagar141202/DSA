# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in the circular sense) that is greater than `x`. If no such element exists, return `-1`. The length of `nums` is in the range `[1, 10^4]`, and all elements are in the range `[1, 10^5]`. For example, if `nums = [1, 2, 1]`, the next greater element for `1` at index `0` is `2` at index `1`, and the next greater element for `1` at index `2` is `2` at index `1` (in the circular sense).

## Approach
We use a stack to keep track of the indices of the elements we have seen so far. We iterate through the array twice to handle the circular case. For each element, we pop all the elements from the stack that are smaller than the current element and update their next greater element.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElements(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n, -1);
    stack<int> s;
    
    // Iterate through the array twice to handle the circular case
    for (int i = 0; i < 2 * n; i++) {
        // Use the modulo operator to handle the circular case
        int idx = i % n;
        
        // Pop all the elements from the stack that are smaller than the current element
        while (!s.empty() && nums[s.top()] < nums[idx]) {
            result[s.top()] = nums[idx];
            s.pop();
        }
        
        // Push the current index to the stack
        s.push(idx);
    }
    
    return result;
}
```

## Test Cases
```
Input: nums = [1, 2, 1]
Output: [2, -1, 2]
```

## Key Takeaways
- Use a stack to keep track of the indices of the elements we have seen so far.
- Iterate through the array twice to handle the circular case.
- Use the modulo operator to handle the circular case when accessing the array elements.