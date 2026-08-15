# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine the minimum number of conference rooms required. The intervals are represented as pairs of integers, where the first integer is the start time and the second integer is the end time. For example, if we have intervals [(0, 30), (5, 10), (15, 20)], we would need at least 2 conference rooms because the intervals (0, 30) and (5, 10) overlap, and the intervals (5, 10) and (15, 20) also overlap. The input intervals are non-empty and the start time is always less than the end time.

## Approach
We can solve this problem using a priority queue to keep track of the end times of the meetings. The idea is to sort the intervals by their start times and then iterate over them, using the priority queue to find the meeting room that will be available the earliest. If the earliest available room is still occupied when a new meeting starts, we need to allocate a new room.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        
        // Sort the intervals by their start times
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        // Initialize a priority queue to store the end times of the meetings
        priority_queue<int, vector<int>, greater<int>> endTimes;
        
        // Initialize the minimum number of rooms required
        int minRooms = 0;
        
        // Iterate over the intervals
        for (const auto& interval : intervals) {
            // If the earliest available room is still occupied when a new meeting starts, we need to allocate a new room
            if (!endTimes.empty() && endTimes.top() <= interval[0]) {
                endTimes.pop();
            }
            
            // Add the end time of the current meeting to the priority queue
            endTimes.push(interval[1]);
            
            // Update the minimum number of rooms required
            minRooms = max(minRooms, (int)endTimes.size());
        }
        
        return minRooms;
    }
};
```

## Test Cases
```
Input: intervals = [[0, 30],[5, 10],[15, 20]]
Output: 2
Input: intervals = [[7, 10],[2, 4]]
Output: 1
```

## Key Takeaways
- We can use a priority queue to efficiently find the meeting room that will be available the earliest.
- Sorting the intervals by their start times is crucial to ensure that we are considering the meetings in the correct order.
- The minimum number of rooms required is equal to the maximum size of the priority queue at any point during the iteration.