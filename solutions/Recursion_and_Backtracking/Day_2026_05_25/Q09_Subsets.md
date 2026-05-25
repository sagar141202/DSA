# Subsets

## Problem Statement
Given a set of distinct integers, generate all possible subsets. The set is defined as a list of unique integers, and a subset is a list of integers that are all present in the original set. The subsets can be of any size, from 0 to the size of the original set. For example, if the input is [1, 2, 3], the output should be [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]. The input set will contain at most 10 integers, and each integer will be between 1 and 100.

## Approach
The solution uses recursion and backtracking to generate all subsets. It iterates over each element in the set, and for each element, it recursively generates all subsets that include the current element and all subsets that do not include the current element. This approach ensures that all possible subsets are generated. The base case for the recursion is when the current index is equal to the size of the set, at which point an empty subset is added to the result.

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

    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums, int index) {
        // base case: add current subset to result
        result.push_back(current);
        
        // recursive case: iterate over remaining elements
        for (int i = index; i < nums.size(); i++) {
            // add current element to subset
            current.push_back(nums[i]);
            // recurse with updated subset and index
            backtrack(result, current, nums, i + 1);
            // backtrack: remove current element from subset
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
- Recursion and backtracking can be used to generate all possible subsets of a set.
- The time complexity of this approach is O(2^n), where n is the size of the input set.
- The space complexity of this approach is also O(2^n), as in the worst case, all subsets need to be stored in memory.