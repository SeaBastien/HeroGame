from random import randint
#from termcolor import colored, cprint
class hero():
  def __init__(self, name, hp, dex, power, stam):
    self.inBattle = False
    self.name = name #The name of the user
    self.health = hp #How many hit points the user has
    self.power = power #Determines the amount of damage in the attack
    self.defence = 0 #determines the amount of damage is taken off from the enemies attack when in battle
    self.totalWeight = 5 #Starts with 5 because of the backpack
    self.stamina = stam #Determines if the hero can lift items
    self.energy = 15 #starting energy
    self.dexterity = dex #Determines if the attack will hit
    self.backpack = backpack() #the self.backpack holds the value of the backpack class
    self.handCap = 2 #Two free hands
    self.enemiesBeat = 0#holds the amount of enemies the hero has beat
    self.weapStyle = "Fisticuffs"#default weapon style is fists...usually
  
  #----------------------------HERO METHODS----------------------------------

#uses the users battle item/weapon as a paramter from the method
  def pickupItem(self, item):
    #1 parameter with object picking up
    #Should be in the users backpack
    #puts the item in the backpack automatically
    self.backpack.totalItems.append(item)
    #if the total weight of the hero is greater than the random integer of the heros stamina then the algorithm will take out the item that was just added
    if self.totalWeight > self.stamina:
      #Tell the user that their maximum weight limit has been reached and that they dropped the picked up item
      print("'nYou are at max capacity for your availible items. You dropped the item")
      #takes the item out of the total items list
      self.backpack.totalItems.pop(item)
    #OR if the total weight is less than the stamina then the user will... 
    elif self.totalWeight <= self.stamina:
      #add the weight to the total weight
      self.totalWeight += int(item.weight)
      #Then return the backpack with all the items leftover
      return self.backpack.totalItems
    
  #allows the user to drop an item
  def drop(self):
    #If the length of the backpack are greater than 0...
    if len(self.backpack.totalItems) > 0:
      #Print the items the user has in their bag
      print(f"\n------------\nHere are your items in your bag:")
      #z just needs some string
      z = ""
      #prints the items in a very nice format
      for i in range(len(self.backpack.totalItems)):
        z += f"\n{i+1})" + str(self.backpack.totalItems[i]) + f"\n"
      print(z)
      while True:
        #Then ask whcih item the user would like to drop
        dropper = input("\nWhich item would you like to drop?\nUse numbers associated to your desired option\nType 'no' to return to the main menu\nYour Decision: ")
        #If the user inputs 'no' then the algorithm will return ther user back to the main menu
        if dropper == 'no':
          print("\nReturning to main menu...")
          break#return user to main menu

        #If the users number is less than the lenth of the total number of items + 1 and greater than 0 
        elif int(dropper) <= int(len(self.backpack.totalItems) + 1) and int(dropper) > 0:
            #the total weight sill subtract the weight of the object 
            self.totalWeight -= int(self.backpack.totalItems[int(dropper)-1].weight)
            #Show the user what item they chose
            print(f"\nYou have chosen to break the following item: \n{str(self.backpack.totalItems[int(dropper)-1])}\n")
            #If the item is a sword and it's power is greater than the heros dexterity then the hero will
            if self.backpack.totalItems[int(dropper)-1].name == "sword" and self.backpack.totalItems[int(dropper)-1].power > self.dexterity:
                #print a message like so
                print("\nYou tried really really hard to break your item, but it turns out it was a mimic that now just ate both your kneecaps...great job.\nBut hey look on the bright side, what doesn't kill you makes you stronger...right?")
                #take damage but dexterity will get higher, and if the power is taken away and lower than 2 then the program will set the heros power level to the according fisticuffs powerlevel
                self.health -= 5
                self.power -= self.backpack.totalItems[int(dropper)-1].power
                if self.power <= 2:
                  self.power = 2
                self.dexterity += 1
                #Tell the user their changed states stats now
                print(f"\nHP: -5\nDexterity: +1")
                #Adds the hand capacity respectively
                self.handCap += self.backpack.totalItems[int(dropper)-1].handCap
                #Then takes the item out of the users bag
                self.backpack.totalItems.pop(int(dropper)-1)
                break#return user to main menu
            
            #If the item is a sword and it's power is greater than the heros dexterity then the hero will
            if self.backpack.totalItems[int(dropper)-1].name == "shield" and self.backpack.totalItems[int(dropper)-1].defence > self.dexterity:
                  #Print a nice message
                  print("\nYou tried really really hard to break your item, but it turns out it was a mimic that now just ate both your kneecaps...great job.\nBut hey look on the bright side, what doesn't kill you makes you stronger...right?")
                  #take damage but dexterity will get higher, and if the power is taken away and lower than 2 then the program will set the heros defence back to the original defence without the item
                  self.health -= 5
                  self.defence -= self.backpack.totalItems[int(dropper)-1].defence
                  if self.defence <= 0:
                    self.defence = 0
                  self.dexterity += 1
                  #Tell the user their changed states stats now
                  print(f"\nHP: -5\nDexterity: +1")
                  #Adds the hand capacity respectively
                  self.handCap += self.backpack.totalItems[int(dropper)-1].handCap
                  #Then takes the item out of the users bag
                  self.backpack.totalItems.pop(int(dropper)-1)
                  break#return user to main menu
            #Buf if the users stamina is greater than the stats then...
            else:
                  #Print a message as such
                  print("\nYou heard a loud *CRACK* as you bent the item over your knee.\nAaaand now it's no longer useable....great...\nyou reluctantly threw it on the ground behind you and continued your travels!")
                  #add back the hand cap
                  self.handCap += self.backpack.totalItems[int(dropper)-1].handCap
                  #the program will try to get the power of the item but if now it will gain the defence of the item then subtract it respectively
                  try:
                    self.power -= self.backpack.totalItems[int(dropper)-1].power
                  except:
                    self.defence -= self.backpack.totalItems[int(dropper)-1].defence
                  #resets the stats to the original amount
                  if self.power <= 0:
                    self.power = 2
                  if self.defence <= 0:
                    self.defence = 0
                  #takes the item out
                  self.backpack.totalItems.pop(int(dropper)-1)
                  break#return user to main menu
        #If the user chooses no then...
        elif dropper == 'no':
            print("\nReturning to main menu...")
            break#return user to main menu
        #if anything else happend jsut let the user know that's not the right answer
        else:
          print("\nThat's not an answer")#loops back after this message 
    #if none of the parameters are satisfied then tell the user such and loops back
    else:
      print("\nThere's nothing in your bag to drop...")

  #equips an item to the user as the item is passed through the function as a parameter
  def equip(self, item):
    #Equipt from the backpack
    #If the hand capacity is 0
    if self.handCap == 0:
      while True:
        #Make things easier
        desiredTotal = self.backpack.totalItems[item-1]
        #tell the user that the hand cap has been reached
        change = input("\n--The hand capacity has been reached--\n\nWould you like to swap your already equipt weapons with your desired one?\n~Type 'yes' or 'no'\nYour Decision: ")
        
        #if they want to change it, then ...
        if change == "yes": 
          #check to see if the hand cap is 2 (double handed)
          if desiredTotal.handCap == 2:
            #self.handCap is already 0
            #the new power is the power of the usered desired weapon
            self.power = desiredTotal.power
            #put the items from the equipt item into the total amount of items
            self.backpack.totalItems.append(self.backpack.equiptItems)
            #take out the items from the equipted list
            self.backpack.equiptItems.pop(-1)
            #put the users desiered item into the equipted list
            self.backpack.equiptItems.append(desiredTotal)
            #The take it out from the total items
            self.backpack.totalItems.pop(item-1)
            #print message saying such
            print("\nYou have successfully equipted the double handed sword!")
            break#return user to main menu
            
          #checks if the name of the item is a sword and if the hand capacity is 1...
          elif desiredTotal.name == 'sword' and desiredTotal.handCap == 1:
            #adds one to the hand cap because the returned items in the bag make the hand cap 2 but adding another item just makes the result for hand cap 1
            self.handCap += 1
            #change the weapon style
            self.weapStyle = "Single Handed Sword"
            #the new power is the power of the usered desired weapon
            self.power += desiredTotal.power
            #put the items from the equipt item into the total amount of items
            self.backpack.totalItems.append(self.backpack.equiptItems)
            #take out the items from the equipted list
            self.backpack.equiptItems.pop(-1)
            #put the users desiered item into the equipted list
            self.backpack.equiptItems.append(desiredTotal)
            #put the users desiered item into the equipted list
            self.backpack.totalItems.pop(item-1)
            #print message saying such
            print("\nYou have successfully equipted the single handed sword!")
            break#return user to main menu

          #checks if the name of the item is a shield and if the hand capacity is 1...
          elif desiredTotal.name == 'shield' and desiredTotal.handCap == 1:
            #adds one to the hand cap because the returned items in the bag make the hand cap 2 but adding another item just makes the result for hand cap 1
            self.handCap += 1
            #the new defence is the defence of the usered desired weapon
            self.defence += desiredTotal.defence
            #put the items from the equipt item into the total amount of items
            self.backpack.totalItems.append(self.backpack.equiptItems)
            #take out the items from the equipted list
            self.backpack.equiptItems.pop(-1)
            #put the users desiered item into the equipted list
            self.backpack.equiptItems.append(desiredTotal)
            #If the last item was a sword and is in the equipt items list then...
            if (self.backpack.totalItems[item-1].name == 'sword') in self.backpack.equiptItems:
              #Don't change the weapon style
              break#return the user to main menu
            else:
              #If that isn't true then change the style back to fisticuffs...and shield
              self.weapStyle = "Fisticuffs"
            #take the item desired out from the total items
            self.backpack.totalItems.pop(item-1)
            #print a message as such
            print("\nYou have successfully equipted a shield")
            break#reurtn the user
        #if the user chooses no the just bring them back to the main menu
        elif change == "no":
          print("\nAnyways, back to the adventure...")
          break
        #if anything else happens print a massage and loop
        else:
          print("""\n*The little voice in your head speaks*\n"I'll equipted it later...Maybe?" """)

    #checks Iif the hand cap is 1
    elif self.handCap == 1:
      while True:
        #Setting the desiredTotal variable as the desired item from the users total items
        desiredTotal = self.backpack.totalItems[item-1]
        #if the user wants a double handed sword
        if desiredTotal.handCap == 2:
          #ask the user to confirm 
          swap = input("\nYou already have an item in your hand\nWould you like to swap the item that's already in your hand for the double handed sword?\n~Type 'yes' or 'no'\nYour Decision: ")
          #if true then
          if swap.lower() == "yes":
            #double sword = 2 hand cap, but hand cap is already at 1...so minus 1 and now you are using 2 hand
            self.handCap -= 1
            #set the desired power to the users weapon desired power
            self.power = desiredTotal.power
            #put the items from the equipt item into the total amount of items
            self.backpack.totalItems.append(self.backpack.equiptItems)
            #take out the items from the equipted list
            self.backpack.equiptItems.pop(-1)
            #put the users desiered item into the equipted list
            self.backpack.equiptItems.append(desiredTotal)
            #The take it out from the total items
            self.backpack.totalItems.pop(item-1)
            #print message saying such
            print("\nYou have successfully equipted the double handed sword!")
            break

          elif swap.lower == "no":
            print("\nAnyways, back to the adventure...")
            break

          else:
            print("""\n*The little voice in your head speaks*\n"I'll equipted it later...Maybe?" """)

        elif desiredTotal.name == 'sword' and desiredTotal.handCap == 1:
          confirm = input("\nAre you sure?\n~Type 'yes' or 'no'\nYour Decision: ")
          if confirm.lower() == "yes":
            #now you are using both hands
            self.handCap -= 1
            #add new power because you are adding an item to your hand
            self.power += desiredTotal.power
            #put the users desiered item into the equipted list
            self.backpack.equiptItems.append(desiredTotal)
            #The take it out from the total items
            self.backpack.totalItems.pop(item-1)
            #print message saying such
            print("\nYou have successfully equipted the single handed sword!")
            break

          elif confirm.lower() == "no":
            print("\nAnyways, back to the adventure...")
            break
            
          else:
            print("""\n*The little voice in your head speaks*\n"I'll equipted it later...Maybe?" """)
        
        #same as sword but now as shield and comments are tedious
        elif desiredTotal.name == 'shield' and desiredTotal.handCap == 1:
          confirm = input("\nAre you sure?\n~Type 'yes' or 'no'\nYour Decision: ")
          if confirm.lower() == "yes":
            #now you are using both hands
            self.handCap -= 1
            #add new defence because you are adding an item to your hand
            self.defence += desiredTotal.defence
            #put the users desiered item into the equipted list
            self.backpack.equiptItems.append(desiredTotal)
            #The take it out from the total items
            self.backpack.totalItems.pop(item-1)
            #print message saying such
            print("\nYou have successfully equipted a shield!")
            break

          elif confirm.lower() == "no":
            print("\nAnyways, back to the adventure...")
            break
            
          else:
            print("""\n*The little voice in your head speaks*\n"I'll equipted it later...Maybe?" """)

    elif self.handCap == 2:
       while True:
        desiredTotal = self.backpack.totalItems[item-1]
        if desiredTotal.handCap == 2:
            #now you are using both hands
            self.handCap -= 2
            #add new power because you are adding an item to your hand
            self.power += desiredTotal.power
            #put the users desiered item into the equipted list
            self.backpack.equiptItems.append(desiredTotal)
            #The take it out from the total items
            self.backpack.totalItems.pop(item-1)
            #print message saying such
            print("\nYou have successfully equipted the double handed sword!")
            break

        elif desiredTotal.name == 'sword' and desiredTotal.handCap == 1 :
            #now you are using one hand
            self.handCap -= 1
            #add new power because you are adding an item to your hand
            self.power += desiredTotal.power
            #put the users desiered item into the equipted list
            self.backpack.equiptItems.append(desiredTotal)
            #The take it out from the total items
            self.backpack.totalItems.pop(item-1)
            #print message saying such
            print("\nYou have successfully equipted the single handed sword!")
            break

        elif desiredTotal.name == 'shield' and desiredTotal.handCap == 1:
            #now you are using one hand
            self.handCap -= 1
            #add new defence because you are adding an item to your hand
            self.defence += desiredTotal.defence
            #put the users desiered item into the equipted list
            self.backpack.equiptItems.append(desiredTotal)
            #The take it out from the total items
            self.backpack.totalItems.pop(item-1)
            #print message saying such
            print("\nYou have successfully equipted a shield!")
            break
        else:
            print("""\n*The little voice in your head speaks*\n"I'll equipted it later...Maybe?" """)

  #Attack method
  def attack(self):
    #only if inBattle is true, if not, tell the user they are not in battle
    if self.inBattle == True:
      #while the users and enemys health are both above death (0)
      while self.health > 0 and e.eHP > 0:
        #Prompt the user as such until either healthbars reach 0
        print(f"------------\nYour HP: {self.health}\nEnemy HP: {e.eHP}")
        #takes the users input 
        a = input("\n1) Attack the Enemy\n2) Your Stats\n3) RUN\nYour Decision: ")
        
        #if the user chooses option one then...
        if a == "1":
          #Generate a random number between 1 and 15
          attckLand = randint(1, 15)
          #If the users energy is 0 then they can't attack
          if self.energy <= 0:
            print("\nYou don't have enough energy to attack...")
          #if the random number is greater than the users dex then tell the user their attack landed
          elif self.dexterity >= attckLand:
            self.energy -= 1
            #Create a list for the total damage, add the sum of the value of the users power as well as the random number
            dam = []
            #The damage is dependant on pow + a random number between 1 and 5
            dam.append(int(self.power))
            dam.append(randint(1,5))
            #sum of damage in list
            damg = sum(dam)
            #enemys health is taken by the damage dealt from the user
            e.eHP -= damg
            #print the message of how much damage the user did
            print(f'\nYour attack landed for {damg} damage\nEnergy -1')
          #if the users dex is less than the rolled number...
          elif self.dexterity < attckLand:
            #the enemy attacks and if the user has a shield it will take some/all the damage for the user
            enemyAtt = e.eAttack - self.defence
            #if the enemys Attack is less or equal to 0 then the enemies attack is automatically 0
            while enemyAtt <= 0:
              enemyAtt = 0
              break
            #the health of the user is subtracted by the enemys attack
            self.health -= enemyAtt
            #if the enemy attack is  equal to 0
            if enemyAtt == 0:
              #print the message accordingly
              print("\n Your trusty shield took the enemy's blow for you!")
            else:
              #print the message of how much damage the enemy did
              print(f"\nThe Antagonist attacks for {enemyAtt} damage")
        #if the user chooses option 2 then print their stats
        elif a == "2":
          print(x)
        
        #if the user chooses 3
        elif a == "3":
          #get a random number between 1-10
          run = randint(1,10)
          #If the users random number is above 5 then the user attacks
          if run >= 5:
            print("\nYou escaped successfully!")
            break
          #If the number is lowr than 5 then enemy attacks
          elif run < 5:
            print("\nDoesn't look like the enemy is quite done with you yet...back into the fray!")
      #If the health of the hero goes lower or equal to 0 then return them as dead
      if self.health <= 0:
        print("\nYou have been beaten by your worst nightmare...the antagonist...")
        return 'dead'

      #If the heath of the enemy is 0 then...
      elif e.eHP <= 0:
        #tell the user they have beat the enemy
        print("\nWooo hoooo, you beat the enemy!")
        #increase number of enemies beat
        self.enemiesBeat += 1
        #increase enemy intensity
        e.elevel += 1
        #refresh enemy stats
        e.eHP = 10
        e.eHP += int(e.elevel)
        e.eAttack += int(e.elevel)
        #If the enemy has a higher attack than 7 then make their attack 7 because that would be too OP
        if e.eAttack >= 7:
          e.eAttack = 7
        #Tell the user how many enemies they have beat
        print(f"\nYou have beat; {self.enemiesBeat} total enemies!")
        return "yes"
        
          
    #If the user is not in battle then they must initiate one
    elif self.inBattle == False:
      print("\nDoesn't look like you're in a fight, looks like it's time to initiate one")
    
  #gives the user the option to heal and recover energy
  def fullRest(self):
    #if the users health and energy are both already at 15 then   
    if self.health == 15 and self.energy == 15:
      #a message saying they are at max stats will show
      print("\nYou are already at max stats")
    #If the users stats are greater than 15
    elif self.health >= 15 and self.energy >= 15:
      #then make it the max and tell them they are at the max
      self.health = 15
      self.energy = 15
      print("\nYou are already at max stats")
    #In the end just make the health and energy 15 and tell the user their stats have been replenished from their rest
    self.energy = 15
    self.health = 15
    print("\nYou are now fully recovered! That was a refreshing sleep!")

  #half rest gives a little less recovery
  def halfRest(self):
    #if the user has less than 5 energy and health
    if self.health <= 5 and self.energy <= 5:
      #then just add 5 to the amount
      self.energy += 5
      self.health += 5
      #print statement saying so
      print("\nYour stats have been partially restored")
    #if the users health and energy are both already at 15 then   
    elif self.health == 15 and self.energy == 15:
      #a message saying they are at max stats will show
      print("\nYou are already at max stats")
      #If the users stats are greater than 15
    elif self.health >= 15 and self.energy >= 15:
      #then make it the max and tell them they are at the max
      self.health = 15
      self.energy = 15
      print("\nYou are already at max stats")
    #if the health is above or equal to 5 then just keep adding 1 to both energy and health
    elif self.health >= 5 and self.energy >= 5:
      self.energy += 1
      self.health += 1
      print("\nYour stats have been partially restored")

  #default string parameter for the hero class that will be shown when the user wants to see their stats
  def __str__(self):
    #if the users bag has items then show the items, if not then say there are no items in the bag
    if int(len(self.backpack.totalItems)) > 0:
      z = ""
      for i in range(len(self.backpack.totalItems)):
        z += f"\n{i+1})" + str(self.backpack.totalItems[i]) + f"\n"
      return f"\n------------\nHero Name: {self.name}\n------------\nSTATS:\nHP: {self.health}\nEnergy: {self.energy}\nPower: {self.power}\nDefence: {self.defence}\nDexterity: {self.dexterity}\nStamina: {self.stamina}\nWeight: {self.totalWeight}\nHands Free: {self.handCap}\nEnemies Beaten: {self.enemiesBeat}\n------------\nWEAPON: {self.weapStyle}\n------------\nITEMS IN BAG: \n {z}"
    else:
      z = ""
      for i in range(len(self.backpack.totalItems)):
        z += f"\n{i+1})" + str(self.backpack.totalItems[i]) + f"\n"
      return f"\n------------\nHero Name: {self.name}\n------------\nSTATS:\nHP: {self.health}\nEnergy: {self.energy}\nPower: {self.power}\nDefence: {self.defence}\nDexterity: {self.dexterity}\nStamina: {self.stamina}\nWeight: {self.totalWeight}\nHands Free: {self.handCap}\nEnemies Beaten: {self.enemiesBeat}\n------------\nWEAPON: {self.weapStyle}\n------------\nNO ITEMS IN BAG"
      
#weapon class
class weapon():
  def __init__(self):
    #gives the type of item
    self.battleType = "Battle Item"
    #power is determined by the randint of 1-5
    self.power = randint(2, 4)
    #not equipted yet
    self.equip = False
    #weight is determined by the 
    self.weight = randint(1, 3)
    
#inheritance from weapon but aggregate to hero
class sword(weapon):
  def __init__(self, weapStyle):
    #takes the weapon self variables
    weapon.__init__(self)
    #the name is sword
    self.name = "sword"
    #the style is style of either single handed or double handed
    self.weapStyle = weapStyle
    #makes a nice list
    self.bagged = []
    #if the weapStyle is single then the weapStyle is a single handed sword
    if self.weapStyle == "single" or self.weapStyle.lower() == "single":
      self.weapStyle = "Single Handed Sword"
      self.handCap = 1 #with the local hand cap of 1


    #if the weapStyle is double then the weapStyle is a double handed sword
    elif self.weapStyle == "double" or self.weapStyle.lower() == "double":
      self.weapStyle = "Double Handed Sword"
      #with the hand cap of 2
      self.handCap = 2
      #change the power and weight to make gameplay...more balanced
      self.power=randint(3,9)
      self.weight=randint(2,7)

  #prints the sword in a nice little list of stats
  def __str__(self):
    return f"Item: {self.name}\n  Sword Style: {self.weapStyle}\n  Power: {self.power}\n  Weight: {self.weight}"

#inheritance from weapon but aggregate to hero
class shield(weapon):
  def __init__(self, defence):
    #takes the weapon self variables
    weapon.__init__(self)
    #the name is shield
    self.name = "shield"
    #the hand cap is 1
    self.handCap = 1
    #the shield holds defence
    self.defence = randint (1, 3)
     #makes a nice list
    self.bagged = []

  #prints the shield in a nice little list of stats
  def __str__(self):
    return f"Item: {self.name}\n  Defence: {self.defence}\n  Weight:{self.weight}"

 #creates the enemy
class enemy():
  def __init__(self, ename, eHP):
    #they get a name!
    self.eName = ename
    #and HP!
    self.eHP = eHP
    #their attack is a scary 1-6 range
    self.eAttack = randint(1, 6)
    #starts at a nice level 1
    self.elevel = 1
    

#crafting the sword
def craftSword():
  #checks if the heros stamina can hold the weight of their inventory
  if x.stamina >= x.totalWeight:
    while True:
      #asks the use which weapon they want
        y = input("\nYou walk up to a blacksmith who appears to be hard at work!\nHe asks; \n'What kind of sword would you like?' \n~Type 'single' for a single handed weapon\n~Type 'double' for a double handed weapon\n~Type 'nvm' to go back to the main menu\nYour Choice: ") 
        #if they want a single handed 
        if y.lower() == "single":
          #the single holds the value from the sword which is the single for the single handed sword
          single = sword(y)
          #the bagged gets appened with the sword and then gets picked up by the hero
          single.bagged.append(sword(y))
          #print such
          x.pickupItem(single)
          print("\nYou've aquired a singled handed sword! \nThe item was added to your bag.")
          return single
        #if they want a double handed 
        elif y.lower() == "double":
          #the double holds the value from the sword which is the double for the double handed sword
          double = sword(y)
          #the bagged gets appened with the sword and then gets picked up by the hero
          double.bagged.append(sword(y))
          x.pickupItem(double)
          #print such
          print("\nYou've aquired a double handed sword! \nThe item was added to your bag.")
          return double
        #If the users answer is nvm then it will bring them back to the main menu
        elif y.lower() == 'nvm':
          print("\n-You leave the blacksmiths anvil as he continues his work.-\n")
          break 
        #if anything else happens then tell the user that is the case and loop
        else:
          print("\nI've never heard of that kind of sword before...")
  #if the users stamina is less than the weight then they can't carry any more items...
  else:
    print("\nYou can't carry that many items with how strong you are right now")

#crafting a shield for the hero
def craftShield():
  #checks if the heros stamina can hold the weight of their inventory
  if x.stamina >= x.totalWeight:
    while True:
      #asks the user if they want a shield
      s = input("\nYou walk up to a blacksmith who appears to be hard at work!\tHe asks; \n'Would you like a shield?'\n~Type 'yes' for a shield\n~Type 'no' if not\nYour Choice: ")
      #if they choose yes
      if s.lower() == 'yes':
        #yeah the parameter doesn't do anything do just don't worry about that, it's cool that I did +600 lines of code right?
        pickShield = shield(s)
        #the bagged gets appened with the shield and then gets picked up by the hero
        pickShield.bagged.append(shield(s))
        x.pickupItem(pickShield)
        #the defence is also added to the users defence
        x.defence += pickShield.defence
        print("\nYou've aquired a shield! \nThe item was added to your bag.\n")
        break
      #if the user chooses no then it will bring the user back to the main menu
      elif s.lower() == 'no':
        ("\n-You leave the blacksmiths anvil as he continues his work.-\n")
        break
      #if anything else...just print and loop
      else:
        print("\nSo...is that a maybe to the shield?")
  #Print and loop, if anything else
  else:
    print("\nYou can't carry that many items with how strong you are right now")

#creates the class of backpack
class backpack():
  def __init__(self):
    #makes a list for the total items in the bag
    self.totalItems = []
    #make a list for all the equipt items
    self.equiptItems = []
    #the weight of a lether bag is 5 lb
    self.weight = 5
    #the material is kinda like leather because it is!
    self.material = "Leather" 

#Hero random stats
power = randint(1, 2)
stam = randint(15, 20)
dex = randint(5, 15)

#Hero parameters
x = hero("Magnus", 15, dex, power, stam)

#Antagonist parameters
e = enemy('Antagonist', 20)


#control pannel
def control():
  while True:
    #UI is the users input for the main menu
    UI = input(
    """\n------------\n
    Actions Availible:
    \n1) Craft an item
    \n2) Equipt items from bag
    \n3) Find a fight
    \n4) Check items in bag
    \n5) Stats page
    \n6) Break item
    \n7) Rest
    \n8) Ready up for battle
    \n9) Quit
Your Decision: """
    )
    #Gives the user the choice on which item they would like to craft
    if UI == "1":
      while True:
        c = input("\nWhat would you like to craft? Choose the number next to your decision;\n1) Sword\n2) Shield\n3) Nevermind\nYour Decision: ")
        #if user chooses 1 then the user will be making a sword
        if c == "1":
            craftSword()
            break
        #if user chooses 2 then the user will be making a shield
        elif c == "2":
          craftShield()
          break
        #if the user chooses 3 then it will take them back to the main menu
        elif c == "3":
          print("\nGoing back to main menu...")
          break

    #if the user chooses 2 from UI then...
    if UI == "2":
      #and if the backpack has something
      if len(x.backpack.totalItems) > 0:
        while True:
          #it will show the users backpack()
          print("\nItems currently in your bag:")
          z = ''
          for i in range(len(x.backpack.totalItems)):
            z += f"\n{i+1})" + str(x.backpack.totalItems[i]) + f"\n"
          print(z)
          #prompt the user with their desired item they wish to equipt
          item = input("Which item would you like to equip? Use numbers associated to your desired option\nType 'no' to return to the main menu\nYour Decision: ")
          #if the user chooses no then, back to the menu
          if item.lower() == 'no':
            print("\nHeading back to the main menu...")
            break
          #if it is a number then just it must be a umber below the total length of items and above 0
          elif int(item) <= len(x.backpack.totalItems) and int(item) > 0:
            #print the users chosen item
            print(f"\nYou have chosen the option: \n{str(x.backpack.totalItems[int(item)-1])}")
            #make desiredItem the user desired item
            desiredItem = x.backpack.totalItems[int(item)-1]
            #if the item is a sword then change the weap style
            if (x.backpack.totalItems[int(item)-1].name).lower() == "sword":
              x.weapStyle = desiredItem.weapStyle
            #then equip the item
            x.equip(int(item))
            break

          #if all else fails just loop
          else:
            print("\nThat's not in the bag...at least from what I can see...")
      #if all else fails loop
      else:
        print("\nThere are currently no items in your bag...")
          
    #if the user chooses 3
    if UI == "3":
      #and teh in battle is true
      if x.inBattle == True:
        #Then get a random number
        bat = randint(1,10)
        #if the number is greater than 2
        if bat > 2:
          #Then get the user ready for battle
          print("\nGet ready for battle....")
          #call the attack method from the users hero and if they return dead then say you're dead and break, IF NOT then just loop again back to the menu
          if x.attack() == 'dead':
            print("\n---YOU DIED---")
            break
          #if the random number is 2 or less then say no battles were found
        elif bat <= 2:
          print("\nNo battles found...Try shoving random people, that usually does the trick")
      #if the user isn't ready for battle then say so
      else:
        print("\nDoesn't look like you're ready for battle...")

    #If the user chooses 4
    if UI == "4":
      #check if the user has items in the bag
      if len(x.backpack.totalItems) > 0:
        #if they do then print the items in a nice orderly fashion
        print(f"\n------------\nHere are your items in your bag:")
        z = ""
        for i in range(len(x.backpack.totalItems)):
          z += f"\n{i+1})" + str(x.backpack.totalItems[i]) + f"\n"
        print(z)
      #if not then just say they don't
      else:
        print("\nThere are currently no items in your bag...")
    #if the user chooses 5 then print their stats
    if UI == "5":
      print(x)
    #if the user chooses 6 then initiate a drop of an item
    if UI == "6":
      x.drop()
    #if the user chooses 7 then...
    if UI == "7":
      while True:
        #ask if they want a full/half/no recovery
        r = input("\nWhat kind of rest would you like?\n~Type 'full' for a full recovery\n~Type 'half' for some recovery\n~Type 'no' to return back to the main menu\nYour Decision: ")
        #if they say full initiate a full rest
        if r.lower() == 'full':
          x.fullRest()
          break
        #if they say half initiate a half rest
        elif r.lower() == 'half':
          x.halfRest()
          break
        #if they say fno then return back to the main menu automatically with a message
        elif r.lower() == 'no':
          print("\nGoing back to main menu...")
          break
    #if the user chooses 8 then...
    if UI == "8":
      #change the users battle stance to true and if it is already true then say they are already ready for battle
      if x.inBattle == True:
        print("\nLooks like you're already ready for battle...Go pick a fight with someone.")
      #if the battle stance is false just make it true
      elif x.inBattle == False:
        x.inBattle = True
        print("\nYou're now ready to fight!\nGood Luck out there!\nAnd don't forget to equipt your weapon!")
    #if the user chooses 9 then...
    if UI == "9":
      #break then out of the hero game with a goodbye message
      print("\nLeaving so soon?\tWell in that case, \nSafe travels...wherever your next adventure is!")
      break

#initiate the control pannel and start this thing
control()
