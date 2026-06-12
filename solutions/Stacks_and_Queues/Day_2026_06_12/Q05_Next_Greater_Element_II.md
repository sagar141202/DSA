# Next Greater Element II

## Problem Statement
Given a circular array of integers, find the next greater element for each element in the array. The next greater element of an element at index `i` is the first element to its right (in a circular manner) that is greater than the element at index `i`. If no such element exists, return -1 for that index. The array is 0-indexed and has a length of `n`, where `n` is in the range [1, 10^4]. Each element in the array is in the range [1, 10^5].

## Approach
We use a stack-based approach to solve this problem, where we iterate over the array twice to handle the circular nature of the array. We maintain a stack to keep track of the indices of the elements we have seen so far.

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
    
    // Iterate over the array twice to handle the circular nature
    for (int i = 0; i < 2 * n; i++) {
        // Calculate the actual index in the array
        int idx = i % n;
        
        // While the stack is not empty and the current element is greater than the element at the top of the stack
        while (!st.empty() && nums[idx] > nums[st.top()]) {
            // Pop the top element from the stack and update the result
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
Input: nums = [1,2,1]
Output: [2,-1,2]
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
```

## Key Takeaways
- Use a stack-based approach to solve problems involving next greater elements.
- Iterate over the array twice to handle the circular nature of the array.
- Maintain a stack to keep track of the indices of the elements we have seen so far.