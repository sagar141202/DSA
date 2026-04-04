# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings. However, in this variation, we need to find the minimum number of meeting rooms required such that all meetings can be accommodated. Each meeting room can hold one meeting at a time. The meeting intervals are non-negative and are represented as pairs of integers (start, end). For example, (0, 30) represents a meeting from 0 to 30 minutes. If two meetings have the same start time, they can be accommodated in two separate rooms.

## Approach
We will use a priority queue to keep track of the end times of the meetings. The idea is to sort the meetings by their start times and then iterate over them, assigning each meeting to the room that becomes available the earliest. If no room is available, we add a new room.

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
        
        // Sort the meetings by their start times
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        // Initialize a priority queue to store the end times of the meetings
        priority_queue<int, vector<int>, greater<int>> endTimes;
        
        // Add the end time of the first meeting to the priority queue
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
        
        // The size of the priority queue is the minimum number of meeting rooms required
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
- Use a priority queue to efficiently manage the end times of the meetings.
- Sort the meetings by their start times to ensure that we are always considering the meeting that starts the earliest.
- The minimum number of meeting rooms required is equal to the size of the priority queue at the end of the algorithm.