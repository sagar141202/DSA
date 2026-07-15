# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine the minimum number of conference rooms required. The intervals are represented as pairs of integers, where the first integer is the start time and the second integer is the end time. For example, if we have intervals [(0, 30), (5, 10), (15, 20)], we need at least 2 rooms because the meeting from 5 to 10 overlaps with the meeting from 0 to 30, and the meeting from 15 to 20 overlaps with both. However, if we have intervals [(5, 8), (9, 15)], we only need 1 room because the two meetings do not overlap.

## Approach
We will use a priority queue to store the end times of the meetings. The idea is to always try to assign a meeting to an existing room before assigning it to a new room. We sort the intervals by their start times and then iterate over them, assigning each meeting to the room that becomes available the earliest.

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
        // If there are no intervals, we don't need any rooms
        if (intervals.empty()) {
            return 0;
        }

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
            // If the meeting starts after the earliest end time, update the earliest end time
            if (!endTimes.empty() && interval[0] >= endTimes.top()) {
                endTimes.pop();
            }

            // Add the end time of the current meeting to the priority queue
            endTimes.push(interval[1]);

            // Update the minimum number of rooms required
            minRooms = max(minRooms, (int)endTimes.size());
        }

        // Return the minimum number of rooms required
        return minRooms;
    }
};
```

## Test Cases
```
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Input: [[5, 8],[9, 15]]
Output: 1
Input: []
Output: 0
```

## Key Takeaways
- We use a priority queue to store the end times of the meetings, allowing us to efficiently find the earliest available room.
- We sort the intervals by their start times to ensure that we process the meetings in the correct order.
- The time complexity is O(n log n) due to the sorting and priority queue operations.