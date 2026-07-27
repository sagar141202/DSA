# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are represented as pairs of integers, where the first integer is the start time and the second integer is the finish time. The goal is to maximize the number of activities that can be completed without any conflicts.

## Approach
The algorithm sorts the activities by their finish times and then iterates through the sorted list, selecting the activities that do not conflict with the previously selected activities. This approach ensures that the maximum number of activities can be completed.

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

// Compare function to sort activities by finish time
bool compare(Activity a, Activity b) {
    return a.finish < b.finish;
}

// Function to select the maximum number of activities
int activitySelection(Activity arr[], int n) {
    // Sort the activities by finish time
    sort(arr, arr + n, compare);

    // Initialize the count of selected activities
    int count = 1;

    // Initialize the finish time of the last selected activity
    int lastFinish = arr[0].finish;

    // Iterate through the sorted list of activities
    for (int i = 1; i < n; i++) {
        // Check if the current activity does not conflict with the last selected activity
        if (arr[i].start >= lastFinish) {
            // Increment the count of selected activities
            count++;

            // Update the finish time of the last selected activity
            lastFinish = arr[i].finish;
        }
    }

    // Return the maximum number of activities that can be completed
    return count;
}

int main() {
    // Example usage
    Activity arr[] = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Select the maximum number of activities
    int maxActivities = activitySelection(arr, n);

    // Print the result
    cout << "Maximum number of activities that can be completed: " << maxActivities << endl;

    return 0;
}
```

## Test Cases
```
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: 4
```

## Key Takeaways
- The greedy algorithm is used to solve the activity selection problem by sorting the activities by their finish times.
- The algorithm iterates through the sorted list of activities and selects the activities that do not conflict with the previously selected activities.
- The time complexity of the algorithm is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the activities.