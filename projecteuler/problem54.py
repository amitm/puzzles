RANKS = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
#
# convert hands to (value, suit)
# j = 11, q = 12, k = 13, a = 14
# sort them


def is_royal_flush(sorted_hand):
    previous = sorted_hand[0]
    if previous[0] != 10:
        return False
    return is_straight_flush(sorted_hand)


def is_straight_flush(sorted_hand):
    flush = is_flush(sorted_hand)
    if not flush:
        return False
    return is_straight(sorted_hand)


def is_of_a_kind(num):
    def inner(sorted_hand):
        previous = sorted_hand[-1]
        kind = 1
        for card in sorted_hand[::-1][1:]:
            if card[0] == previous[0]:
                kind += 1
                if kind == num:
                    return (card[0],)
            else:
                previous = card
                kind = 1
        return False
    return inner

is_four_of_a_kind = is_of_a_kind(4)
is_three_of_a_kind = is_of_a_kind(3)
is_two_of_a_kind = is_of_a_kind(2)


def is_full_house(sorted_hand):
    is_three = is_three_of_a_kind(sorted_hand)
    if not is_three:
        return False
    # remove the threes
    is_two = is_two_of_a_kind([c for c in sorted_hand if c[0] != is_three[0]])
    if not is_two:
        return False
    return is_three[0], is_two[0]


def is_flush(sorted_hand):
    s = sorted_hand[0][1]
    for card in sorted_hand[1:]:
        if card[1] != s:
            return False
    return (sorted_hand[-1][0],)


def is_straight(sorted_hand):
    previous = sorted_hand[0]
    for card in sorted_hand[1:]:
        if card[0] == previous[0] + 1:
            previous = card
        else:
            return False
    return (sorted_hand[-1][0],)


def is_two_pairs(sorted_hand):
    first_pair = is_two_of_a_kind(sorted_hand)
    if not first_pair:
        return False
    second_pair = is_two_of_a_kind(
        [c for c in sorted_hand if c[0] != first_pair[0]])
    if not second_pair:
        return False
    return (
        max(first_pair[0], second_pair[0]), min(first_pair[0], second_pair[0]))


def get_high_card(sorted_hand):
    return (sorted_hand[-1],)

HAND_RANKS = [is_royal_flush, is_straight_flush, is_four_of_a_kind,
              is_full_house, is_flush, is_straight, is_three_of_a_kind,
              is_two_pairs, is_two_of_a_kind, get_high_card]


def get_rank(sorted_hand):
    """Hand is a list of values, give rank of hand and rank of value in hand"""
    for idx, rank_fn in enumerate(HAND_RANKS):
        res = rank_fn(sorted_hand)
        if res:
            return (len(HAND_RANKS) - idx,) + res


def compare(hand1, hand2):
    sorted_hand_1 = get_sorted_hand(hand1)
    sorted_hand_2 = get_sorted_hand(hand2)
    rank1 = get_rank(sorted_hand_1)
    rank2 = get_rank(sorted_hand_2)
    for idx, v in enumerate(rank1):
        res = cmp(v, rank2[idx])
        if res == -1:
            return 1
        if res == 1:
            return 0
    reversed_sorted_hand_2 = sorted_hand_2[::-1]
    for idx, v in enumerate(sorted_hand_1[::-1]):
        res = cmp(v[0], reversed_sorted_hand_2[idx][0])
        if res == -1:
            return 1
        if res == 1:
            return 0


def get_card_value(card):
    try:
        return int(card)
    except ValueError:
        return RANKS[card]


def get_sorted_hand(hand):
    s = [(get_card_value(card[0]), card[1]) for card in hand]
    return sorted(s, key=lambda card: card[0])


def main():
    first = 0
    second = 0
    with open('data/poker.txt') as f:
        for line in f:
            line = line.split(" ")
            res = compare(line[:5], line[5:])
            if res == 0:
                first += 1
            else:
                second += 1
    print first, second

if __name__ == '__main__':
    main()
