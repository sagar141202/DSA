# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max], where min and max are the minimum and maximum values in the range. If there are multiple such ranges with the same length, return the one with the smallest min value. For example, given the lists [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], the smallest range covering elements from all lists is [20, 24].

## Approach
The approach involves using a priority queue to keep track of the smallest element from each list. We initialize the priority queue with the first element from each list and then iteratively remove the smallest element and add the next element from the same list. The range is updated whenever we find a smaller range that covers at least one element from each list.

## Complexity
- Time: O(N log K)
- Space: O(K)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
        int mx = INT_MIN;
        for (int i = 0; i < nums.size(); i++) {
            pq.push({nums[i][0], {i, 0}});
            mx = max(mx, nums[i][0]);
        }
        int ans = INT_MAX, st = -1, en = -1;
        while (pq.size() == nums.size()) {
            auto [val, idx] = pq.top();
            pq.pop();
            if (mx - val < ans) {
                ans = mx - val;
                st = val;
                en = mx;
            }
            if (idx.second + 1 < nums[idx.first].size()) {
                pq.push({nums[idx.first][idx.second + 1], {idx.first, idx.second + 1}});
                mx = max(mx, nums[idx.first][idx.second + 1]);
            } else {
                break;
            }
        }
        return {st, en};
    }
};
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
```

## Key Takeaways
- We use a priority queue to efficiently find the smallest element from each list.
- We keep track of the maximum value seen so far to calculate the range.
- We update the range whenever we find a smaller range that covers at least one element from each list.