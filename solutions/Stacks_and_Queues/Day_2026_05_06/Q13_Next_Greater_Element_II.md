# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in a circular manner) that is greater than `x`. If no such element exists, return `-1`. The input array `nums` will have a length in the range `[1, 10^4]`, and the values in the array will be in the range `[-10^4, 10^4]`. For example, given `nums = [1, 2, 1]`, the output should be `[2, -1, 2]`.

## Approach
We use a stack-based approach to solve this problem. The idea is to iterate over the array twice to handle the circular nature of the array, using a stack to keep track of the elements we have seen so far. We pop elements from the stack when we find a greater element and update the result array accordingly.

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
        int idx = i % n;
        
        // While the stack is not empty and the current element is greater than the top of the stack
        while (!s.empty() && nums[idx] > nums[s.top()]) {
            // Update the result array with the next greater element
            result[s.top()] = nums[idx];
            // Pop the top element from the stack
            s.pop();
        }
        
        // Push the current index onto the stack
        s.push(idx);
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
- Iterate over the array twice to handle the circular nature of the array.
- Update the result array with the next greater element when we find a greater element.