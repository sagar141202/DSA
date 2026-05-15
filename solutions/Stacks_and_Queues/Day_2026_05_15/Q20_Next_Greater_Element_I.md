# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. The next greater element of an element `x` is the first element to its right that is greater than `x`. If no such element exists, the next greater element is -1. The input array `nums1` is a subset of `nums2`. The problem can be solved using a stack data structure. The constraints are 1 <= nums1.length <= nums2.length <= 1000, and 0 <= nums1[i], nums2[i] <= 1000.

## Approach
The algorithm uses a stack to keep track of the elements in `nums2` that do not have a greater element to their right yet. It iterates over `nums2`, popping elements from the stack that are smaller than the current element and updating the result array accordingly.

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
```

## Key Takeaways
- Use a stack to keep track of elements that do not have a greater element to their right yet.
- Use an unordered map to store the next greater element for each element in `nums2`.
- Iterate over `nums1` to find the next greater element for each element using the map.