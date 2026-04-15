# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings. If not, find the minimum number of meeting rooms required. The meeting time intervals are non-overlapping and are given in the form [start, end]. The start time is inclusive and the end time is exclusive. For example, [0, 30] means a meeting starts at 0 and ends at 30. The minimum number of meeting rooms required should be returned.

## Approach
We can use a priority queue to keep track of the end times of the meetings. We sort the start times and then iterate through them, updating the priority queue accordingly. If a meeting starts after the earliest end time, we can reuse the room, otherwise, we need a new room.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int minMeetingRooms(vector<vector<int>>& intervals) {
    if (intervals.empty()) return 0;
    
    // Sort the start times
    sort(intervals.begin(), intervals.end());
    
    // Priority queue to store the end times
    priority_queue<int, vector<int>, greater<int>> endTimes;
    
    // Add the first meeting's end time
    endTimes.push(intervals[0][1]);
    
    // Iterate through the rest of the meetings
    for (int i = 1; i < intervals.size(); i++) {
        // If the current meeting starts after the earliest end time, reuse the room
        if (intervals[i][0] >= endTimes.top()) {
            endTimes.pop();
        }
        // Add the current meeting's end time
        endTimes.push(intervals[i][1]);
    }
    
    // The size of the priority queue is the minimum number of rooms required
    return endTimes.size();
}
```

## Test Cases
```
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Input: [[7, 10],[2, 4]]
Output: 1
```

## Key Takeaways
- Use a priority queue to efficiently track the end times of the meetings.
- Sort the start times to ensure correct ordering of meetings.
- Reuse rooms when possible to minimize the number of rooms required.