# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings. The meetings are represented as intervals where intervals[i] = [start_i, end_i]. If a person can attend all meetings, return 0. Otherwise, return the minimum number of rooms required. For example, if we have intervals = [[0,30],[5,10],[15,20]], the minimum number of rooms required is 2 because we need two rooms to accommodate the meetings that overlap.

## Approach
The algorithm uses a priority queue to track the end times of the meetings. It sorts the meetings by their start times and then iterates over them, updating the priority queue as necessary. If a meeting starts after the earliest end time, it reuses the room; otherwise, it allocates a new room.

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
        // If there are no meetings, we don't need any rooms.
        if (intervals.empty()) return 0;

        // Sort the meetings by their start times.
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        // Initialize a priority queue to store the end times of the meetings.
        priority_queue<int, vector<int>, greater<int>> endTimes;
        endTimes.push(intervals[0][1]);

        // Iterate over the rest of the meetings.
        for (int i = 1; i < intervals.size(); i++) {
            // If the current meeting starts after the earliest end time, reuse the room.
            if (intervals[i][0] >= endTimes.top()) {
                endTimes.pop();
            }
            // Add the end time of the current meeting to the priority queue.
            endTimes.push(intervals[i][1]);
        }

        // The size of the priority queue is the minimum number of rooms required.
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
- Sort the meetings by their start times to process them in chronological order.
- Use a priority queue to efficiently track the end times of the meetings and determine when a room becomes available.
- The size of the priority queue represents the minimum number of rooms required to accommodate all meetings.