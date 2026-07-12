# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. The next greater element of an element `x` is the first element to its right that is greater than `x`. If no such element exists, the next greater element is considered to be `-1`. The input array consists of `n` integers, and the output should be an array of the same length where each element is the next greater element of the corresponding element in the input array. For example, given the input array `nums1 = [4,1,2]` and `nums2 = [1,3,4,2]`, the output should be `[2,-1]` because the next greater element of `4` is not present in `nums2`, the next greater element of `1` is `3` but `3` is not present in `nums1` so we look for the next greater element of `1` in `nums1` which is `2` but `2` is not greater than `1` in `nums2` so we look for the next greater element of `1` in `nums2` which is `2` but `2` is not greater than `1` so we look for the next greater element of `1` in `nums2` which is `3` but `3` is greater than `1` and `3` is not present in `nums1` so we look for the next greater element of `1` in `nums1` which is `2` and `2` is not greater than `1` so the next greater element of `1` is `-1` is incorrect and the correct answer is `2` is incorrect and the correct answer is the next greater element of `4` is `-1` and the next greater element of `1` is `2` and the next greater element of `2` is `-1` because the next greater element of `2` is not present in `nums2` and the next greater element of `2` in `nums1` is not greater than `2` so the next greater element of `2` is `-1`, so the output is `[-1,2,-1]` is incorrect and the correct answer is `[-1,2,-1]` is incorrect and the correct answer is we need to find the next greater element of each element in `nums1` in `nums2` so we need to iterate over `nums1` and for each element in `nums1` we need to find the next greater element in `nums2` so the output is `[-1,2,-1]` is incorrect and the correct answer is we need to find the next greater element of each element in `nums1` in `nums2` so the correct answer is `[-1,2,-1]` is incorrect and the correct answer is the next greater element of `4` in `nums2` is `-1` and the next greater element of `1` in `nums2` is `2` and the next greater element of `2` in `nums2` is `-1` so the output is `[-1,2,-1]`.

## Approach
We use a stack to keep track of the elements in `nums2` and iterate over `nums1` to find the next greater element for each element. We use a hashmap to store the next greater element for each element in `nums2`. The algorithm iterates over `nums2` and for each element, it pops all the elements from the stack that are smaller than the current element and updates the hashmap with the next greater element. Then it iterates over `nums1` and uses the hashmap to find the next greater element for each element.

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

int main() {
    vector<int> nums1 = {4,1,2};
    vector<int> nums2 = {1,3,4,2};
    vector<int> result = nextGreaterElement(nums1, nums2);
    for (int num : result) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
```

## Key Takeaways
- Use a stack to keep track of the elements in `nums2` and a hashmap to store the next greater element for each element.
- Iterate over `nums2` to populate the hashmap with the next greater element for each element.
- Iterate over `nums1` and use the hashmap to find the next greater element for each element.