# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. The input is a list of integers, and the output should be a list of lists, where each sublist is a permutation of the input list. For example, given the input [1, 2, 3], the output should be [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]. The length of the input list is between 1 and 6, and the elements are between 1 and 100.

## Approach
The problem can be solved using recursion and backtracking. The idea is to choose each element in the list as the first element of the permutation and then recursively generate all permutations of the remaining elements. The base case is when the list is empty, in which case the only permutation is an empty list.

## Complexity
- Time: O(n!)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        backtrack(result, nums, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& nums, int start) {
        if (start == nums.size()) {
            result.push_back(nums);
        } else {
            for (int i = start; i < nums.size(); i++) {
                swap(nums[start], nums[i]);
                backtrack(result, nums, start + 1);
                swap(nums[start], nums[i]);
            }
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = solution.permute(nums);
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
```

## Key Takeaways
- Use recursion and backtracking to generate all permutations of a list.
- The time complexity is O(n!) because there are n! permutations of a list of length n.
- The space complexity is O(n) because the maximum depth of the recursion tree is n.