# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in a circular manner) that is greater than `x`. If no such element exists, return `-1`. The input array `nums` will contain unique integers, and the length of the array will be between 1 and 10^5. For example, if `nums = [1, 2, 1]`, the next greater element for each element would be `[2, -1, 2]`.

## Approach
We can use a stack-based approach to solve this problem. The idea is to iterate over the array twice to handle the circular nature, using a stack to keep track of the elements we have seen so far. We pop elements from the stack whenever we find a greater element, updating the result accordingly.

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
    
    // Iterate over the array twice to handle the circular nature
    for (int i = 0; i < 2 * n; i++) {
        // Use the modulus operator to wrap around to the start of the array
        int j = i % n;
        
        // While the stack is not empty and the current element is greater than the top of the stack
        while (!s.empty() && nums[j] > nums[s.top()]) {
            // Update the result for the top element of the stack
            result[s.top()] = nums[j];
            // Pop the top element from the stack
            s.pop();
        }
        
        // Push the current index onto the stack
        s.push(j);
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
- Iterate over the array twice to handle the circular nature.
- Update the result whenever we find a greater element for the top element of the stack.