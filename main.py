from discord.ext import commands
import requests
from os import getenv


bot = commands.Bot(command_prefix='!!')

def get_token():
    data = {
        'client_id': '10365',
        'client_secret': 'fjZ0UsFaMS7ak7t5tsejhOblMRYOtirYFTQdD8zq',
        'grant_type': 'client_credentials',
        'scope': 'public'
    }

    response = requests.post('https://osu.ppy.sh/oauth/token', data=data).json()

    print(response)
    return response['access_token']


@bot.command()
async def link(ctx, name=None):
    token = get_token()
    
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    r = requests.get(f'https://osu.ppy.sh/api/v2/users/{name}', headers=headers).json()
    pp = r['statistics']['pp']
    
    if r['discord'] == str(ctx.author):
        if 0 <= pp <= 50:
            role = ctx.guild.get_role()
        elif 50 <= pp <= 100:
            role = ctx.guild.get_role()
    else:
        await ctx.reply('Please follow instructions in <#899027902677524572>')
        
        
bot.run('ODk2Mzk3ODA1NDQxMTIyMzA0.YWGhgw.72If96CKyH1mUp83sB9J80eVyr8')