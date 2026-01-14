#Write a program that finds the longest intersection. You will be given a number N.
# On each of the next N lines you will be given two ranges in the format:
# "{first_start},{first_end}-{second_start},{second_end}".
# You should find the intersection of these two ranges.
# The start and end numbers in the ranges are inclusive.
#Finally, you should find the longest intersection of all N intersections, print the
# numbers that are included and its length in the format:
# "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
#Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one.

def realizing_intersection(string):
    start, end = string.split(",")
    return set(range(int(start), int(end) + 1))

longest_intersection = set()

for intersection in range(int(input())):
    first, second = input().split("-")
    first_set = realizing_intersection(first)
    second_set = realizing_intersection(second)
    union = first_set.intersection(second_set)
    if len(union) > len(longest_intersection):
        longest_intersection = union
    else:
        pass

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")


