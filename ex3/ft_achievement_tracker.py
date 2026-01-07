print("=== Achievement Tracker System ===\n")

alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
bob = {"first_kill", "level_10", "boss_slayer", "collector"}
charlie = {
    "level_10", "treasure_hunter", "boss_slayer", "speed_demon",
    "perfectionist"
}

print("Player alice achievements", alice)
print("Player bob achievements", bob)
print("Player charlie achievements", charlie)
print()
print("=== Achievement Analytics ===")
unique_achievements = alice.union(bob, charlie)
print("All unique achievements:", unique_achievements)
print(f"Total unique achievements: {len(unique_achievements)}")
print()
common_achievements = alice.intersection(bob, charlie)
dup = alice.intersection(bob).union(
    alice.intersection(charlie), bob.intersection(charlie)
)
print(f"Common to all players: {common_achievements}")
rare_achievements = unique_achievements.difference(dup)
print(f"Rare achievements: {rare_achievements}")
print()
print("Alice vs Bob common:", alice.intersection(bob))
print("Alice unique:", alice.difference(alice.intersection(bob)))
print("Bob unique:", bob.difference(bob.intersection(alice)))
