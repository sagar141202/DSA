# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. Given two arrays `nums1` and `nums2`, for each element in `nums1`, find the next greater element in `nums2`. If no such element exists, return -1. The next greater element of an element `x` is the first element to the right of `x` that is greater than `x`. The arrays `nums1` and `nums2` contain distinct elements, and `nums1` is a subset of `nums2`. The problem can be solved using a stack-based approach.

## Approach
We will use a stack to store the indices of elements from `nums2` and iterate over `nums2` to find the next greater element for each element. We will also use a map to store the next greater element for each element in `nums2`.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    stack<int> st;
    unordered_map<int, int> map;
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
Output: [-1,3,-1]
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
```

## Key Takeaways
- Use a stack to store the indices of elements and find the next greater element.
- Utilize an unordered map to store the next greater element for each element in `nums2`.
- Iterate over `nums1` to find the next greater element for each element using the map.