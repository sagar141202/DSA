# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings. If not, find the minimum number of meeting rooms required to hold all meetings. The meeting intervals are non-overlapping and are given in the format [start, end]. For example, given the intervals [[0, 30], [5, 10], [15, 20]], the minimum number of meeting rooms required is 2.

## Approach
We can use a priority queue to store the end times of the meetings. We sort the start times and iterate through them, updating the priority queue as we go. If a meeting starts after the earliest end time, we can reuse the room.

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
        if (intervals.empty()) {
            return 0;
        }

        // Sort the meetings by start time.
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        // Use a priority queue to store the end times of the meetings.
        priority_queue<int, vector<int>, greater<int>> endTimes;
        endTimes.push(intervals[0][1]);

        // Iterate through the rest of the meetings.
        for (int i = 1; i < intervals.size(); i++) {
            // If the current meeting starts after the earliest end time, we can reuse the room.
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
Input: [[0, 30], [5, 10], [15, 20]]
Output: 2
Input: [[7, 10], [2, 4]]
Output: 1
```

## Key Takeaways
- Use a priority queue to efficiently manage the end times of the meetings.
- Sort the start times to ensure we process the meetings in the correct order.
- Reuse rooms when possible to minimize the number of rooms required.