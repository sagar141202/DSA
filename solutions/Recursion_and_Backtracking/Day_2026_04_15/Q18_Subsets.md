# Subsets

## Problem Statement
Given a set of distinct integers, return all possible subsets (the power set). The solution should be implemented using recursion and backtracking. For example, given the set [1, 2, 3], the power set is [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]. The input set will have at most 10 elements, and each element will be between 1 and 100.

## Approach
The algorithm uses recursion to generate all subsets by deciding whether to include or exclude each element from the current subset. Backtracking is used to explore all possible combinations. This approach ensures that all possible subsets are generated.

## Complexity
- Time: O(2^n)
- Space: O(2^n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        backtrack(result, current, nums, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums, int start) {
        result.push_back(current);
        for (int i = start; i < nums.size(); i++) {
            current.push_back(nums[i]);
            backtrack(result, current, nums, i + 1);
            current.pop_back();
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = solution.subsets(nums);
    for (auto& subset : result) {
        cout << "[";
        for (int i = 0; i < subset.size(); i++) {
            cout << subset[i];
            if (i < subset.size() - 1) {
                cout << ", ";
            }
        }
        cout << "]" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [1, 2, 3]
Output: 
[]
[1]
[1, 2]
[1, 2, 3]
[1, 3]
[2]
[2, 3]
[3]
```

## Key Takeaways
- Recursion and backtracking can be used to generate all possible subsets of a given set.
- The time complexity of this approach is exponential (O(2^n)), where n is the number of elements in the input set.
- The space complexity is also exponential (O(2^n)), as we need to store all generated subsets.