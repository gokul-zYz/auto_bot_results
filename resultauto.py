from discord_webhook import DiscordWebhook,DiscordEmbed
from selenium import webdriver
import time
import cv2;
import textwrap;
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)


driver.maximize_window()
c="1"
var=401
def image(loc):
  def put_text(img, text, x_value, y_value):
    font = cv2.FONT_HERSHEY_DUPLEX
    wrapped_text = textwrap.wrap(text, width=10)
    x, y = 200, 40
    font_size = 2
    font_thickness = 3

    for i, line in enumerate(wrapped_text):
        textsize = cv2.getTextSize(line, font, font_size, font_thickness)[0]

        gap = textsize[1] + 40
        y = y_value + i * gap
        x = int((img.shape[1] - textsize[0]) / 2)
        cv2.putText(img, line, (x_value, y), font,
                    font_size,
                    (255,255,255),
                    font_thickness,
                    lineType = cv2.LINE_AA)


  img = cv2.imread(mail+".png")
  put_text(img, mail, 80, 150)
  cv2.imwrite(mail+".png", img)
def cord(y):
  webhookurl="https://discord.com/api/webhooks/1019113357653065788/MUebVsWHRRfq-XYS2pDDAVyir5FuahBcMxGxS0ArNUsgj40UMcdS_1NWc2Cw9oCwF_gh"
  webhook=DiscordWebhook(url=webhookurl)
  with open("E:/PYTHON/Selenium project/"+str(y)+".png", "rb") as f:
    embed=DiscordEmbed(title="------------------RESULT----------------",description=y,color="ED4245")
    webhook.add_embed(embed)
    webhook.add_file(file=f.read(), filename=str(y)+'.png')
    webhook.execute()
for i in range(0,100):
  if var<=495:
   driver.get("http://exam.pondiuni.edu.in/results/")
   const="19TH0"
   mail=const+str(var)
   driver.find_element_by_xpath('//*[@id="reg_no"]').send_keys(mail)
   driver.find_element_by_xpath('//*[@id="exam"]').send_keys("fifth")
   driver.find_element_by_xpath('//*[@id="print_app_form"]/span').click()
   time.sleep(1)
   try:
     driver.switch_to.alert.accept()
   except:
    print("SUCCESFULLY RETRIEVED")
    driver.get_screenshot_as_file(mail+".png")
    image(mail)
    
    cord(mail)
  c=str(int(c)+1)
  var=var+1
driver.quit()













  
