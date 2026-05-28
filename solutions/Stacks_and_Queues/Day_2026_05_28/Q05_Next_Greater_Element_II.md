# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (circularly) that is greater than `x`. If no such element exists, return `-1`. The input array `nums` will contain distinct integers, and its length will be between 1 and 10^4.

## Approach
We use a stack to keep track of the elements we have seen so far. We iterate over the array twice to handle the circular case. For each element, we pop all the elements from the stack that are smaller than the current element and update their next greater element.

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
    
    // iterate over the array twice to handle the circular case
    for (int i = 0; i < 2 * n; i++) {
        while (!st.empty() && nums[st.top()] < nums[i % n]) {
            // update the next greater element for the top element of the stack
            result[st.top()] = nums[i % n];
            st.pop();
        }
        st.push(i % n);
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
- Use a stack to keep track of the elements we have seen so far.
- Iterate over the array twice to handle the circular case.
- Update the next greater element for each element by popping smaller elements from the stack.