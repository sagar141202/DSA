# Next Greater Element I

## Problem Statement
The problem "Next Greater Element I" involves finding the next greater element for each element in the first array. Given two arrays `nums1` and `nums2`, for each element in `nums1`, find the next greater element in `nums2`. If no such element exists, return -1. The next greater element of an element `x` is the first element to its right that is greater than `x`. The arrays contain distinct integers, and `nums1` is a subset of `nums2`. For example, given `nums1 = [4,1,2]` and `nums2 = [1,3,4,2]`, the output should be `[3,-1,3]`.

## Approach
We will use a stack-based approach to find the next greater element. The idea is to iterate through `nums2` and use a stack to keep track of elements that do not have a greater element yet. When we encounter an element that is greater than the top of the stack, we pop the stack and update the result for the popped element.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int, int> map;
    stack<int> st;
    for (int num : nums2) {
        // while the stack is not empty and the current number is greater than the top of the stack
        while (!st.empty() && num > st.top()) {
            // pop the stack and update the result for the popped element
            map[st.top()] = num;
            st.pop();
        }
        // push the current number onto the stack
        st.push(num);
    }
    vector<int> result;
    for (int num : nums1) {
        // if the number is in the map, add the next greater element to the result
        if (map.find(num) != map.end()) {
            result.push_back(map[num]);
        } else {
            // otherwise, add -1 to the result
            result.push_back(-1);
        }
    }
    return result;
}
```

## Test Cases
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [3,-1,3]
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
```

## Key Takeaways
- Use a stack to keep track of elements that do not have a greater element yet.
- Iterate through the second array and update the result for elements in the first array.
- Use an unordered map to store the next greater element for each element in the second array.