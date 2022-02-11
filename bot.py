import discord 
import datetime
import requests
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument , CommandNotFound
from decouple import config

bot = commands.Bot("!")
@bot.event 
async def on_ready( ):
    print(f"LETS GOOOO eu estou conectado como {bot.user}")
    await bot.change_presence(activity = discord.Activity
    (type= discord.ActivityType.playing, name="World of Tanks Blitz"))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "puta"  in message.content:
        embed = discord.Embed(
            title= "Cuidado!",
            description = "Não use palavras de baixo calão!",
            color = 0xff0000
        )
        await message.channel.send(embed = embed)
        await message.delete() 
    if "desgraçado"  in message.content:
        embed = discord.Embed(
            title= "Cuidado!",
            description = "Não use palavras de baixo calão!",
            color = 0xff0000
        )
        await message.channel.send(embed = embed)
        await message.delete() 
    if "desgraça"  in message.content:
        embed = discord.Embed(
            title= "Cuidado!",
            description = "Não use palavras de baixo calão!",
            color = 0xff0000
        )
        await message.channel.send(embed = embed)
        await message.delete() 
    if "caralho"  in message.content:
        embed = discord.Embed(
            title= "Cuidado!",
            description = "Não use palavras de baixo calão!",
            color = 0xff0000
        )
        await message.channel.send(embed = embed)
        await message.delete() 
    await bot.process_commands(message) 
    if "porra"  in message.content:
        embed = discord.Embed(
            title= "Cuidado!",
            description = "Não use palavras de baixo calão!",
            color = 0xff0000
        )
        await message.channel.send(embed = embed)
        await message.delete()
    if "buceta"  in message.content:
        embed = discord.Embed(
            title= "Cuidado!",
            description = "Não use palavras de baixo calão!",
            color = 0xff0000
        )
        await message.channel.send(embed = embed)
        await message.delete()
    if "bct"  in message.content:
        embed = discord.Embed(
            title= "Cuidado!",
            description = "Não use palavras de baixo calão!",
            color = 0xff0000
        )
        await message.channel.send(embed = embed)
        await message.delete()
    if "arrombado"  in message.content:
        embed = discord.Embed(
            title= "Cuidado!",
            description = "Não use palavras de baixo calão!",
            color = 0xff0000
        )
        await message.channel.send(embed = embed)
        await message.delete()

@bot.event
async def on_command_error(ctx,error):
   if isinstance(error,MissingRequiredArgument):
        embed = discord.Embed(
            title= "Atenção!",
            description = "O comando está incompleto! Consulte !ajuda para ver o comando completo!",
            color = 0xff0000
        )
        await ctx.send(embed = embed)
           
   if isinstance(error,CommandNotFound):
        embed = discord.Embed(
            title= "Atenção!",
            description = "Este comando não existe na lista de comandos do bot! Consulte !ajuda para ver a lista de comandos possíveis!",
            color = 0xff0000
        )
        await ctx.send(embed = embed)

@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name

    resposta = "Olá, " + name

    await ctx.send(resposta)

@bot.command(name="hr")
async def send_time(ctx):

    now = datetime.datetime.now()

    now = now.strftime("%d/%m/%Y às %H:%M")

    channel = bot.get_channel(928708614632382504)
    await channel.send("Data atual: " + now)

@bot.command(name="calc")
async def calculate_some_expression(ctx,expression):
    response = eval(expression)
    await ctx.send("A resposta é: "+ str(response))

@bot.command()
async def binance(ctx,coin,base):

    try:
        response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
        data = response.json()
        price = data.get("price")
        if price:
            await ctx.send(f"O valor de de 1 {coin} em {base} é {price}")
        else:
            await ctx.send("Moeda invalida!")
    except:
        await ctx.send("Algo deu errado!")

@bot.command(name="dm")
async def direct_message(ctx):
    embed = discord.Embed(
        title = "Olá!",
        description = "Sou um bot desenvolvido pelo Sir Fortesque para o servidor do Berlim's Panzers! Conheça a equipe que criou o servidor!",
        color = 0x00ffff
    )
    embed.set_author(name=bot.user.name, icon_url= bot.user.avatar_url)
    embed.set_footer(text= "By Sir Fortesque", icon_url = "https://imgur.com/mgbdede.png")
    embed.set_image(url= "https://imgur.com/FaOnIp6.png")
    embed.set_thumbnail (url = "https://c.tenor.com/K3ysWo8hdloAAAAd/tank.gif")
    embed.add_field(name="Inteer",value="líder do clã/criador do Discord Server")
    embed.add_field(name="MadSoldierBr",value="vice-líder do clã")
    embed.add_field(name="Erwin Rommel",value="vice-líder do clã")
    embed.add_field(name="Cronos_825",value="Apoiador Discord Server")
    embed.add_field(name="Doidoendoidado",value="Apoiador/Programador Discord Server")
    embed.add_field(name="Esses somos nós",value="Aqui você encontra um espaço perfeito para se comunicar com os outros membros do clã! Aproveite!", inline=False)

    try:
        await ctx.author.send(embed = embed)
    except:
        await ctx.send("Eu não tenho acesso a sua DM! Para receber as mensagens na DM ative-a e refaça o comando novamente!")

@bot.command(name="ajuda")
async def get_embed(ctx):

    embed = discord.Embed(
        title = "Precisa de ajuda?",
        description = "Você pode usar os seguintes comandos no bot:",
        color = 0x00ff00
    )
    embed.set_author(name=bot.user.name, icon_url= bot.user.avatar_url)
    embed.set_footer(text= "By Sir Fortesque", icon_url = "https://imgur.com/mgbdede.png")
    embed.set_image(url= "https://imgur.com/FaOnIp6.png")
    embed.add_field ( name="Ver hora atual:",value = "Comando !hr")
    embed.add_field (name="Mandar DM:",value = "Comando !dm")
    embed.add_field ( name="Mandar uma saudação:",value = "Comando !oi")
    embed.add_field ( name="Calcular uma expressão:",value = "Comando !calc")
    embed.add_field ( name="Ver preço de moedas:",value = "Comando !binance (sigla das moedas)")
    embed.add_field ( name="Precisa de mais alguma ajuda?",value = "Mande uma DM pro Fortesque!",inline=False)
    embed.set_thumbnail (url = "https://c.tenor.com/K3ysWo8hdloAAAAd/tank.gif")

    await ctx.send(embed = embed)




bot.run('OTMzMDQxNTk3ODYyNTE4ODE1.YebwtA.OYBPS-kuQtWAr3dBcLkQVzCmrRc')
