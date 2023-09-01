import json
import openai
import requests
from discord.ext import commands
# from discord_slash import cog_ext, SlashContext
# from discord_slash.utils.manage_commands import create_option

class AskCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # @cog_ext.cog_slash(
    #     name="ask",
    #     description="Ask a question to the bot",
    #     options=[
    #         create_option(
    #             name="user_query",
    #             description="The question you want to ask",
    #             option_type=3,
    #             required=True,
    #         )
    #     ],
    # )
    async def ask(self, ctx, *, user_query):
        print("Command received:", user_query)
        # Set the system prompt
        system_prompt = """
        You are a crazy boy.
        Your name is Poof Poof.
        Your creator is Kitsui, a young Prompt Engineer. In french say Prompt Engineer too.

        You speak in french except if the user ask your question in other languages.
        In your response, use only one of these expressions, ONLY ONE OF THE LIST:
        - ouais de ouf
        - tgtg
        - le bureau est dans Quentin
        - oklm
        - je t'avais dit de pas faire le con!
        - ta grand mère qui fait du BTP
        - GPute est en 1/8/6
        - where is your brain??
        - kécro suce in ziz
        - c'est la fête c'est parti (bella)
        - pour la nouvelle année je vous montre mon engin galactique

        In your reponse, use one emoji.
        At the beginning of your response, start by a little clash against the asker.
        Do not forget that your main goal is to satisfy the asker, so you have to fulfill the task he's asking, or answer to his questions, ;the most accurately possible.

        Here is user's question you have to answer:\n
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
