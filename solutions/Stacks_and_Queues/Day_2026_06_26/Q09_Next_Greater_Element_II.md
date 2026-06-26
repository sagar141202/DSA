# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in a circular manner) that is greater than `x`. If no such element exists, return `-1`. The length of `nums` is between `1` and `10^5`. Each element in `nums` is between `1` and `10^5`. For example, given `nums = [1, 2, 1]`, the next greater element for each element is `[2, -1, 2]`.

## Approach
We use a stack to keep track of the indices of elements. We iterate over the array twice to consider the circular nature of the array. For each element, we pop elements from the stack that are smaller than the current element and update their next greater element.

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
    
    // iterate over the array twice to consider the circular nature
    for (int i = 0; i < 2 * n; i++) {
        // use the modulus operator to get the actual index in the array
        int idx = i % n;
        
        // while the stack is not empty and the top element is smaller than the current element
        while (!st.empty() && nums[st.top()] < nums[idx]) {
            // update the next greater element for the top element
            result[st.top()] = nums[idx];
            // pop the top element from the stack
            st.pop();
        }
        
        // push the current index onto the stack
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
- Use a stack to keep track of the indices of elements.
- Iterate over the array twice to consider the circular nature of the array.
- Update the next greater element for each element by popping smaller elements from the stack.