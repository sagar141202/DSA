# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings. The meetings are non-overlapping if a meeting ends before the next meeting starts. The input is an array of intervals where intervals[i] = [start_i, end_i]. The constraint is that 1 <= intervals.length <= 10^5 and 0 <= start_i < end_i <= 10^9.

## Approach
We can use a priority queue to store the end times of the meetings. We sort the meetings by their start times and then iterate over the meetings. If the current meeting starts after the earliest end time, we update the earliest end time. Otherwise, we need to add a new room.

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
            // If the current meeting starts after the earliest end time, we can reuse the room.
            if (intervals[i][0] >= endTimes.top()) {
                endTimes.pop();
            }
            // Add the end time of the current meeting to the queue.
            endTimes.push(intervals[i][1]);
        }

        // The size of the queue is the minimum number of rooms needed.
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
- We can use a priority queue to efficiently manage the end times of the meetings.
- Sorting the meetings by their start times allows us to iterate over them in a way that minimizes the number of rooms needed.
- The size of the priority queue at the end of the iteration is the minimum number of rooms required.