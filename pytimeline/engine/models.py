from django.db import models

from django.urls import reverse


DEFAULT_DECK_SIZE = 60
DEFAULT_HAND_SIZE = 5


class Player(models.Model):
    name = models.CharField(max_length=64)
    # cards = many2many(Card)
    game = models.ForeignKey(
        "engine.Game", 
        related_name="players",
        on_delete=models.CASCADE,
    ) # Un jugador tiene una sola partida.


class Game(models.Model):
    deck_size = models.PositiveIntegerField(default=DEFAULT_DECK_SIZE)
    initial_hand_size = models.PositiveIntegerField(default=DEFAULT_HAND_SIZE)
    # deck = many2many(Card)
    current = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('engine:game_details', kwargs={'pk': self.pk})


    def register_user(self, name):
        """Agrega un usuario al state y saca cartas del deck para darle."""
        p = Player.objects.create(name=name, game=self)
        #players_cards = self.extract_cards_from_deck()
        #p.add(players_cards)

    def start(self, users):
        """Inicialize a new game for the given users."""
        #self.deck.add(inic ialize_deck())
        for u in users:
            self.register_user(u)
        #self.timeline.add(self.first_from_deck()))
        print("······· Start " + str(users))
