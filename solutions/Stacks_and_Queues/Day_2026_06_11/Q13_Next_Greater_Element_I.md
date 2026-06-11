# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. The next greater element of an element `x` is the first element to its right that is greater than `x`. If no such element exists, the next greater element is considered to be `-1`. The function should return an array of the same length as the input array, where each element at index `i` is the next greater element of the corresponding element in the input array. The input array consists of distinct integers, and the length of the array is between `1` and `10^4`. For example, given the input array `[2, 1, 5]`, the output should be `[5, 5, -1]`.

## Approach
We can solve this problem using a stack-based approach. The idea is to iterate over the input array and push elements onto the stack. When a greater element is encountered, we pop elements from the stack and update the result array until the stack is empty or the top element is greater than the current element.

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
        result.push_back(map.count(num) ? map[num] : -1);
    }
    return result;
}
```

## Test Cases
```
Input: nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
Output: [-1, 3, -1]
Input: nums1 = [2, 4], nums2 = [1, 2, 3, 4]
Output: [3, -1]
```

## Key Takeaways
- Use a stack to keep track of elements that do not have a greater element yet.
- Use an unordered map to store the next greater element for each element in the input array.
- Iterate over the input array to update the result array based on the next greater element of each element.