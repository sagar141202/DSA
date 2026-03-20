# Next Greater Element II

## Problem Statement
Given a circular array of integers, find the next greater element for each element. The next greater element of an element x is the first element to its right (in a circular manner) that is greater than x. If no such element exists, return -1. The input array will contain unique integers and will have a length between 1 and 10^5. For example, given the array [1, 2, 1], the next greater element for each element is [2, -1, 2] because the next greater element for 1 (at index 0) is 2 (at index 1), there is no greater element for 2 (at index 1), and the next greater element for 1 (at index 2) is 2 (at index 1 in a circular manner).

## Approach
We can solve this problem by using a stack to keep track of the indices of the elements we have seen so far. We iterate over the array twice to consider the circular nature of the array. For each element, we pop all the elements from the stack that are smaller than the current element and update the next greater element for these elements.

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
    
    // iterate over the array twice to consider the circular nature
    for (int i = 0; i < 2 * n; i++) {
        // use the modulus operator to get the actual index in the array
        int idx = i % n;
        
        // pop all the elements from the stack that are smaller than the current element
        while (!s.empty() && nums[s.top()] < nums[idx]) {
            result[s.top()] = nums[idx];
            s.pop();
        }
        
        // push the current index onto the stack
        s.push(idx);
    }
    
    return result;
}
```

## Test Cases
```
Input: [1, 2, 1]
Output: [2, -1, 2]
Input: [1, 2, 3, 4, 3]
Output: [2, 3, 4, -1, 4]
```

## Key Takeaways
- Use a stack to keep track of the indices of the elements we have seen so far.
- Iterate over the array twice to consider the circular nature of the array.
- Pop all the elements from the stack that are smaller than the current element and update the next greater element for these elements.