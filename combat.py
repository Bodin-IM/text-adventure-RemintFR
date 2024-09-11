from random import randint
from time import sleep
#damage = randint(1, 10)
#randomChance = randint(-10,0)
def checkHealth(hp):
    if hp <= 0:
        return True
    else:
        return False
 
playerHp = 100
playerMaxDmg = 20
playerMinDmg = 5
hitChance = 80 # hit chance in percent
 
enemyHp = 100
enemyMaxDmg = 20
enemyMinDmg = 5
enemyhitChance = 90 # hit chance in percent
 
combat = True
while combat:
    sleep(1)
    print(f"You have {playerHp} HP left. The enemy has {enemyHp} HP left.")
 
    if randint(0,100) < hitChance:
        dmg = randint(playerMinDmg, playerMaxDmg)
        enemyHp -= dmg
        print(f"You did {dmg} to the enemy, the enemy now has {enemyHp} HP.")
    else:
        print("You missed.")
 
    if checkHealth(enemyHp):
        print("Enemy is dead")
        combat = False

    if randint(0,100) < hitChance:
        dmg = randint(enemyMinDmg, enemyMaxDmg)
        playerHp -= dmg
        print(f"You did {dmg} to the player, the player now has {playerHp} HP.")
    else:
        print("You missed.")
 

    
 
    if checkHealth(playerHp):
        print("You died")
        combat = False


