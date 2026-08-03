# Next Greater Element I

## Problem Statement
The problem "Next Greater Element I" involves finding the next greater element for each element in an array. Given two arrays `nums1` and `nums2`, for each element in `nums1`, find the next greater element in `nums2`. If no greater element is found, return -1. The arrays contain distinct integers, and `nums1` is a subset of `nums2`. The length of `nums1` is `m`, and the length of `nums2` is `n`. For example, if `nums1 = [4, 1, 2]` and `nums2 = [1, 3, 4, 2]`, the output should be `[3, 3, -1]`.

## Approach
We will use a stack-based approach to find the next greater element. We iterate through `nums2` and use a stack to keep track of elements that do not have a greater element yet. When we encounter a greater element, we update the result for the elements in the stack.

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
Input: nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
Output: [3, 3, -1]
```

## Key Takeaways
- Use a stack to keep track of elements that do not have a greater element yet.
- Utilize an unordered map to store the next greater element for each element in `nums2`.
- Iterate through `nums1` to find the next greater element for each element using the map.