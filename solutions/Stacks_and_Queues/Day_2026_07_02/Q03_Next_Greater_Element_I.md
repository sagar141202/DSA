# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. Given two arrays `nums1` and `nums2`, for each element in `nums1`, find the next greater element in `nums2`. If no such element is found, return -1. The next greater element of an element `x` is the first element to the right of `x` that is greater than `x`. The arrays contain distinct elements and the elements in `nums1` are guaranteed to be present in `nums2`. For example, given `nums1 = [4,1,2]` and `nums2 = [1,3,4,2]`, the output should be `[3,-1,3]`.

## Approach
We will use a stack-based approach to solve this problem. The idea is to iterate through `nums2` and use a stack to keep track of the elements that do not have a greater element yet. When we encounter an element that is greater than the top of the stack, we update the result for the top element of the stack.

## Complexity
- Time: O(n + m)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int, int> map;
    stack<int> st;
    for (int num : nums2) {
        while (!st.empty() && st.top() < num) {
            map[st.top()] = num;
            st.pop();
        }
        st.push(num);
    }
    vector<int> result;
    for (int num : nums1) {
        if (map.find(num) != map.end()) {
            result.push_back(map[num]);
        } else {
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
- Iterate through the second array to update the result for each element in the first array.
- Use an unordered map to store the next greater element for each element in the second array.