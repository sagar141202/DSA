# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...](si < ei), determine if a person could attend all meetings. If the person can attend all meetings, return 0. Otherwise, return the minimum number of rooms required. The meeting intervals are non-overlapping when [s1, e1] and [s2, e2] do not satisfy the following conditions: e1 > s2 and e2 > s1. For example, given intervals = [[0,30],[5,10],[15,20]], the minimum number of rooms required is 2 because we need two rooms to accommodate all the meetings.

## Approach
We can solve this problem using a priority queue to keep track of the end times of the meetings. We sort the start times and then iterate over the start times. If the current start time is greater than or equal to the smallest end time, we can reuse the room. Otherwise, we need a new room.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int minMeetingRooms(vector<vector<int>>& intervals) {
    if (intervals.empty()) return 0;
    
    // Sort the intervals by start time
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    
    // Initialize a priority queue to store the end times
    priority_queue<int, vector<int>, greater<int>> endTimes;
    
    // Add the first end time to the priority queue
    endTimes.push(intervals[0][1]);
    
    // Iterate over the rest of the intervals
    for (int i = 1; i < intervals.size(); i++) {
        // If the current start time is greater than or equal to the smallest end time, reuse the room
        if (intervals[i][0] >= endTimes.top()) {
            endTimes.pop();
        }
        // Add the current end time to the priority queue
        endTimes.push(intervals[i][1]);
    }
    
    // The size of the priority queue is the minimum number of rooms required
    return endTimes.size();
}
```

## Test Cases
```
Input: [[0,30],[5,10],[15,20]]
Output: 2
Input: [[7,10],[2,4]]
Output: 1
```

## Key Takeaways
- Use a priority queue to keep track of the end times of the meetings.
- Sort the start times to ensure that we can reuse rooms when possible.
- The size of the priority queue is the minimum number of rooms required.