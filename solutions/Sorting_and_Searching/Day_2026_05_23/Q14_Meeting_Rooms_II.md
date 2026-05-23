# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine the minimum number of rooms required to accommodate all meetings. Each meeting requires one room, and a room can be reused once a meeting ends. The input array will have intervals in the format [start, end], where start and end are integers representing the start and end times of a meeting. For example, given the intervals [[0, 30], [5, 10], [15, 20]], the minimum number of rooms required is 2.

## Approach
The algorithm uses a priority queue to keep track of the end times of the meetings. It sorts the meetings by their start times and then iterates over them, assigning each meeting to a room and updating the end time of the room. The priority queue ensures that the room with the earliest end time is always used first.

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

        // Sort the meetings by their start times.
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        // Initialize a priority queue to store the end times of the meetings.
        priority_queue<int, vector<int>, greater<int>> endTimes;

        // Initialize the minimum number of rooms required.
        int minRooms = 0;

        // Iterate over the meetings.
        for (const auto& interval : intervals) {
            // If the meeting starts after the earliest end time, we can reuse the room.
            if (!endTimes.empty() && interval[0] >= endTimes.top()) {
                endTimes.pop();
            }

            // Add the meeting to a room and update the end time.
            endTimes.push(interval[1]);

            // Update the minimum number of rooms required.
            minRooms = max(minRooms, (int)endTimes.size());
        }

        return minRooms;
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
- We can use a priority queue to efficiently manage the end times of the meetings.
- Sorting the meetings by their start times ensures that we can reuse rooms as soon as possible.
- The minimum number of rooms required is equal to the maximum size of the priority queue at any point.