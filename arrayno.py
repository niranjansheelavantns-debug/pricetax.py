# Easy Score Processor using sys.argv and if-else

import sys

# Check if scores are provided
if len(sys.argv) < 2:
    print("Usage: python scores.py <score1> <score2> ...")
else:
    # Convert arguments to numbers
    scores = [float(x) for x in sys.argv[1:]]

    # Calculate average
    average = sum(scores) / len(scores)

    # Display results
    print("Scores:", scores)
    print("Average:", average)

    # Simple pass/fail check
    if average >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")
