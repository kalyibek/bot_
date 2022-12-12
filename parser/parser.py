import requests
import json
from config import bot
from aiogram import types


async def pokemon_parser(message: types.Message):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/")
    data = json.JSONDecoder().decode(response.text)

    for pokemon in data['results']:
        id = pokemon['url'].split('/')[-2]
        img_url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png'

        await bot.send_photo(
            message.chat.id,
            img_url,
        )

        await bot.send_message(
            message.chat.id,
            pokemon['name']
        )
