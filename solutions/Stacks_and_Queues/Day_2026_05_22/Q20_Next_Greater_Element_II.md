# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in a circular manner) that is greater than `x`. If no such element exists, return `-1`. The input array `nums` contains unique integers and has a length of `n`, where `1 <= n <= 10^5`. The elements in `nums` are in the range `[-10^5, 10^5]`.

## Approach
We will use a stack to keep track of the indices of the elements in `nums`. We iterate through `nums` twice to consider the circular nature of the array. For each element, we pop all the elements from the stack that are smaller than the current element and update their next greater element.

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
    
    // Iterate through nums twice to consider the circular nature
    for (int i = 0; i < 2 * n; i++) {
        // Use modulo to wrap around to the start of nums
        int j = i % n;
        
        // Pop all the elements from the stack that are smaller than the current element
        while (!st.empty() && nums[st.top()] < nums[j]) {
            result[st.top()] = nums[j];
            st.pop();
        }
        
        // Push the current index to the stack
        st.push(j);
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
- Use a stack to keep track of the indices of the elements in `nums`.
- Iterate through `nums` twice to consider the circular nature of the array.
- Pop all the elements from the stack that are smaller than the current element and update their next greater element.