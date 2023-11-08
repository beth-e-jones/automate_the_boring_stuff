"""
Regular expressions allow us to specify a pattern of text to search for e.g.,
415-555-1234 is a US phone number but 4,155,551,234 is not
Can check this manually using python by checking a string of numbers is exactly
12 characters, each secion contains only numeric characters, and the pattern is
correct with hyphens between area codes. However, this is a long winded way of
doing this. it's also an issue because if you wanted to find a phone number
within a larger string, you'd have to add more code to spot the number pattern
(see the example)

It's easier to find patterns with regular expressions - called regexes for 
short. These are descriptions of any pattern of text e.g., \d is a digit
so \d\d\d-\d\d\d-\d\d\d\d would represent a US phone number, but ({3}) will
tell Python to replicate that pattern 3 times, so  \d{3}-\d{3}-\d{4} will also
do the job.
"""