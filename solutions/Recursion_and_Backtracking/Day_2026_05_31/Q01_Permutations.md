# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. For example, if the input is `[1, 2, 3]`, a solution set is `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`. The input will contain unique integers and the length of the input array will be between 1 and 6.

## Approach
We can solve this problem using backtracking, a form of recursion. The idea is to fix one element at a time and recursively generate all permutations of the remaining elements. We will use a helper function to swap elements and explore different branches of the permutation tree.

## Complexity
- Time: O(N * N!)
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
                // Swap elements
                swap(nums[start], nums[i]);
                // Recur for the next element
                backtrack(result, nums, start + 1);
                // Backtrack and swap back
                swap(nums[start], nums[i]);
            }
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = solution.permute(nums);
    for (auto vec : result) {
        for (auto num : vec) {
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
- Use backtracking to generate all permutations by fixing one element at a time.
- Swap elements to explore different branches of the permutation tree.
- Backtrack and swap back after exploring each branch to maintain the original array.