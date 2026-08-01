# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (circularly) that is greater than `x`. If no such element exists, return `-1`. The input array `nums` contains distinct integers and has a length of `n`, where `1 <= n <= 10^5`. The elements in `nums` are in the range `[1, 10^5]`. For example, given `nums = [1, 2, 1]`, the output should be `[2, -1, 2]`.

## Approach
We use a stack to keep track of the indices of the elements we've seen so far. We iterate over the array twice to handle the circular case. For each element, we pop all the elements from the stack that are smaller than the current element and update their next greater element.

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
    stack<int> st;
    
    // Iterate over the array twice to handle the circular case
    for (int i = 0; i < 2 * n; i++) {
        // Use the modulus operator to handle the circular case
        int idx = i % n;
        
        // Pop all the elements from the stack that are smaller than the current element
        while (!st.empty() && nums[st.top()] < nums[idx]) {
            result[st.top()] = nums[idx];
            st.pop();
        }
        
        // Push the current index onto the stack
        st.push(idx);
    }
    
    return result;
}
```

## Test Cases
```
Input: nums = [1, 2, 1]
Output: [2, -1, 2]
Input: nums = [1, 2, 3, 4, 3]
Output: [2, 3, 4, -1, 4]
```

## Key Takeaways
- Use a stack to keep track of the indices of the elements we've seen so far.
- Iterate over the array twice to handle the circular case.
- Pop all the elements from the stack that are smaller than the current element and update their next greater element.