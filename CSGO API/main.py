import requests
import pandas as pd


csgo = requests.get(f"http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v2/?appid=730&key={'02FA9F9D0E349BA259C403B0E008F47A'}&steamid={'76561198362704529'}")

#assign json to value
csgo_stats = csgo.json()

name_array=[]
value_array=[]

#set up table
data={
    'Name':name_array,
    'Value':value_array
}

print(f'Stats of Player Safrdo on game Counter Strike: Global Offensive')
# find and add value to arrays
for stat in csgo_stats["playerstats"]["stats"]:
    if stat["name"] == "total_kills":
        name_array.append("Total Kills: ")
        value_array.append(stat["value"])
    if stat["name"] == "total_time_played":
        name_array.append("Total Time Played: ")
        value_array.append(stat["value"])
    if stat["name"] == "total_planted_bombs":
        name_array.append("Total Planted Bombs: ")
        value_array.append(stat["value"])
    if stat["name"] == "total_defused_bombs":
        name_array.append("Total Defused bombs: ")
        value_array.append(stat["value"])
    if stat["name"] == "total_wins":
        name_array.append("Total Wins: ")
        value_array.append(stat["value"])
    if stat["name"] == "total_damage_done":
        name_array.append("Total Damage Done: ")
        value_array.append(stat["value"])
    if stat["name"] == "total_kills_headshot":
        name_array.append("Total Kills Headshot: ")
        value_array.append(stat["value"])
    if stat["name"] == "total_wins_pistolround":
        name_array.append("Total Wins Pistol Round: ")
        value_array.append(stat["value"])
    if stat["name"] == "total_kills_knife":
        name_array.append("Total Kills Knife: ")
        value_array.append(stat["value"])
    if stat["name"] == "total_kills_hegrenade":
        name_array.append("Total Kills by Grenade: ")
        value_array.append(stat["value"])

# print data table
print(pd.DataFrame(data))


