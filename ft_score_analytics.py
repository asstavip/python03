import sys

print("=== Player Score Analytics ===")

if len(sys.argv) == 1:
    print("No scores provided. Usage: python3 ft_score_analytics.py"
    " <score1> <score2> ..")

else:
#     Scores processed: [1500, 2300, 1800, 2100, 1950]
# Total players: 5
# Total score: 9650
# Average score: 1930.0
# High score: 2300
# Low score: 1500
# Score range: 800
    number = [x for x in sys.argv[1:]]
    numbers = []
    for i in number:
        try:
            i = int(i)
        except ValueError:
            print(f"Invalid score for '{i}'")
        else:
            numbers.append(i)
    print("Scores processed:",numbers)
    print("Total players:",len(numbers))
    print("Total score:",sum(numbers))
    print("Average score:",sum(numbers)/len(numbers))
    print("High score:",max(numbers))
    print("Low score:",min(numbers))
    print("Score range:",max(numbers)-min(numbers))