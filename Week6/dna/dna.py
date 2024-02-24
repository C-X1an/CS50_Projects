import csv
import sys


def main():

    long_list = ['AGATC', 'TTTTTTCT', 'AATG', 'TCTAG', 'GATA', 'TATC', 'GAAA', 'TCTG']
    short_list = ['AGATC', 'AATG', 'TATC']

    # TODO: Check for command-line usage
    valid_filenames = [f"sequences/{num}.txt" for num in range(1, 21)]
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        return 1
    elif sys.argv[1] not in ["databases/large.csv", "databases/small.csv"] or sys.argv[2] not in valid_filenames:
        print("Usage: python dna.py data.csv sequence.txt")
        return 1

    # TODO: Read database file into a variable
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        database = {}
        for row in reader:
            database[row['name']] = []
            if sys.argv[1] == "databases/small.csv":
                database[row['name']].append([row["AGATC"], row['AATG'], row['TATC'], row['name']])
            elif sys.argv[1] == "databases/large.csv":
                database[row['name']].append([row['AGATC'], row['TTTTTTCT'], row['AATG'], row['TCTAG'],
                                             row['GATA'], row['TATC'], row['GAAA'], row['TCTG']])

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as sequence:
        structure = sequence.read()

    # TODO: Find longest match of each STR in DNA sequence
    longest_run = {}
    if sys.argv[1] == "databases/small.csv":
        for subsequence in short_list:
            longest_run[subsequence] = longest_match(structure, subsequence)
    else:
        for subsequence in long_list:
            longest_run[subsequence] = longest_match(structure, subsequence)

    # TODO: Check database for matching profiles
    for line in database:
        database[line] = list(database[line])
        check = 0
        i = 0
        if sys.argv[1] == "databases/small.csv":
            for subsequence in short_list:
                if str(longest_run[subsequence]) in database[line][0][i]:
                    check += 1
                    i += 1
                if sys.argv[1] == "databases/small.csv" and check == 3:
                    print(line)
                    return 0
        elif sys.argv[1] == "databases/large.csv":
            for subsequence in long_list:
                if str(longest_run[subsequence]) in database[line][0][i]:
                    check += 1
                    i += 1
                if sys.argv[1] == "databases/large.csv" and check == 8:
                    print(line)
                    return 0
    print("No match")
    return 1


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
