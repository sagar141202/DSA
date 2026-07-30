# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. For example, if the input is `[1, 2, 3]`, a solution set is `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`. The input array will not contain duplicates, and the length of the input array will be between 1 and 6.

## Approach
We will use recursion and backtracking to generate all permutations. The algorithm will swap each element with the remaining elements and recursively generate permutations for the remaining elements. Backtracking will be used to restore the original array after each permutation is generated.

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
                // Swap elements
                swap(nums[start], nums[i]);
                // Recur for the remaining elements
                backtrack(result, nums, start + 1);
                // Backtrack and restore the original array
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
- Use recursion and backtracking to generate all permutations of an array.
- The time complexity of this solution is O(n!) due to the generation of all permutations.
- The space complexity is O(n) for the recursive call stack.