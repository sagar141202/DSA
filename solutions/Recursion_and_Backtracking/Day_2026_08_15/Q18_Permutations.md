# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. For example, if the input is `[1, 2, 3]`, a solution set is `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`. The input array will have a length between 1 and 9.

## Approach
We will use recursion and backtracking to generate all permutations. The algorithm will swap each element with the remaining elements to generate all possible permutations.

## Complexity
- Time: O(N!)
- Space: O(N)

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
Output: 
1 2 3 
1 3 2 
2 1 3 
2 3 1 
3 1 2 
3 2 1 
```

## Key Takeaways
- Use recursion and backtracking to solve permutation problems.
- The time complexity for generating all permutations of a set is typically O(N!), where N is the size of the set.
- Use a helper function (`backtrack` in this case) to perform the recursive operation and avoid code duplication.