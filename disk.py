from discord_webhook import DiscordWebhook,DiscordEmbed
webhookurl="https://discord.com/api/webhooks/1019113357653065788/MUebVsWHRRfq-XYS2pDDAVyir5FuahBcMxGxS0ArNUsgj40UMcdS_1NWc2Cw9oCwF_gh"
webhook=DiscordWebhook(url=webhookurl)

c=1
while 1>0:
 c=c+1
 for i in range(0,1001):
    if i==1000:
       embed=DiscordEmbed(title="------------------RESULT----------------",description=str(c)+"times",color="ED4245")
       webhook.add_embed(embed)
       webhook.execute()
           

