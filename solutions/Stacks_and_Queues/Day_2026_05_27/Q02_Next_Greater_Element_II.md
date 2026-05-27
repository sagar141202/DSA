# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in a circular manner) that is greater than `x`. If no such element exists, return `-1`. The input array `nums` will contain at least one element and at most 1000 elements. The elements in `nums` will be in the range `[1, 10^5]`. For example, given `nums = [1, 2, 1]`, the next greater element for each element is `[2, -1, 2]`.

## Approach
We can use a stack to store the indices of the elements. We iterate through the array twice to handle the circular case. For each element, we pop all the elements from the stack that are smaller than the current element and update their next greater element.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<int> nextGreaterElements(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n, -1);
    stack<int> st;
    
    // iterate through the array twice to handle the circular case
    for (int i = 0; i < 2 * n; i++) {
        while (!st.empty() && nums[st.top()] < nums[i % n]) {
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
- Use a stack to store the indices of the elements to efficiently find the next greater element.
- Iterate through the array twice to handle the circular case.
- Pop all the elements from the stack that are smaller than the current element and update their next greater element.