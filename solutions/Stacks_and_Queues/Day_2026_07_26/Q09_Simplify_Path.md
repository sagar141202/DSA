# Simplify Path

## Problem Statement
Given an absolute path to a file in a Unix-style file system, simplify the path by resolving the '.' and '..' directories. The '.' directory refers to the current directory, and the '..' directory refers to the parent directory. The path is guaranteed to start with a '/', and all directories will be separated by '/'. There will be no '.' or '..' at the beginning of the path. The path will not contain any empty directories, and the path will not end with a '/'. For example, "/home/" should be simplified to "/home", and "/../" should be simplified to "/". If the simplified path does not start with a '/', it is invalid, so return "/".

## Approach
We will use a stack to keep track of the directories in the path. When we encounter a '..', we will pop the last directory from the stack if it is not empty. When we encounter a '.', we will skip it. Otherwise, we will push the directory to the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stack;
        string dir = "";
        
        // Split the path into directories
        for (char c : path) {
            if (c == '/') {
                if (dir != "" && dir != "." && dir != "..") {
                    stack.push_back(dir);
                } else if (dir == ".." && !stack.empty()) {
                    stack.pop_back();
                }
                dir = "";
            } else {
                dir += c;
            }
        }
        
        // Handle the last directory
        if (dir != "" && dir != "." && dir != "..") {
            stack.push_back(dir);
        } else if (dir == ".." && !stack.empty()) {
            stack.pop_back();
        }
        
        // Build the simplified path
        string simplifiedPath = "";
        for (string dir : stack) {
            simplifiedPath += "/" + dir;
        }
        
        // Return the simplified path, or "/" if it is empty
        return simplifiedPath == "" ? "/" : simplifiedPath;
    }
};
```

## Test Cases
```
Input: "/home/"
Output: "/home"
Input: "/../"
Output: "/"
Input: "/home//foo/"
Output: "/home/foo"
Input: "/a/./b/../../c/"
Output: "/c"
```

## Key Takeaways
- Use a stack to keep track of the directories in the path.
- Handle the '.' and '..' directories correctly by skipping or popping from the stack.
- Build the simplified path by concatenating the directories in the stack.