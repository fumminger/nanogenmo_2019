#!/usr/bin/python

import argparse
import os
import random
import sys

stories = [
    ("{time} there was a {person} in {place0}. One day they met a {monster} at {place1}. "
    "It said '{threat}, for I shall {death}, for as the story says {story0}.' "
    "The {person} responded 'A wise story indeed. But you must spare me for as the story says {story1}.' "
    "Then the {monster} disappeared in a burst of flame, screaming 'You have outwitted and defeated me O {person}!' "
    ),
    ("{time} a {monster} dwelt at {place1}. One day a {person} from {place0} travelled there." 
    "The {monster} confronted them and said 'All who pass must perish, lest they explain the riddle of this story. {story0}.' "
    "'Speak and tell me its lesson, or I shall {death}. {threat}!"
    "The {person} responded 'I shall tell you a story of my own, whose meaning shall bring light upon this. {story1}.' "
    "Then the {monster} cried 'You story shows the wisdom of the prophets! {person}, pass in peace' "
    )
]

times = [
    "Long ago",
    "May years past",
    "Before your father was born",
    "In the time of Solomon",
    "Once many years ago"
]

places = [
    "a small village",
    "Baghdad",
    "an abandoned city",
    "a fishing village",
    "a barren farm",
    "a sumptious palace",
    "the court of Solomon",
    "city of brass"
]

persons = [
    "poor fisherman",
    "poor cobbler",
    "young prince",
    "beautiful princess",
    "notorious thief",
    "old man",
    "wise counselor"
]

monsters = [
    "efreet",
    "djinn",
    "roc",
    "man of brass",
    "sorcerer",
    "giant snake"
]

threats = [
    "Woe unto you",
    "Tremble before me",
    "God has abandoned you",
    "Pray for the last time",
    "Make peace with death",
    "Behold your doom"
]
deaths = [
    "eat you",
    "burn you alive",
    "kill you",
    "cut you into pieces"
]

sins = [
    "a sinner deserves the wages of sin",
    "the spendthrift face ruin",
    "blasphemers shall burn in eternal fire",
    "the words of the prophet are forever true"
]
redemptions = [
    "a virtuous man deserves all mercies",
    "no one may judge lest they be judged",
    "only God may judge the sinner",
    "even the worst man may be redeemed",
    "the merciless shall receive no mercy"
]
def choose(array):
    return array[random.randrange(len(array))]

def generate(maxDepth, depth):
    story = choose(stories)
    time = choose(times)
    person = choose(persons)
    place0 = choose(places)
    place1 = choose(places)
    threat = choose(threats)
    monster = choose(monsters)
    death = choose(deaths)

    story0 = choose(sins)
    story1 = choose(redemptions)
    if not depth >= maxDepth:
        story0 = generate(maxDepth, depth+1)
        story1 = generate(maxDepth, depth+1)

    return '\n'*(maxDepth-depth+2) + '\t'*depth + story.format(
            time=time, 
            person=person, 
            place0=place0, 
            place1=place1, 
            monster=monster, 
            threat=threat,
            death=death, 
            story0=story0, 
            story1=story1) + '\n'*(maxDepth-depth+2)



def main(argv):
    parser = argparse.ArgumentParser(prog=os.path.basename(__file__),
        description='Nested story generator.')
    parser.add_argument('-d','--depth', action='store', required=True)
 
    args = parser.parse_args(argv)
    story = generate(int(args.depth), 0)
    print(story)

if __name__ == '__main__':
    main(sys.argv[1:])