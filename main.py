import os

import pylast

API_KEY: str = os.environ["LAST_API_KEY"]
API_SECRET: str = os.environ["LAST_API_SECRET"]
LAST_USER: str = os.environ["LAST_USER"]
LAST_PASSWORD: str = pylast.md5(os.environ["LAST_PASSWORD"])

network: pylast._Network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
    username=LAST_USER,
    password_hash=LAST_PASSWORD,
)


def generate_next_recommendation(track: pylast.Track) -> pylast.Track:
    tag: pylast.Tag = track.get_top_tags()[0][0]
    next_track: pylast.Track = tag.get_top_tracks()[0][0]
    print(next_track.get_name())
    return next_track


track: pylast.Track = network.get_track("Noisestorm", "Crab Rave")
for i in range(0, 10):
    track = generate_next_recommendation(track)
