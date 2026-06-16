# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in a circular manner) that is greater than `x`. If no such element exists, return `-1`. The input array `nums` contains distinct integers and has a length of `n`, where `1 <= n <= 10^5`. The elements in `nums` are in the range `[1, 10^5]`.

## Approach
We can use a stack to keep track of the elements we have seen so far. We iterate over the array twice to handle the circular case. For each element, we pop all the elements from the stack that are smaller than the current element and update their next greater element.

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
    
    // Iterate over the array twice to handle the circular case
    for (int i = 0; i < 2 * n; i++) {
        // Calculate the actual index in the array
        int j = i % n;
        
        // While the stack is not empty and the top element is smaller than the current element
        while (!s.empty() && nums[s.top()] < nums[j]) {
            // Update the next greater element for the top element
            result[s.top()] = nums[j];
            // Pop the top element from the stack
            s.pop();
        }
        
        // Push the current index to the stack
        s.push(j);
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
- Use a stack to keep track of the elements we have seen so far.
- Iterate over the array twice to handle the circular case.
- Update the next greater element for each element by popping all the smaller elements from the stack.