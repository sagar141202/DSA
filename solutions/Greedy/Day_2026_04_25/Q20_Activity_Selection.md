# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are given as pairs of start and finish times. The goal is to find the maximum number of non-conflicting activities that can be selected.

## Approach
The algorithm sorts the activities by their finish times and then iterates through the sorted list, selecting the activities that do not conflict with the previously selected activity. This approach ensures that the maximum number of non-conflicting activities are selected. The key insight is to always select the activity with the earliest finish time.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent an activity
struct Activity {
    int start;
    int finish;
};

// Comparison function to sort activities by finish time
bool compareActivities(const Activity& a, const Activity& b) {
    return a.finish < b.finish;
}

// Function to select the maximum number of non-conflicting activities
int selectActivities(vector<Activity>& activities) {
    // Sort the activities by their finish times
    sort(activities.begin(), activities.end(), compareActivities);

    // Initialize the count of selected activities to 1 (the first activity)
    int count = 1;

    // Initialize the finish time of the last selected activity
    int lastFinish = activities[0].finish;

    // Iterate through the sorted list of activities
    for (int i = 1; i < activities.size(); i++) {
        // Check if the current activity does not conflict with the last selected activity
        if (activities[i].start >= lastFinish) {
            // Increment the count of selected activities
            count++;

            // Update the finish time of the last selected activity
            lastFinish = activities[i].finish;
        }
    }

    // Return the maximum number of non-conflicting activities
    return count;
}

int main() {
    // Example usage
    vector<Activity> activities = {{1, 2}, {3, 4}, {0, 6}, {5, 7}, {8, 9}, {5, 9}};
    cout << "Maximum number of non-conflicting activities: " << selectActivities(activities) << endl;
    return 0;
}
```

## Test Cases
```
Input: [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
Output: 4
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (1, 9)]
Output: 3
```

## Key Takeaways
- The greedy approach is used to select the maximum number of non-conflicting activities.
- The activities are sorted by their finish times to ensure that the activity with the earliest finish time is selected first.
- The algorithm has a time complexity of O(n log n) due to the sorting step.