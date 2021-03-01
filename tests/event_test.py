import json
from rest_framework import status
from rest_framework.test import APITestCase
from levelupapi.models import Event, Game, GameType

class EventTest(APITestCase):
    def setUp(self):
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those gamez!!"
        }
        # Initiate request and capture response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Store the auth token
        self.token = json_response["token"]

        # Assert that a user was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # SEED DATABASE WITH ONE GAME TYPE
        # This is needed because the API does not expose a /gametypes
        # endpoint for creating game types
        gametype = GameType()
        gametype.label = "Board game"
        gametype.save()


        game = Game()
        game.gametype_id = 1
        game.title = "Monopoly"
        game.description = "win capitalism"
        game.number_of_players = 4
        game.gamer_id = 1

        game.save()
        

    def test_get_event(self):
        


        event=Event()
        event.game_id=1
        event.scheduler_id=1
        event.location="The moon"
        event.event_time="2021-02-05 17:00:00"
        event.save()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        response = self.client.get(f"/events/{event.id}")
        json_response = json.loads(response.content)
        self.assertEqual(json_response["location"], "The moon")

    