# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. The next greater element of an element `x` is the first element to its right that is greater than `x`. If no such element is found, the next greater element is considered to be `-1`. The function should return an array where each element at index `i` is the next greater element of the element at index `i` in the input array. The input array will contain distinct integers and will have a length between `1` and `10000`. For example, given the input array `[2, 1, 5]`, the output should be `[5, 5, -1]` because the next greater element of `2` is `5`, the next greater element of `1` is `5`, and there is no next greater element for `5`.

## Approach
The algorithm uses a stack to keep track of the elements for which the next greater element has not been found yet. It iterates through the array, popping elements from the stack and updating the result array whenever it finds a greater element. The stack is updated by pushing the current element if it is not greater than the top of the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int, int> map;
    stack<int> s;
    for (int num : nums2) {
        while (!s.empty() && s.top() < num) {
            map[s.top()] = num;
            s.pop();
        }
        s.push(num);
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
- Use a stack to keep track of elements for which the next greater element has not been found yet.
- Iterate through the array and update the result array whenever a greater element is found.
- Use an unordered map to store the next greater element for each element in the input array.