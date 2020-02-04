from collections import defaultdict
from typing import DefaultDict, List, Set

import requests
from pincelate import Pincelate


def syns(word: str) -> Set[str]:
    return set([obj['word'] for obj in requests.get('https://api.datamuse.com/words', params={
        'ml': word
    }).json() if ' ' not in obj['word']] + [word])


def generate(one: str, other: str) -> Set[str]:
    pin = Pincelate()

    ones: List[str] = list(map(
        lambda x: ' '.join(pin.soundout(x)), syns(one)))
    others: List[str] = list(map(
        lambda x: ' '.join(pin.soundout(x)), syns(other)))

    one_starts = set()
    one_ends: DefaultDict[str, Set[str]] = defaultdict(set)

    other_starts = set()
    other_ends: DefaultDict[str, Set[str]] = defaultdict(set)

    final = set()

    for w in (x.split(' ') for x in ones):
        for i in range(4, len(w) - 3, 1):
            one_starts.add(' '.join(w[:i + 1]))
            one_ends[w[i]].add(' '.join(w[i + 1:]))

    for w in (x.split(' ') for x in others):
        for i in range(4, len(w) - 3, 1):
            other_starts.add(' '.join(w[:i + 1]))
            other_ends[w[i]].add(' '.join(w[i + 1:]))

    for s in one_starts:
        for e in other_ends[s.split(' ')[-1]]:
            final.add(pin.spell(s.split(' ') + e.split(' ')))

    for s in other_starts:
        for e in one_ends[s.split(' ')[-1]]:
            final.add(pin.spell(s.split(' ') + e.split(' ')))

    return final


if __name__ == "__main__":
    names = generate('spider', 'robot')

    with open('arachnotron_names.txt', 'w') as f:
        for n in names:
            f.write('{}\n'.format(n))
