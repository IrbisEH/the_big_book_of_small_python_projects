import sys, random

# Set up constans

HEARTS = chr(9829)  # ♥
DIAMONDS = chr(9830)  # ♦
SPADES = chr(9824)  # ♠
CLUBS = chr(9827)  # ♣

BACKSIDE = 'backside'


def main():
    print('Blackjack!!!!')

    money = 5000
    while True:
        if money <= 0:
            print('You are broke!')
            print('Thanks for playing')
            sys.exit()

        print('Money:', money)
        bet = get_bet(money)

        # Give the dealer and player two cards from deck each
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        # Handle player actions
        print('Bet:', bet)
        while True:
            display_hands(player_hand, dealer_hand, False)
            print()

            if get_hand_value(player_hand) > 21:
                break

            move = get_move(player_hand, money - bet)

            if move == 'D':
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print('Bet increased to {}.'.format((bet)))
                print('Bet:', bet)

            if move in ('H', 'D'):
                new_card = deck.pop()
                rank, suit = new_card
                print('You drew a {} of {}.'.format(rank, suit))
                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:
                    continue

            if move in ('S', 'D'):
                break

            if get_hand_value(player_hand) <= 21:
                while get_hand_value(dealer_hand) < 17:
                    print('Dealer hits...')
                    dealer_hand.append(deck.pop())
                    display_hands(player_hand, dealer_hand, False)

                    if get_hand_value(dealer_hand) > 21:
                        break
                    input('Press Enter to continue...')

                    print('\n\n')

            # Show the final hands:
            display_hands(player_hand, dealer_hand, True)

            player_value = get_hand_value(player_hand)
            dealer_value = get_hand_value(dealer_hand)

            if dealer_value > 21:
                print('Dealer busts! You win ${}!'.format(bet))
                money += bet
            elif (player_value > 21) or (player_value < dealer_value):
                print('You lost')
                money -= bet
            elif player_value > dealer_value:
                print('You won ${}'.format(bet))
                money += bet
            elif player_value == dealer_value:
                print('It\'s a tie, the bet is returned to you.')

            input('Press Enter to continue...')
            print('\n\n')



def get_bet(max_bet):
    """Ask the player how much they want to bet for this round."""
    while True:
        print('How much fo you bet? (1-{}, or QUIT)'.format(max_bet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet


def get_deck():
    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    """Show the player's and dealer's cards. Hide the dealer's first
    card if show_dealer_hand is False"""
    print()
    if show_dealer_hand:
        print('DEALER:', get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print('DEALER: ???')
        display_cards([BACKSIDE] + dealer_hand[1:])

    print('PLAYER:', get_hand_value(player_hand))
    display_cards(player_hand)


def get_hand_value(cards):
    """Returns the value of the cards. Face cards are worth 10, aces are
    worth 11 or 1 (this function picks the most suitable ace value)."""
    value = 0
    number_of_aces = 0

    # Add the value for the non-ace cards
    for card in cards:
        rank = card[0]
        if rank == 'A':
            number_of_aces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    # Add the value for the aces:
    value += number_of_aces
    for i in range(number_of_aces):
        if value + 10 <= 21:
            value += 10

    return value


def display_cards(cards):
    """Display all the coards in the card list."""
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += ' ___ '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##|'
        else:
            rank, suit = card
            rows[1] += '|{} |'.format(rank.ljust(2))
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|_{}|'.format(rank.rjust(2, '_'))
    for row in rows:
        print(row)


def get_move(player_hand, money):
    """Asks the pleayer for their move, and retuns 'H' for hit,
    'S' for stand, and 'D' for double down."""
    while True:
        moves = ['(H)it', '(S)tand']

        if len(player_hand) == 2 and money > 0:
            moves.append('(D)ouble down')

        move_prompt = ', '.join(moves) + '> '
        move = input(move_prompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move


if __name__ == '__main__':
    main()
