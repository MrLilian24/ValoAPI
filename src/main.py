# Valorant API
from riotwatcher import RiotWatcher, ValWatcher, ApiError

YOUR_API_KEY = ""

riot = RiotWatcher(YOUR_API_KEY) # Riot API
val = ValWatcher(YOUR_API_KEY) # Valorant API

# Riot User
def get_player_puuid(name, tag):
    return riot.account.by_riot_id("EUROPE", name, tag)["puuid"]

def get_player_pseudo(puiid):
    player_pseudo = riot.account.by_puuid("EUROPE", puiid)
    return player_pseudo["gameName"] + "#" + player_pseudo["tagLine"]

# Valorant Ranked
def get_current_act():
    data = val.content.contents("EU","fr-FR")["acts"]
    for act in data:
        if act["isActive"]:
            if act["type"] == "act":
                current_act = act["name"]
            elif act["type"] == "episode":
                current_episode = act["name"]
    return current_episode + " - " + current_act


if __name__ == "__main__":
    try:
        player_puuid = "B0s7DeR8XNKCcDdFW6TpnRdY7cNBiFXpAWbhZaNk53sOkUQboogZxjwHdoCbWeOrnHxn9hH5T-aJlQ"
        assert get_player_puuid("JaimeLesGlaces", "CCLES") == player_puuid
        assert get_player_pseudo(player_puuid) == "JaimeLesGlaces#CCLES"
        assert get_current_act() == "ÉPISODE 8 - ACTE 3"
    except ApiError as e:
        print(e)