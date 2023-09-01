import json
import openai
import requests
from discord.ext import commands

class AskCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ask(self, ctx, *, user_query):
        print("Command received:", user_query)
        # Set the system prompt
        system_prompt = """
        
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
    await bot.add_cog(AskCog(bot))
