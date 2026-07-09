# Simplify Path

## Problem Statement
Given an absolute path, simplify it by resolving '..' and '.' in the path. The path is made up of a sequence of directories separated by '/'. Here are the rules for simplifying a path: 
- '.' is the current directory, so it can be ignored.
- '..' is the parent directory, so it moves up one level from the current directory.
- If the simplified path starts with a '/', it means it is an absolute path.
- The path "/../" should return "/" since going to the parent directory of the root directory is still the root directory.
- The path "/home//" should return "/home" since multiple consecutive '/' characters are equivalent to a single '/'.
- The path "/a/./b/../../c/" should return "/a/c".

## Approach
To simplify a path, we can use a stack data structure to store the directories. We iterate over each directory in the path, and if the directory is not '.' or '..', we push it to the stack. If the directory is '..', we pop the last directory from the stack if it's not empty. Finally, we construct the simplified path from the stack.

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
        stack<string> st;
        string res = "";
        string word = "";
        
        // split the path by '/' and process each directory
        for (char c : path) {
            if (c == '/') {
                if (word == "..") {
                    if (!st.empty()) {
                        st.pop();
                    }
                } else if (word != "" && word != ".") {
                    st.push(word);
                }
                word = "";
            } else {
                word += c;
            }
        }
        
        // process the last directory
        if (word == "..") {
            if (!st.empty()) {
                st.pop();
            }
        } else if (word != "" && word != ".") {
            st.push(word);
        }
        
        // construct the simplified path
        while (!st.empty()) {
            res = "/" + st.top() + res;
            st.pop();
        }
        
        // return the simplified path
        return res == "" ? "/" : res;
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
Output: "/a/c"
```

## Key Takeaways
- Use a stack to store the directories and simplify the path by resolving '..' and '.'.
- Handle edge cases such as the path starting with '/' or containing consecutive '/' characters.
- Construct the simplified path from the stack by prepending each directory with '/'.