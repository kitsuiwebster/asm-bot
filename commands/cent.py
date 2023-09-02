import json
import openai
import requests
from discord.ext import commands

class CentCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cent(self, ctx, *, user_query):
        print("Command received:", user_query)
        # Set the system prompt
        system_prompt = """
        Tu es ASM Bot, un bot qui parle français.

        L'utilisateur va te donner 2 lettres et tu vas lui retourner des mots qui contiennent ces consonnes. Ce doit être les 2 consonnes par lesquelles les 2 premières syllabes commencent.
        Voici quelques examples pour t'aider à saisir ce que tu dois retourner:
        
        Si l'utilisateur te donne ST, tu vas lui retourner des mots tels que: saturne, satellite, citrouille, citèrne, sept, soute, site, satan, sativa etc.
        Si l'utilisateur te donne BL, tu vas lui retourner des mots tels que: ballon, boule, balet, bol, balle, boulet, boulot, bulle, bolide, bali, baliverne etc.

        Tu ne dois uniquement que faire cela, si l'utilisateur te donne autre chose que 2 consonnes, comme par example LT, SP, JZ etc. tu dois lui expliquer ce qu'il doit te donner.
        """

        # Set the OpenAI API request settings
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai.api_key}",
        }
        data = {
            "model": "gpt-4",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query},
            ],
            "max_tokens": 2000,
        }
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            data=json.dumps(data),
        )
        response_json = response.json()

        try:
            # Send the response
            await ctx.send(response_json["choices"][0]["message"]["content"])
        except Exception as e:
            print(f"Error sending message: {e}")

async def setup(bot):
    await bot.add_cog(CentCog(bot))
