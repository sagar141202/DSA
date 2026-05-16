# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max], where min and max are the minimum and maximum values in the range, respectively. The range should be as small as possible, i.e., the difference between max and min should be minimized. For example, if we have three lists [4,10,15,24,26], [0,9,12,20], and [5,18,22,30], the smallest range covering elements from all lists is [20,24].

## Approach
The approach involves using a priority queue to keep track of the smallest element from each list. We initialize the priority queue with the first element from each list, along with the list index and element index. Then, we repeatedly extract the smallest element from the priority queue and add the next element from the same list to the priority queue.

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
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
        for (int i = 0; i < nums.size(); i++) {
            pq.push({nums[i][0], i, 0});
        }

        // Initialize variables to track smallest range
        int minRange = INT_MAX;
        int minVal = INT_MIN;
        int maxVal = INT_MAX;

        // Initialize set to track lists that have been covered
        unordered_set<int> covered;

        // Repeatedly extract smallest element from priority queue
        while (!pq.empty()) {
            auto [val, listIndex, elementIndex] = pq.top();
            pq.pop();

            // Update maxVal if necessary
            maxVal = max(maxVal, val);

            // Add listIndex to covered set
            covered.insert(listIndex);

            // If all lists have been covered, update smallest range if necessary
            if (covered.size() == nums.size()) {
                if (maxVal - val < minRange) {
                    minRange = maxVal - val;
                    minVal = val;
                }
            }

            // Add next element from same list to priority queue if possible
            if (elementIndex + 1 < nums[listIndex].size()) {
                pq.push({nums[listIndex][elementIndex + 1], listIndex, elementIndex + 1});
            } else {
                // If no more elements in list, remove listIndex from covered set
                covered.erase(listIndex);
            }
        }

        return {minVal, minVal + minRange};
    }
};
```

## Test Cases
```
Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
```

## Key Takeaways
- Use a priority queue to efficiently track the smallest element from each list.
- Keep track of the smallest range seen so far and update it as necessary.
- Use a set to track which lists have been covered to ensure that the smallest range covers at least one element from each list.