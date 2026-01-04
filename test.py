alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie =  {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
asta = {'first_kill', 'level_10', 'nadi','wnassa'}
# dup = alice.intersection(bob).intersection(asta).union(alice.intersection(charlie),bob.intersection(charlie),alice.intersection(asta),bob.intersection(asta))
# unique_achievements = alice.union(bob,charlie,asta)
#
# print(unique_achievements - dup)

print(alice.intersection(charlie))
print(bob.intersection(charlie))

# print(dup)