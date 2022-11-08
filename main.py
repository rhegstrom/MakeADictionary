# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 18:11:33 2022

@author: Roger Hegstrom(rhegstrom@avc.edu)

make a dictionary the contains 'Family' members (Family in quotes because I do not want real name or birthday... make them),
 at least 5 'immediate' family members.   

object for each member contains birthday (string), favorite color, favorite recording artist(s)

  1. print the dictionary
  2. add an entry for new member of the family (no recording artist)
  3 print values for member of the family  whose name string starts with whoever is first in the alphabet

"""

family = {}


def addFamilyMember(name, birthday, fav_color, fav_artist = ''):
    family[name] = {'birthday': '09/08/1984', 'fav_color': fav_color, 'fav_artist': fav_artist}


# Add all family members
addFamilyMember('Roger', birthday='09/08/1984', fav_color='blue', fav_artist='da baby')
addFamilyMember('Bill',  birthday='06/30/1939', fav_color='yellow', fav_artist='otis')
addFamilyMember('Joe',   birthday='01/03/1990', fav_color='green')
addFamilyMember('Mary',  birthday='02/09/1973', fav_color='red', fav_artist='mariah carey')
addFamilyMember('Bob',   birthday='04/20/1963', fav_color='orange', fav_artist='korn')

# Print members of family in dictionary
print('Printing family members:\n----------------------------')
for name in family:
    print(f'{name} = {family[name]}')


# Prints family members with names starting with 'B'
print('\n\nPrinting family members that start with \'B\'\n-------------------------------------------')
for name in family:
    if name.startswith('B'):
        print(f'{name} = {family[name]}')



