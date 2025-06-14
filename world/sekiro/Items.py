from dataclasses import dataclass

@dataclass
class ItemData:
    code: int
    name: str

item_list: list[ItemData] = [
    ItemData(1000, "Spirit Emblem"),
    ItemData(1001, "Red Spirit Emblem"),
    ItemData(1100, "Regenerative Power"),
    ItemData(1101, "Regenerative Power Fragment"),
    ItemData(1110, "Temporary Regenerative Power"),
    ItemData(1200, "Skill Point"),
    ItemData(2000, "Resurrection"),
    ItemData(2100, "Bloodsmoke Ninjutsu"),
    ItemData(2110, "Puppeteer Ninjutsu"),
    ItemData(2120, "Bestowal Ninjutsu"),
    ItemData(2300, "Kusabimaru"),
    ItemData(2310, "Shinobi Prosthetic"),
    ItemData(2390, "Night Eye"),
    ItemData(2400, "Mortal Blade"),
    ItemData(2420, "Mibu Breathing Technique"),
    ItemData(2450, "Anti-air Deathblow Text"),
    ItemData(2460, "Dragon Flash"),
    ItemData(2461, "Floating Passage Text"),
    ItemData(2462, "One Mind"),
    ItemData(2470, "Shinobi Medicine Rank 1"),
    ItemData(2471, "Shinobi Medicine Rank 2"),
    ItemData(2472, "Shinobi Medicine Rank 3"),
    ItemData(2475, "A Beast's Karma"),
    ItemData(2480, "Breath of Life: Shadow"),
    ItemData(2481, "Breath of Nature: Shadow"),
    ItemData(2490, "Sakura Dance"),
    ItemData(2500, "Lotus of the Palace"),
    ItemData(2501, "Shelter Stone"),
    ItemData(2502, "Aromatic Branch"),
    ItemData(2503, "Aromatic Flower"),
    ItemData(2910, "Mechanical Barrel"),
    ItemData(2920, "Shinobi Esoteric Text"),
    ItemData(2921, "Prosthetic Esoteric Text"),
    ItemData(2922, "Ashina Esoteric Text"),
    ItemData(2923, "Senpou Esoteric Text"),
    ItemData(2924, "Mushin Esoteric Text"),
    ItemData(2930, "Recovery Charm"),
    ItemData(3000, "Healing Gourd"),
    ItemData(3001, "Healing Gourd (2)"),
    ItemData(3020, "Pellet"),
    ItemData(3040, "Divine Grass"),
    ItemData(3050, "Red Lump"),
    ItemData(3051, "Red Lump (2)"),
    ItemData(3052, "Red Lump (3)"),
    ItemData(3053, "Academics' Red Lump"),
    ItemData(3060, "Sweet Rice Ball"),
    ItemData(3061, "Sweet Rice Ball (2)"),
    ItemData(3070, "Persimmon"),
    ItemData(3071, "Taro Persimmon"),
    ItemData(3080, "Rice"),
    ItemData(3081, "Fine Snow"),
    ItemData(3200, "Antidote Powder"),
    ItemData(3210, "Dousing Powder"),
    ItemData(3211, "Ministry Dousing Powder"),
    ItemData(3220, "Pacifying Agent"),
    ItemData(3230, "Eel Liver"),
    ItemData(3250, "Contact Medicine"),
    ItemData(3290, "Bite Down"),
    ItemData(3291, "Hidden Tooth"),
    ItemData(3292, "Bite Down (2)"),
    ItemData(3300, "Green Mossy Gourd"),
    ItemData(3301, "Green Mossy Gourd (2)"),
    ItemData(3310, "Withered Red Gourd"),
    ItemData(3311, "Withered Red Gourd (2)"),
    ItemData(3320, "Mottled Purple Gourd"),
    ItemData(3321, "Mottled Purple Gourd (2)"),
    ItemData(3350, "Ako's Spiritfall"),
    ItemData(3360, "Yashariku's Spiritfall"),
    ItemData(3370, "Ungo's Spiritfall"),
    ItemData(3380, "Gokan's Spiritfall"),
    ItemData(3390, "Gachiin's Spiritfall"),
    ItemData(3400, "Ako's Sugar"),
    ItemData(3410, "Yashariku's Sugar"),
    ItemData(3420, "Ungo's Sugar"),
    ItemData(3430, "Gokan's Sugar"),
    ItemData(3440, "Gachiin's Sugar"),
    ItemData(3450, "Divine Confetti"),
    ItemData(3500, "Ceramic Shard"),
    ItemData(3510, "Fistful of Ash"),
    ItemData(3520, "Oil"),
    ItemData(3530, "Snap Seed"),
    ItemData(3580, "Five-color Rice"),
    ItemData(3581, "Five-color Rice (2)"),
    ItemData(3600, "Mibu Balloon of Wealth"),
    ItemData(3610, "Mibu Balloon of Soul"),
    ItemData(3620, "Mibu Possession Balloon"),
    ItemData(3630, "Mibu Balloon of Spirit"),
    ItemData(3640, "Mibu Pilgrimage Balloon"),
    ItemData(3700, "Light Coin Purse"),
    ItemData(3704, "Heavy Coin Purse"),
    ItemData(3708, "Bulging Coin Purse"),
    ItemData(3720, "Bundled Jizo Statue"),
    ItemData(3721, "Jinza's Jizo Statue"),
    ItemData(3730, "Bell Demon"),
    ItemData(3800, "Ceremonial Tanto"),
    ItemData(3801, "Ceremonial Tanto (2)"),
    ItemData(3900, "Nightjar Monocular"),
    ItemData(3980, "Homeward Idol"),
    ItemData(3990, "Illusive Hall Bell"),
    ItemData(4000, "Prayer Bead"),
    ItemData(4100, "First Prayer Necklace"),
    ItemData(4101, "Second Prayer Necklace"),
    ItemData(4102, "Third Prayer Necklace"),
    ItemData(4103, "Fourth Prayer Necklace"),
    ItemData(4104, "Fifth Prayer Necklace"),
    ItemData(4105, "Sixth Prayer Necklace"),
    ItemData(4106, "Seventh Prayer Necklace"),
    ItemData(4107, "Eighth Prayer Necklace"),
    ItemData(4108, "Ninth Prayer Necklace"),
    ItemData(4109, "Final Prayer Necklace"),
    ItemData(4400, "Gourd Seed"),
    ItemData(5100, "Memory"),
    ItemData(5200, "Memory: Gyoubu Oniwa"),
    ItemData(5201, "Memory: Lady Butterfly"),
    ItemData(5202, "Memory: Genichiro"),
    ItemData(5203, "Memory: Screen Monkeys"),
    ItemData(5204, "Memory: Guardian Ape"),
    ItemData(5205, "Memory: Corrupted Monk"),
    ItemData(5206, "Memory: Great Shinobi"),
    ItemData(5207, "Memory: Foster Father"),
    ItemData(5208, "Memory: True Monk"),
    ItemData(5209, "Memory: Divine Dragon"),
    ItemData(5210, "Memory: Hatred Demon"),
    ItemData(5211, "Memory: Saint Isshin"),
    ItemData(5212, "Memory: Isshin Ashina"),
    ItemData(5213, "Memory: Headless Ape"),
    ItemData(5220, "Memory: Inner Genichiro"),
    ItemData(5221, "Memory: Inner Father"),
    ItemData(5222, "Memory: Inner Isshin"),
    ItemData(5300, "Remnant: Gyoubu"),
    ItemData(5301, "Remnant: Lady Butterfly"),
    ItemData(5302, "Remnant: Genichiro"),
    ItemData(5303, "Remnant: Screen Monkeys"),
    ItemData(5304, "Remnant: Guardian Ape"),
    ItemData(5305, "Remnant: Corrupted Monk"),
    ItemData(5306, "Remnant: Great Shinobi"),
    ItemData(5307, "Remnant: Foster Father"),
    ItemData(5308, "Remnant: True Monk"),
    ItemData(5309, "Remnant: Divine Dragon"),
    ItemData(5310, "Remnant: Hatred Demon"),
    ItemData(5311, "Remnant: Saint Isshin"),
    ItemData(5312, "Remnant: Isshin Ashina"),
    ItemData(5313, "Remnant: Headless Ape"),
    ItemData(5320, "Remnant: Inner Genichiro"),
    ItemData(5321, "Remnant: Inner Father"),
    ItemData(5322, "Remnant: Inner Isshin"),
    ItemData(5400, "Memory (2)"),
    ItemData(5500, "Mask Fragment: Right"),
    ItemData(5501, "Mask Fragment: Left"),
    ItemData(5502, "Mask Fragment: Dragon"),
    ItemData(5510, "Dancing Dragon Mask"),
    ItemData(5600, "Dragon's Blood Droplet"),
    ItemData(6000, "Scrap Iron"),
    ItemData(6010, "Scrap Magnetite"),
    ItemData(6020, "Adamantite Scrap"),
    ItemData(6100, "Black Gunpowder"),
    ItemData(6200, "Yellow Gunpowder"),
    ItemData(6210, "Fulminated Mercury"),
    ItemData(6300, "Lump of Fat Wax"),
    ItemData(6310, "Lump of Grave Wax"),
    ItemData(6400, "Lapis Lazuli"),
    ItemData(9000, "Divine Dragon's Tears"),
    ItemData(9003, "Kuro's Charm"),
    ItemData(9009, "Sakura Droplet"),
    ItemData(9010, "Young Lord's Bell Charm"),
    ItemData(9011, "Father's Bell Charm"),
    ItemData(9020, "Ornamental Letter"),
    ItemData(9052, "Red Carp Eyes"),
    ItemData(9060, "Dragon's Tally Board"),
    ItemData(9061, "Promissory Note"),
    ItemData(9070, "Water of the Palace"),
    ItemData(9071, "Great White Whisker"),
    ItemData(9080, "Red and White Pinwheel"),
    ItemData(9081, "White Pinwheel"),
    ItemData(9090, "Rice for Kuro"),
    ItemData(9091, "Frozen Tears"),
    ItemData(9100, "Ashina Sake"),
    ItemData(9101, "Unrefined Sake"),
    ItemData(9102, "Monkey Booze"),
    ItemData(9103, "Dragonspring Sake"),
    ItemData(9104, "Ashina Sake (2)"),
    ItemData(9105, "Unrefined Sake (2)"),
    ItemData(9180, "Precious Bait"),
    ItemData(9181, "Truly Precious Bait"),
    ItemData(9182, "Truly Precious Bait (2)"),
    ItemData(9192, "Fresh Serpent Viscera"),
    ItemData(9193, "Dried Serpent Viscera"),
    ItemData(9200, "Herb Catalogue Scrap"),
    ItemData(9205, "Dosaku's Note"),
    ItemData(9206, "Rat Description"),
    ItemData(9207, "Surgeon's Bloody Letter"),
    ItemData(9208, "Surgeon's Stained Letter"),
    ItemData(9209, "Holy Chapter: Dragon's Return"),
    ItemData(9210, "Immortal Severance Text"),
    ItemData(9211, "Immortal Severance Scrap"),
    ItemData(9212, "Fragrant Flower Note"),
    ItemData(9213, "Okami's Ancient Text"),
    ItemData(9214, "Page's Diary"),
    ItemData(9215, "Holy Chapter: Infested"),
    ItemData(9216, "Tomoe's Note"),
    ItemData(9217, "Flame Barrel Memo"),
    ItemData(9218, "Nightjar Beacon Memo"),
    ItemData(9219, "Isshin's Letter"),
    ItemData(9220, "Rotting Prisoner's Note"),
    ItemData(9221, "Sabimaru Memo"),
    ItemData(9222, "Sabimaru Memo (2)"),
    ItemData(9223, "Valley Apparitions Memo"),
    ItemData(9224, "Valley Apparitions Memo (2)"),
    ItemData(9225, "Three-story Pagoda Memo"),
    ItemData(9226, "Three-story Pagoda Memo (2)"),
    ItemData(9227, "Black Scroll"),
    ItemData(9228, "Holy Chapter: Infested (2)"),
    ItemData(9402, "Gatehouse Key"),
    ItemData(9403, "Hidden Temple Key"),
    ItemData(9404, "Secret Passage Key"),
    ItemData(9405, "Gun Fort Shrine Key"),
    ItemData(9500, "Rot Essence: Sculptor"),
    ItemData(9501, "Rot Essence: Newcomer"),
    ItemData(9502, "Rot Essence: Black Hat"),
    ItemData(9503, "Rot Essence: Lost Child"),
    ItemData(9504, "Rot Essence: Charmed One"),
    ItemData(9505, "Rot Essence: Surgeons"),
    ItemData(9510, "Rot Essence: Fine Son"),
    ItemData(9511, "Rot Essence: Thirsty One"),
    ItemData(9515, "Rot Essence: Timid Maid"),
    ItemData(9516, "Rot Essence: Faithful One"),
    ItemData(9520, "Rot Essence: Crow Mob"),
    ItemData(9521, "Rot Essence: Wartorn Mob"),
    ItemData(9522, "Rot Essence: Jail Mob"),
    ItemData(9523, "Rot Essence: Toxic Mob"),
    ItemData(9524, "Rot Essence: Pious Mob"),
    ItemData(9525, "Rot Essence: Drunk Mob"),
    ItemData(9526, "Rot Essence: Info Broker"),
    ItemData(9560, "Dragonrot Blood Sample"),
    ItemData(9700, "Shuriken Wheel"),
    ItemData(9701, "Phantom Kunai"),
    ItemData(9710, "Robert's Firecrackers"),
    ItemData(9720, "Flame Barrel"),
    ItemData(9721, "Pine Resin Ember"),
    ItemData(9730, "Shinobi Axe of the Monkey"),
    ItemData(9740, "Mist Raven's Feathers"),
    ItemData(9750, "Sabimaru"),
    ItemData(9760, "Iron Fortress"),
    ItemData(9770, "Large Fan"),
    ItemData(9780, "Gyoubu's Broken Horn"),
    ItemData(9790, "Slender Finger"),
    ItemData(9791, "Malcontent's Ring"),
    ItemData(9800, "Another's Memory: Shura"),
    ItemData(9810, "Another's Memory: Ashina"),
    ItemData(9820, "Another's Memory: Tengu"),
    ItemData(10000, "Treasure Carp Scale"),
    ItemData(11000, "Gyoubu Oniwa"),
    ItemData(11010, "Lady Butterfly"),
    ItemData(11020, "Genichiro Ashina"),
    ItemData(11030, "Folding Screen Monkeys"),
    ItemData(11040, "Guardian Ape"),
    ItemData(11050, "Headless Ape"),
    ItemData(11060, "Corrupted Monk"),
    ItemData(11070, "True Monk"),
    ItemData(11080, "Great Shinobi - Owl"),
    ItemData(11090, "Owl (Father)"),
    ItemData(11100, "Divine Dragon"),
    ItemData(11110, "Emma, the Gentle Blade"),
    ItemData(11120, "Isshin Ashina"),
    ItemData(11130, "Isshin, the Sword Saint"),
    ItemData(11140, "Demon of Hatred"),
    ItemData(11150, "Inner Genichiro"),
    ItemData(11160, "Inner Father"),
    ItemData(11170, "Inner Isshin"),
    ItemData(11180, "Genichiro, Way of Tomoe"),
    ItemData(11500, "???"),
]