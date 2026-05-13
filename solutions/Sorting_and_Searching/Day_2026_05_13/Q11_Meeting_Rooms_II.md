# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings. The meetings are represented as intervals where intervals[i] = [start_i, end_i]. If a person can attend all meetings, return 0. Otherwise, return the minimum number of rooms required to hold all meetings. For example, if we have intervals = [[0,30],[5,10],[15,20]], the minimum number of rooms required is 2 because we need two rooms to hold the meetings that start at 5 and 15. We can attend the meeting that starts at 0 in one room, and then use the same room for the meeting that starts at 15 after the meeting that starts at 0 ends.

## Approach
We can solve this problem by sorting the start times and end times separately, then using two pointers to track the current end time and the number of rooms required. If a meeting starts before the current end time, we need a new room. If a meeting ends before the current start time, we can reuse a room.

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

        // Separate the start and end times into different vectors.
        vector<int> startTimes;
        vector<int> endTimes;
        for (auto& interval : intervals) {
            startTimes.push_back(interval[0]);
            endTimes.push_back(interval[1]);
        }

        // Sort the start and end times.
        sort(startTimes.begin(), startTimes.end());
        sort(endTimes.begin(), endTimes.end());

        // Initialize two pointers, one for the start times and one for the end times.
        int startPointer = 0;
        int endPointer = 0;

        // Initialize the number of rooms required and the maximum number of rooms required.
        int roomsRequired = 0;
        int maxRoomsRequired = 0;

        // Iterate over the start times.
        while (startPointer < startTimes.size()) {
            // If a meeting starts before the current end time, we need a new room.
            if (startTimes[startPointer] < endTimes[endPointer]) {
                roomsRequired++;
                startPointer++;
            }
            // If a meeting ends before the current start time, we can reuse a room.
            else {
                roomsRequired--;
                endPointer++;
            }

            // Update the maximum number of rooms required.
            maxRoomsRequired = max(maxRoomsRequired, roomsRequired);
        }

        return maxRoomsRequired;
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
- Sort the start and end times separately to track the current end time and the number of rooms required.
- Use two pointers to iterate over the start times and end times.
- Update the maximum number of rooms required as we iterate over the start times.