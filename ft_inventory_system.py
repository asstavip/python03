# === Player Inventory System ===
# === Alice's Inventory ===
# sword (weapon, rare): 1x @ 500 gold each = 500 gold
# potion (consumable, common): 5x @ 50 gold each = 250 gold
# shield (armor, uncommon): 1x @ 200 gold each = 200 gold
# Inventory value: 950 gold
# Item count: 7 items
# Categories: weapon(1), consumable(5), armor(1)
# === Transaction: Alice gives Bob 2 potions ===
# Transaction successful!
# === Updated Inventories ===
# Alice potions: 3
# Bob potions: 2
# === Inventory Analytics ===
# Most valuable player: Alice (850 gold)
# Most items: Alice (5 items)
# Rarest items: sword, magic_ring
"""

inventory = {
            "players": {},
            "global_stats": {
                "total_items": 0,
                "total_value": 0,
                "rarest_items": []
            },
            "market_data": {
                "prices": {},
                "trends": {}
            }
        }
player_inv = {
                "items": {},
                "stats": {
                    "total_items": 0,
                    "total_value": 0,
                    "favorite_type": None
                },
                "history": []
            }

"""

print("=== Player Inventory System ===")

print("=== Alice's Inventory ===")
inventory = {
    "players": {
        "alice": {
            "items": {
                "pixel_sword": 1,
                "code_bow": 1,
                "health_byte": 1,
                "quantum_ring": 3,
            },
            "total_value": 1875,
            "item_count": 6,
        },
        "bob": {
            "items": {"code_bow": 3, "pixel_sword": 2},
            "total_value": 900,
            "item_count": 5,
        },
        "charlie": {
            "items": {"pixel_sword": 1, "code_bow": 1},
            "total_value": 350,
            "item_count": 2,
        },
        "diana": {
            "items": {
                "code_bow": 3,
                "pixel_sword": 3,
                "health_byte": 3,
                "data_crystal": 3,
            },
            "total_value": 4125,
            "item_count": 12,
        },
    },
    "catalog": {
        "pixel_sword": {"type": "weapon", "value": 150, "rarity": "common"},
        "quantum_ring": {"type": "accessory", "value": 500, "rarity": "rare"},
        "health_byte": {"type": "consumable", "value": 25, "rarity": "common"},
        "data_crystal": {"type": "material", "value": 1000, "rarity": "legendary"},
        "code_bow": {"type": "weapon", "value": 200, "rarity": "uncommon"},
    },
}


# print("=== Alice's Inventory ===")
for p in inventory.keys():
    print(p, inventory[p])
    print("--------------------------------------------------------")
