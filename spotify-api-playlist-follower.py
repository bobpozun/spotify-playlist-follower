import asyncio
import os
import spotify
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

client = spotify.Client(os.environ.get("CLIENTID", os.environ.get("SECRET"))


async def get_access_token():
    endpoint = "https://accounts.spotify.com/api/token"
    request_body = {
        "grant_type": "client_credentials"
        }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(endpoint, data=request_body, headers=headers, auth=HTTPBasicAuth(os.environ.get("CLIENTID"), os.environ.get("SECRET")))
    return response.json()["access_token"]


async def main():
    token = await get_access_token()
    user = await spotify.User.from_token(client, token)

    print(user)
    # all_playlists = await user.get_all_playlists()



    # async for playlist in user:
    #    if playlist.uri == playlist_uri:
    #        return await playlist.sort(reverse=True, key=(lambda track: track.popularity))
    #
    # async for playlist in all_playlists:
    #     print(playlist)
    # print('No playlists were found!', file=sys.stderr)

if __name__ == '__main__':
    load_dotenv(".env")
    asyncio.get_event_loop().run_until_complete(main())