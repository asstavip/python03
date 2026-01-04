import sys

print("=== Command Quest ===")
if len(sys.argv) == 1:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    print("Total arguments: 1")
else:
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {len(sys.argv) - 1}")
    for i,arg in enumerate(sys.argv[1:],start=1):
        print(f"Argument {i}: {arg}")
    print("Total arguments: ", len(sys.argv))