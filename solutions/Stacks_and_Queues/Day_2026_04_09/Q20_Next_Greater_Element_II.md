# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in a circular manner) that is greater than `x`. If no such element exists, return `-1`. The input array `nums` will contain unique integers, and the length of the array will be between 1 and 10000.

## Approach
We can use a stack to store the indices of the elements in the array. We iterate over the array twice to consider the circular nature of the array. For each element, we pop all the elements from the stack that are smaller than the current element and update the result array.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElements(vector<int>& nums) {
    int n = nums.size();
    vector<int> res(n, -1);
    stack<int> st;
    
    // Iterate over the array twice to consider the circular nature
    for (int i = 0; i < 2 * n; i++) {
        // Use the modulus operator to get the actual index in the array
        int idx = i % n;
        
        // While the stack is not empty and the top element is smaller than the current element
        while (!st.empty() && nums[st.top()] < nums[idx]) {
            // Pop the top element from the stack and update the result array
            res[st.top()] = nums[idx];
            st.pop();
        }
        
        // Push the current index onto the stack
        st.push(idx);
    }
    
    return res;
}
```

## Test Cases
```
Input: nums = [1,2,1]
Output: [2,-1,2]
```

## Key Takeaways
- Use a stack to store the indices of the elements in the array.
- Iterate over the array twice to consider the circular nature of the array.
- Pop all the elements from the stack that are smaller than the current element and update the result array.