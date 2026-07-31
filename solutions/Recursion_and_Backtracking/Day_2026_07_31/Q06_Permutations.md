# Permutations

## Problem Statement
Generate all possible permutations of a given array of integers. The array may contain duplicate elements. The solution should be able to handle arrays of varying lengths. For example, given the array `[1, 2, 3]`, the output should be `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`. The solution should be efficient and scalable.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will start by selecting the first element, then recursively generate all permutations of the remaining elements, and finally backtrack to explore other possibilities. This process will be repeated until all elements have been selected.

## Complexity
- Time: O(n!)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, int start, vector<vector<int>>& result) {
    if (start == nums.size()) {
        result.push_back(nums);
        return;
    }
    for (int i = start; i < nums.size(); i++) {
        swap(nums[start], nums[i]);
        backtrack(nums, start + 1, result);
        swap(nums[start], nums[i]);
    }
}

vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> result;
    backtrack(nums, 0, result);
    return result;
}

int main() {
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = permute(nums);
    for (auto& permutation : result) {
        for (auto& num : permutation) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
Input: [0, 1]
Output: [[0, 1], [1, 0]]
```

## Key Takeaways
- Recursion and backtracking can be used to generate all permutations of an array.
- The time complexity of this solution is O(n!), where n is the length of the array, because there are n! possible permutations.
- The space complexity is O(n) due to the recursive call stack.