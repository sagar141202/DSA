# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are given as pairs of start and finish times. The goal is to find the maximum number of activities that can be selected such that no two activities overlap.

## Approach
The algorithm sorts the activities based on their finish times and then iterates through the sorted list, selecting the activities that do not overlap with the previously selected activity. This approach ensures that the maximum number of activities are selected.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent an activity
struct Activity {
    int start;
    int finish;
};

// Comparison function to sort activities based on finish time
bool compareActivities(const Activity &a, const Activity &b) {
    return a.finish < b.finish;
}

// Function to select the maximum number of activities
int selectActivities(Activity activities[], int n) {
    // Sort the activities based on finish time
    sort(activities, activities + n, compareActivities);

    // Initialize the count of selected activities
    int count = 1;

    // Initialize the finish time of the last selected activity
    int lastFinish = activities[0].finish;

    // Iterate through the sorted list of activities
    for (int i = 1; i < n; i++) {
        // Check if the current activity does not overlap with the last selected activity
        if (activities[i].start >= lastFinish) {
            // Increment the count of selected activities
            count++;

            // Update the finish time of the last selected activity
            lastFinish = activities[i].finish;
        }
    }

    // Return the maximum number of selected activities
    return count;
}

int main() {
    // Example usage
    Activity activities[] = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    int n = sizeof(activities) / sizeof(activities[0]);

    int maxActivities = selectActivities(activities, n);

    cout << "Maximum number of activities: " << maxActivities << endl;

    return 0;
}
```

## Test Cases
```
Input: activities = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
Output: Maximum number of activities: 4
```

## Key Takeaways
- The greedy algorithm is used to solve the activity selection problem by sorting the activities based on their finish times.
- The algorithm iterates through the sorted list of activities and selects the activities that do not overlap with the previously selected activity.
- The time complexity of the algorithm is O(n log n) due to the sorting operation, and the space complexity is O(1) as no extra space is required.