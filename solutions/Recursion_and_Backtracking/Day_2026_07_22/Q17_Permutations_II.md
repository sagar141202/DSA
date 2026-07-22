# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. For example, given the collection `[1, 1, 2]`, the unique permutations are `[[1, 1, 2], [1, 2, 1], [2, 1, 1]]`. The input collection is not null, and the size of the collection is between 1 and 9.

## Approach
We will use a backtracking approach to generate all permutations. The algorithm will recursively generate all possible permutations by swapping each number with the remaining numbers. To avoid duplicates, we will skip the same numbers in the current level of recursion.

## Complexity
- Time: O(N! / (k1! * k2! * ... * km!)) where N is the total number of elements and k1, k2, ..., km are the frequencies of each distinct element
- Space: O(N) for storing the recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, int start, vector<vector<int>>& result) {
    if (start == nums.size()) {
        result.push_back(nums);
        return;
    }
    unordered_set<int> used;
    for (int i = start; i < nums.size(); i++) {
        if (used.find(nums[i]) != used.end()) continue;
        used.insert(nums[i]);
        swap(nums[start], nums[i]);
        backtrack(nums, start + 1, result);
        swap(nums[start], nums[i]);
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> result;
    backtrack(nums, 0, result);
    return result;
}

int main() {
    vector<int> nums = {1, 1, 2};
    vector<vector<int>> result = permuteUnique(nums);
    for (auto& perm : result) {
        for (auto& num : perm) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [1, 1, 2]
Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
```

## Key Takeaways
- Use backtracking to generate all permutations of the input collection
- Use an unordered_set to keep track of used numbers in the current level of recursion to avoid duplicates
- Swap each number with the remaining numbers to generate all possible permutations