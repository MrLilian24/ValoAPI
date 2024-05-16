# Valorant API
from riotwatcher import RiotWatcher, ValWatcher, LolWatcher, ApiError

api_key = ""

riot = RiotWatcher(api_key) # Riot API
lol = LolWatcher(api_key) # League of Legends API
val = ValWatcher(api_key) # Valorant API

try:
    player_puuid = "B0s7DeR8XNKCcDdFW6TpnRdY7cNBiFXpAWbhZaNk53sOkUQboogZxjwHdoCbWeOrnHxn9hH5T-aJlQ"

    # Get player name
    player_name = riot.account.by_puuid("EUROPE", player_puuid)["gameName"]
    print(f"Player name: {player_name}")

except ApiError as e:
    print(e)

