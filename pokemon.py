class Pokemon:
  def __init__(self, name, level, type, is_knocked_out):
    self.name = name
    self.level = level
    self.type = type
    self.max_health = level
    self.health = self.max_health
    self.is_knocked_out = is_knocked_out
  
  def lose_health(self, dmg):
    self.dmg = dmg
    self.health -= dmg
    if self.health <= 0:
      self.health = 0
      print('{} has taken {} damage!'.format(self.name,self.dmg))
      self.knock_out()
    else:
      print('{} has taken {} dmg and now has {} hp.'.format(self.name, self.dmg, self.health))

  def gain_health(self, heal):
    self.health += heal
    print('{} has been healed and now has {} hp'.format(self.name, self.health))

  def knock_out(self):
    if self.is_knocked_out:
      print('{} is already knocked out!'.format(self.name))
    else:
      self.is_knocked_out = True
      print('{} is knocked out!'.format(self.name))

  def attack(self, other, dmg):
    self.other = other
    if self.type == 'Fire':
      if other.type == 'Grass':
        dmg *= 2
        effective = True
      elif other.type == 'Water':
        dmg /= 2
        effective = False
      elif other.type == 'Fire':
        dmg /= 2
        effective = False
    elif self.type == 'Grass':
      if other.type == 'Water':
        dmg *= 2
        effective = True
      elif other.type == 'Fire':
        dmg /= 2
        effective = False
      elif other.type == 'Grass':
        dmg /= 2
        effective = False
    elif self.type == 'Water':
      if other.type == 'Fire':
        dmg *= 2
        effective = True
      elif other.type == 'Grass':
        dmg /= 2
        effective = False
      elif other.type == 'Water':
        dmg /= 2
        effective = False
    other.lose_health(dmg)
    if effective == True:
      print('Your attack was very effective!')
    elif effective == False:
      print('Your attack was not very effective...')

class Trainer:
  def __init__(self, name, pokemons, potions, current_pokemon):
    self.name = name
    self.pokemons = pokemons
    self.potions = potions
    self.current_pokemon = current_pokemon

  def __repr__(self):
    ko_list = []
    print_list = []
    for pokemon in self.pokemons:
      if pokemon.is_knocked_out == True:
        ko_list.append(pokemon.name)
      print_list.append(pokemon.name)
      
    return f'Current Stats for {self.name}\n Active pokemon: {self.current_pokemon.name}\n Number of potions: {self.potions}\n Current pokemon health: {self.current_pokemon.health}\n Current team: {print_list}\n Knocked out pokemon: {ko_list}'

  def use_potion(self):
    if self.potions > 0:
      if self.current_pokemon.health < self.current_pokemon.max_health:  
        self.potions -= 1
        self.current_pokemon.gain_health(1)
        print('{} used a potion to heal {}! You now have {} potion(s).'.format(self.name, self.current_pokemon.name, self.potions))
      elif self.current_pokemon.health >= self.current_pokemon.max_health:
        print('{} is already at max health!'.format(self.current_pokemon.name))
    elif self.potions <= 0:
      print('{} is out of potions!'.format(self.name))

  def attack_trainer(self, other_trainer, dmg):
    if self.current_pokemon.is_knocked_out == True:
      print("{}'s {} is knocked out and cannot attack!".format(self.name,self.current_pokemon.name))
    else:
      print("{}'s {} has attacked {}'s {}!".format(self.name, self.current_pokemon.name, other_trainer.name, other_trainer.current_pokemon.name))
      self.current_pokemon.attack(other_trainer.current_pokemon, dmg)
    
  def switch_pokemon(self, new_pokemon):
      self.new_pokemon = new_pokemon
      if self.new_pokemon != self.current_pokemon:
        self.current_pokemon = self.new_pokemon
        print('{}! I choose you!'.format(self.new_pokemon.name))
      elif self.new_pokemon.is_knocked_out == True:
        print('{} is knocked out! You can\'t switch to them!'.format(self.new_pokemon.name))
      elif self.new_pokemon == self.current_pokemon:
        print('{} is already active!'.format(self.new_pokemon.name))
      


charmander = Pokemon('Charmander',2,'Fire',False)
squirtle = Pokemon('Squirtle', 3, 'Water',False)
bulbasaur = Pokemon('Bulbasaur', 4, 'Grass',False)

aaron = Trainer('Aaron',[charmander,squirtle], 3, charmander)
jade = Trainer('Jade',[bulbasaur], 2, bulbasaur)

print(aaron)
print(jade)
aaron.attack_trainer(jade, 1)
jade.use_potion()
aaron.switch_pokemon(squirtle)
jade.attack_trainer(aaron, 1)
aaron.switch_pokemon(charmander)
jade.attack_trainer(aaron,1)
aaron.switch_pokemon(squirtle)
jade.attack_trainer(aaron,1)
print(aaron)
print(jade)
aaron.attack_trainer(jade,1)
#aaron.switch_pokemon(squirtle)
aaron.use_potion()
print(aaron)
aaron.attack_trainer(jade,1)
jade.use_potion()
jade.use_potion()





    