# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. The next greater element of an element `x` is the first element to its right that is greater than `x`. If no such element exists, the next greater element is considered to be `-1`. The problem takes two arrays `nums1` and `nums2` as input, where `nums1` is a subset of `nums2`. The task is to find the next greater element for each element in `nums1` based on the elements present in `nums2`. The arrays contain distinct integers, and the length of `nums1` is less than or equal to the length of `nums2`. For example, given `nums1 = [4,1,2]` and `nums2 = [1,3,4,2]`, the output should be `[-1,3,-1]`.

## Approach
The algorithm uses a stack to keep track of the elements in `nums2` that do not have a greater element to their right yet. It iterates over `nums2` and pushes elements onto the stack. When a greater element is encountered, it pops elements from the stack and updates the next greater element for each popped element. The next greater elements for `nums1` are stored in a map for efficient lookup.

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
- Use a stack to keep track of elements that do not have a greater element to their right yet.
- Utilize a map to store the next greater elements for efficient lookup.
- Iterate over the second array to populate the stack and map, then iterate over the first array to find the next greater elements.