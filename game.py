from goblin import Goblin
from hero import Hero

ARENA_NAME = "bottomless hole"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
    if hero.is_alive():
        print(f"{hero.name} has won the battle!")
    else:
        print(f"{enemy.name} has won the battle!")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Schlork")
    goblin2 = Goblin("Scribble")
    hero = Hero("1BirdInTheHandIsWorth2InTheBush", "Janitor")
    numworks = Hero("NumWorks Calculator", "Calculator")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print(f"{hero.name} enters te arena with {hero.health} health. He is a {hero.battle_class}.")
    battle(hero, goblin2)
    battle(hero, numworks)



if __name__ == "__main__":
    main()
