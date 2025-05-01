from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://gol.gg/players/list/season-S15/split-ALL/tournament-ALL/"
driver = webdriver.Chrome()  # Make sure you have the ChromeDriver installed
driver.get(url)

# Wait for the page to load (you may need to adjust the sleep time or use WebDriverWait)
import time
time.sleep(5)

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# Find the player cells
player_cells = soup.find_all("td", class_="tablesaw-cell-persist")
print(player_cells)