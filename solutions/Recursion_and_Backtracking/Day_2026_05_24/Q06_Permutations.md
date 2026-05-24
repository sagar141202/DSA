# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. For example, if the input is `[1, 2, 3]`, the output should be `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`. The input will contain at most 6 numbers, and each number will be between 1 and 9.

## Approach
The problem can be solved using recursion and backtracking. The idea is to choose each number in the collection as the first number in the permutation, and then recursively generate all permutations of the remaining numbers. Backtracking is used to try all possible choices for the first number.

## Complexity
- Time: O(N!), where N is the number of numbers in the collection, because there are N! possible permutations.
- Space: O(N), for the recursion stack.

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
Output: [
  [1, 2, 3],
  [1, 3, 2],
  [2, 1, 3],
  [2, 3, 1],
  [3, 1, 2],
  [3, 2, 1]
]
```

## Key Takeaways
- Recursion and backtracking can be used to solve problems that involve trying all possible combinations or permutations.
- The key to solving permutation problems is to choose each element as the first element in the permutation, and then recursively generate all permutations of the remaining elements.
- Backtracking is used to try all possible choices for the first element.