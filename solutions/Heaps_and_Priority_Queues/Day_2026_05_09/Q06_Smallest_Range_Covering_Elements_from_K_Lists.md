# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max], where min and max are the minimum and maximum values in the range. If there are multiple such ranges, return the one with the smallest length. For example, given the lists [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], the smallest range covering elements from all lists is [20, 24].

## Approach
We use a priority queue to keep track of the smallest element from each list. We initialize the queue with the first element from each list, along with the list index and element index. We then repeatedly remove the smallest element from the queue and add the next element from the same list until we find a range that covers at least one element from each list.

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
        // Initialize priority queue with first element from each list
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
        for (int i = 0; i < nums.size(); i++) {
            pq.push({nums[i][0], {i, 0}});
        }

        // Initialize variables to keep track of the smallest range
        int minRange = INT_MAX;
        int maxRange = INT_MIN;
        int minVal = INT_MAX;
        int maxVal = INT_MIN;

        // Initialize set to keep track of lists that have been covered
        unordered_set<int> covered;

        while (!pq.empty()) {
            // Remove smallest element from queue
            int val = pq.top().first;
            int listIdx = pq.top().second.first;
            int elemIdx = pq.top().second.second;
            pq.pop();

            // Update max and min values
            minVal = min(minVal, val);
            maxVal = max(maxVal, val);

            // Add list to covered set
            covered.insert(listIdx);

            // If all lists have been covered, update range
            if (covered.size() == nums.size()) {
                if (maxVal - minVal < minRange) {
                    minRange = maxVal - minVal;
                    maxRange = maxVal;
                }
            }

            // Add next element from same list to queue
            if (elemIdx + 1 < nums[listIdx].size()) {
                pq.push({nums[listIdx][elemIdx + 1], {listIdx, elemIdx + 1}});
            }
        }

        return {maxRange - minRange, maxRange};
    }
};
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
```

## Key Takeaways
- Use a priority queue to keep track of the smallest element from each list.
- Repeatedly remove the smallest element from the queue and add the next element from the same list until a range is found that covers at least one element from each list.
- Keep track of the smallest range found so far and return it at the end.