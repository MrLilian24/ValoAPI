# Valorant API
from riotwatcher import RiotWatcher, ValWatcher, LolWatcher, ApiError

YOUR_API_KEY = ""

riot = RiotWatcher(YOUR_API_KEY) # Riot API
val = ValWatcher(YOUR_API_KEY) # Valorant API

def get_player_puuid(name, tag):
    try:
        player_puuid = riot.account.by_riot_id("EUROPE", name, tag)["puuid"]
        return player_puuid
    except ApiError as e:
        print("Player cannot be found.\n", e)

def get_player_pseudo(puiid):
    try:
        player_pseudo = riot.account.by_puuid("EUROPE", puiid)
        return player_pseudo["gameName"] + "#" + player_pseudo["tagLine"]
    except ApiError as e:
        print(e)

if __name__ == "__main__":
    player_puuid = "B0s7DeR8XNKCcDdFW6TpnRdY7cNBiFXpAWbhZaNk53sOkUQboogZxjwHdoCbWeOrnHxn9hH5T-aJlQ"
    assert get_player_puuid("JaimeLesGlaces", "CCLES") == player_puuid
    assert get_player_pseudo(player_puuid) == "JaimeLesGlaces#CCLES"