# Python script that compares two lists of lists based on a specified element index (e.g., compare element [i] from each sublist). It returns a new list with:
# - element[0]: the compared value
# - element[1]: index in list1 (or None if not found)
# - element[2]: index in list2 (or None if not found)
# - element[3]: result text: "found", "not in list1", or "not in list2"


def compare_lists(list1, list2, index1, index2):
    result = []
    values1 = [row[index1] for row in list1 if len(row) > index1]
    values2 = [row[index2] for row in list2 if len(row) > index2]

    all_values = set(values1).union(values2)

    for value in all_values:
        idx1 = next((i for i, row in enumerate(list1) if len(row) > index1 and row[index1] == value), None)
        idx2 = next((i for i, row in enumerate(list2) if len(row) > index2 and row[index2] == value), None)

        if idx1 is not None and idx2 is not None:
            status = "found"
        elif idx1 is None:
            status = "not in list1"
        else:
            status = "not in list2"

        result.append([value, idx1, idx2, status])

    return result

# Example usage
list1 = [['apple', 1], ['banana', 2], ['cherry', 3]]
list2 = [['banana', 5], ['date', 6], ['apple', 7]]

# Compare element 0 from each sublist
comparison = compare_lists(list1, list2, 0, 0)

for row in comparison:
    print(row)
