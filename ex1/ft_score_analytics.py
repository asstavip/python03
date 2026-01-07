import sys

print("=== Player Score Analytics ===")

if len(sys.argv) == 1:
    print(
        "No scores provided. Usage: python3 ft_score_analytics.py"
        " <score1> <score2> .."
    )

else:
    number = [x for x in sys.argv[1:]]
    numbers = []
    for i in number:
        try:
            i = int(i)
        except ValueError:
            print(f"Invalid score for '{i}'")
        else:
            numbers.append(i)
    print("Scores processed:", numbers)
    print("Total players:", len(numbers))
    print("Total score:", sum(numbers))
    print("Average score:", sum(numbers) / len(numbers))
    print("High score:", max(numbers))
    print("Low score:", min(numbers))
    print("Score range:", max(numbers) - min(numbers))
