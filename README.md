# unhardwrap

Take a txt file that has been hard-wrapped and remove the hardwrapping.

Use like:

    ./unhardwrap < example_in.txt > example_out.txt

This takes text, for example: (line numbers added for clarity)

    1. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    2. incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    3. nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    4. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
    5. fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
    6. culpa qui officia deserunt mollit anim id est laborum.

And produces output without the hardwrapped newlines, like: (line numbers added for clarity)

    1. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    2. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

The rules are:

* Two adjacent lines are considered to have been hardwrapped and should be remerged, if the first line ends with a letter, comma or hyphen.
* But don't merge if the second line starts with a space or utf8 opening quote.
* Everything between utf8 speechmarks “..” will be treated as one line.
