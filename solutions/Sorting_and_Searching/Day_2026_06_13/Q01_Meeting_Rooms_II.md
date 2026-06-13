# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine the minimum number of rooms required to accommodate all meetings. The intervals are given as pairs of integers, where the first integer represents the start time and the second integer represents the end time. For example, if we have two meetings, one from 0 to 30 and another from 5 to 10, we need two rooms because the two meetings overlap. The input array will have at least one meeting time interval and at most 100,000 intervals. The start and end times are non-negative integers less than 100,000.

## Approach
The algorithm sorts the meeting intervals by start time and uses a priority queue to track the end times of the meetings. By comparing the start time of the next meeting with the smallest end time in the priority queue, we can determine if a new room is needed.

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
        
        // Sort the intervals by start time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        // Priority queue to store the end times
        priority_queue<int, vector<int>, greater<int>> endTimes;
        
        // Initialize the priority queue with the end time of the first meeting
        endTimes.push(intervals[0][1]);
        
        // Iterate over the rest of the meetings
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
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Input: [[7, 10],[2, 4]]
Output: 1
```

## Key Takeaways
- Sort the meeting intervals by start time to ensure that we process the meetings in the correct order.
- Use a priority queue to efficiently track the end times of the meetings and determine the minimum number of rooms required.