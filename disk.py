from discord_webhook import DiscordWebhook,DiscordEmbed
webhookurl="https://discord.com/api/webhooks/1019113357653065788/MUebVsWHRRfq-XYS2pDDAVyir5FuahBcMxGxS0ArNUsgj40UMcdS_1NWc2Cw9oCwF_gh"
webhook=DiscordWebhook(url=webhookurl)
embed=DiscordEmbed(title="------------------RESULT----------------",description="HEL23213LO",color="ED4245")
webhook.add_embed(embed)
while 1>0:
 for i in range(0,1000):
    if i==1000:
           webhook.execute()
           print("message received")

