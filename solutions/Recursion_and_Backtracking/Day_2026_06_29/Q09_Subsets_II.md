# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). Each subset should not contain duplicate subsets and the order of subsets does not matter. For example, if the input is `[1, 2, 2]`, the output should be `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`.

## Approach
The problem can be solved using recursion and backtracking. The idea is to generate all subsets and skip duplicates by sorting the input array and only considering the next element if it's different from the current one. This way, duplicate subsets are avoided.

## Complexity
- Time: O(2^n * n) where n is the number of elements in the input array, as in the worst case, we generate all possible subsets and sort them.
- Space: O(2^n * n) for storing the result.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(int start, vector<int>& nums, vector<int>& subset, vector<vector<int>>& result) {
    result.push_back(subset);
    for (int i = start; i < nums.size(); i++) {
        // skip duplicates
        if (i > start && nums[i] == nums[i - 1]) continue;
        subset.push_back(nums[i]);
        backtrack(i + 1, nums, subset, result);
        subset.pop_back();
    }
}

vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    vector<vector<int>> result;
    vector<int> subset;
    sort(nums.begin(), nums.end());
    backtrack(0, nums, subset, result);
    return result;
}

int main() {
    vector<int> nums = {1, 2, 2};
    vector<vector<int>> result = subsetsWithDup(nums);
    for (auto& subset : result) {
        for (auto& num : subset) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [1, 2, 2]
Output: 
[ ]
[ 1 ]
[ 1 2 ]
[ 1 2 2 ]
[ 2 ]
[ 2 2 ]
```

## Key Takeaways
- Recursion and backtracking are useful techniques for generating all possible subsets of a set.
- To avoid duplicates in the subsets, sort the input array and skip duplicates by only considering the next element if it's different from the current one.
- The time and space complexity of this solution are O(2^n * n) due to generating all possible subsets and storing them in the result.