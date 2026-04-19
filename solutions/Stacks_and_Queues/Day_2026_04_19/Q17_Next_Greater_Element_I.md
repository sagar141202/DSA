# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. The next greater element of an element `x` is the first element to its right that is greater than `x`. If no such element exists, the next greater element is `-1`. The function should return an array of the same length as the input array, where each element at index `i` is the next greater element of the element at index `i` in the input array. For example, given the input array `[2, 1, 2, 4, 3]`, the output should be `[4, 2, 4, -1, -1]` because the next greater element of `2` is `4`, the next greater element of `1` is `2`, and so on.

## Approach
We can solve this problem using a stack data structure. The idea is to iterate over the array and for each element, pop all the elements from the stack that are smaller than the current element and update the next greater element for these elements.

## Complexity
- Time: O(n)
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
Input: nums1 = [2, 4], nums2 = [1, 2, 3, 4]
Output: [2, -1]
Input: nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
Output: [-1, 3, -1]
```

## Key Takeaways
- Use a stack to keep track of the elements that do not have a next greater element yet.
- Iterate over the array and pop all the elements from the stack that are smaller than the current element.
- Update the next greater element for the popped elements.
- Use an unordered map to store the next greater element for each element.