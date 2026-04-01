import urllib.request, json

latest = json.load(urllib.request.urlopen("https://xkcd.com/info.0.json"))

with open("config.json", "r") as f:
    config = json.load(f)

config["max"] = latest["num"]

with open("config.json", "w") as f:
    json.dump(config, f)