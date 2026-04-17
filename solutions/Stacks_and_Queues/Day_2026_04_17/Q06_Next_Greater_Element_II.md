# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (circularly) that is greater than `x`. If no such element exists, return `-1`. The input array will contain at least one element and at most 10,000 elements. Each element in the input array will be between 1 and 10^9.

## Approach
We can use a stack to keep track of the elements we have seen so far. We iterate over the array twice to consider the circular nature of the array. For each element, we pop all the elements from the stack that are smaller than the current element and update the next greater element for these elements.

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
    stack<int> s;
    
    // iterate over the array twice to consider the circular nature
    for (int i = 0; i < 2 * n; i++) {
        // use the modulus operator to wrap around to the start of the array
        int j = i % n;
        
        // while the stack is not empty and the top element of the stack is smaller than the current element
        while (!s.empty() && nums[s.top()] < nums[j]) {
            // update the next greater element for the top element of the stack
            res[s.top()] = nums[j];
            // pop the top element from the stack
            s.pop();
        }
        
        // push the current index onto the stack
        s.push(j);
    }
    
    return res;
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
- Use a stack to keep track of the elements we have seen so far.
- Iterate over the array twice to consider the circular nature of the array.
- Update the next greater element for each element by popping all the elements from the stack that are smaller than the current element.