# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine the minimum number of rooms required to accommodate all meetings. Each meeting is represented as an interval [start, end], and two meetings can share the same room if they do not overlap. The input array of intervals is not guaranteed to be sorted. For example, given intervals [[0, 30], [5, 10], [15, 20]], the minimum number of rooms required is 2.

## Approach
We can solve this problem by sorting the start and end times separately and then using two pointers to track the current end time and the next start time. This approach allows us to determine the minimum number of rooms required at each time step. We utilize a priority queue to keep track of the end times of the meetings.

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

        // Separate the start and end times into different vectors and sort them.
        vector<int> startTimes, endTimes;
        for (auto& interval : intervals) {
            startTimes.push_back(interval[0]);
            endTimes.push_back(interval[1]);
        }
        sort(startTimes.begin(), startTimes.end());
        sort(endTimes.begin(), endTimes.end());

        // Initialize two pointers, one for the start times and one for the end times.
        int startPtr = 0, endPtr = 0;
        int rooms = 0, maxRooms = 0;

        // Use a priority queue to store the end times.
        priority_queue<int, vector<int>, greater<int>> endTimesPQ;

        // Iterate through the start times.
        while (startPtr < startTimes.size()) {
            // If the current meeting starts after the earliest end time, update the earliest end time.
            if (!endTimesPQ.empty() && startTimes[startPtr] >= endTimesPQ.top()) {
                endTimesPQ.pop();
            }

            // Add the current meeting's end time to the priority queue.
            endTimesPQ.push(intervals[startPtr][1]);

            // Update the maximum number of rooms required.
            maxRooms = max(maxRooms, (int)endTimesPQ.size());

            // Move to the next meeting.
            startPtr++;
        }

        return maxRooms;
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
- We can use a priority queue to efficiently track the end times of the meetings.
- Sorting the start and end times allows us to determine the minimum number of rooms required at each time step.
- The time complexity of the solution is O(n log n) due to the sorting operation.