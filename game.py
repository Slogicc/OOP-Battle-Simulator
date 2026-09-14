from goblin import Goblin
from hero import Hero

ARENA_NAME = "bottomless hole"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Schlork")
    goblin2 = Goblin("Scribble")
    hero = Hero("1BirdInTheHandIsWorth2InTheBush", "Janitor")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print(f"{hero.name} enters te arena with {hero.health} health. He is a {hero.battle_class}.")
    damageDealt = hero.attack()
    print(f"{hero.name} attacks!")
    goblin.take_damage(damageDealt)
    if goblin.is_alive():
        damageDealt = goblin.attack()
        print(f"{goblin.name} attacks!")
        hero.take_damage(damageDealt)



if __name__ == "__main__":
    main()
