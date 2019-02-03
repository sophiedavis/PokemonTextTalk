#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint
from gtts import gTTS
from pygame import mixer, time
import time


# In[ ]:


def speak(text, lang='en'):
    if spoken:
        a = str(int(time.time()))
        tts = gTTS(text=text, lang=lang)
        tts.save(a+'.mp3')
        mixer.init()
        mixer.music.load(a+'.mp3')
        mixer.music.play()
        while mixer.music.get_busy()==True:
            continue
    
def random_pokemon():
    pokemon_collection = ['Charmander', 'squirtle', 'bulbasur', 'pikachu']    
    random_number = randint(0, len(pokemon_collection)-1)
    return pokemon_collection[random_number]


# In[ ]:


spoken=True

pokemon = []

speak(f'what is your name?')
user_name = input()
speak(f'okay {user_name} lets begin your adventure!')
speak(f'so {user_name} is it?')
speak(f'great! I am Professer Sophie I will give you a pokemon')
speak(f'what would you like?')
pokemon.append(input())
print('ok then', pokemon[0], 'it is then!')
print('you are walking along the beach with your new' , pokemon[0] , 'when you come across your rival gary')
print('gary says yes, it is me, surprised? I am going to challenge you with my new dratini!')
war_cry = input('Rival gary challenges you! you send out your new pokemon and say ')
print('Gary thyen says, that pokemon is pathetic! also' , war_cry , 'to you too')
user_move = input('You tremble in anger and use a move on his dratini before he can say anything, the move you use is ')
print('your' , user_move , 'was so effective it knocked out his dratini in one go!')
print('gary raged, gave you his pokecoins and stomped away....')
print('as you leave the pokecenter you noice a flash in the sky')
legendary = input('you look closly and nearly fall over when you relise its the LEGENDARY ')
print('you study the the thing in the sky and then....')
other_name = input('HELLOOOOOOOOOO remember me? Its... I forgot my name what was it again? Said ')
print('WAIT dont say anything i remember its' , other_name , 'see I can remember things sometimes')
print('lets have a battle says' , other_name , 'cmon!')
user_move = input('I have a jolteon you could never defeat! says' , other_name , 'you then use the attack ')
print ('sorry', user_name, 'using your', pokemon[0], ' wasnt enough')
print ('ha, it will take more than a little' , user_move ,  'to defeat my jolteon!' , other_name, 'said')
print ('they are actually doing pretty well, maybe...')
active_pokemon = random_pokemon()
print ('come back jolteon! Go', active_pokemon, 'you can do it!' , other_name , 'says')
print ('her' , active_pokemon , 'did a quick attack so strong it knocked out your' , pokemon[0] , 'in one go!')
user_talk = input('sorry' ,)


# In[ ]:




