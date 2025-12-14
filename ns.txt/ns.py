with open("ns.txt", "r") as ns_file:
    allowed_names = [name.strip().lower() for name in ns_file.readlines()]

with open("ns.txt", "r") as file:
    lines = file.readlines()

found_names = set()
name_counts = {name: 0 for name in allowed_names}
occurrences = []

for line_number, line in enumerate(lines, start=1):
    # Find "name" positions
    start = 0
    while True:
        index = line.lower().find("name", start)
        if index == -1:
            break
        occurrences.append((line_number, index + 1))
        start = index + len("name")

    # Count allowed names
    words = line.strip().split()
    for word in words:
        if word.lower() in allowed_names:
            found_names.add(word.lower())
            name_counts[word.lower()] += 1

ordered_names = [name for name in allowed_names if name in found_names]

print("My name is " + " ".join(ordered_names))
for name, count in name_counts.items():
    print(f"{name} appears {count} times")

print(f"\nThe word 'name' appears {len(occurrences)} times.")
for line_num, pos in occurrences:
    print(f"Line {line_num}, position {pos}")
