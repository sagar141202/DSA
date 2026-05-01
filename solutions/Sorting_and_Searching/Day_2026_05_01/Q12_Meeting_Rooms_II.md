# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...](si < ei), determine if a person could attend all meetings. If the person can attend all meetings, the function should return 0. Otherwise, it should return the minimum number of rooms required. The intervals are non-overlapping when [s1, e1] and [s2, e2] do not overlap, i.e., s1 >= e2 or s2 >= e1. For example, given intervals [[0,30],[5,10],[15,20]], the function should return 2 because two rooms are needed to accommodate all meetings.

## Approach
We will use a priority queue to store the end times of the meetings. The intuition is to always try to assign a meeting to an existing room. If no room is available, we add a new room. We sort the start times and iterate through them, updating the end times in the priority queue.

## Complexity
- Time: O(N log N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        
        // Sort the intervals by start time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        // Priority queue to store the end times
        priority_queue<int, vector<int>, greater<int>> endTimes;
        
        // Initialize the priority queue with the end time of the first meeting
        endTimes.push(intervals[0][1]);
        
        // Iterate through the rest of the meetings
        for (int i = 1; i < intervals.size(); i++) {
            // If the current meeting starts after the earliest end time, update the earliest end time
            if (intervals[i][0] >= endTimes.top()) {
                endTimes.pop();
            }
            // Add the end time of the current meeting to the priority queue
            endTimes.push(intervals[i][1]);
        }
        
        // The size of the priority queue is the minimum number of rooms required
        return endTimes.size();
    }
};
```

## Test Cases
```
Input: [[0,30],[5,10],[15,20]]
Output: 2
Input: [[7,10],[2,4]]
Output: 1
```

## Key Takeaways
- Use a priority queue to efficiently store and update the end times of the meetings.
- Sort the start times to ensure that we process the meetings in the correct order.
- The size of the priority queue at the end is the minimum number of rooms required to accommodate all meetings.