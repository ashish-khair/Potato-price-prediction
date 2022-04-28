from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=24&Tx_State=UP&Tx_District=1&Tx_Market=0&DateFrom=20-Mar-2021&DateTo=20-Mar-2021&Fr_Date=20-Mar-2021&To_Date=20-Mar-2021&Tx_Trend=0&Tx_CommodityHead=Potato&Tx_StateHead=Uttar+Pradesh&Tx_DistrictHead=Agra&Tx_MarketHead=--Select--'

start = input('Enter the date from: ')
end = input("Enter the date to: ")
market = input("Enter the market name: ")

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)


# starting date
starting_date = driver.find_element(By.NAME, value = "ctl00$txtDate")
starting_date.clear()
starting_date.send_keys(start)

# ending_date
ending_date = driver.find_element(By.NAME, value = "ctl00$txtDateTo")
ending_date.clear()
ending_date.send_keys(end)

#market name
market_name = driver.find_element(By.NAME, value = "ctl00$ddlMarket")
market_name.send_keys(market)

# Search and download
go= driver.find_element(By.NAME,value = 'ctl00$btnGo')
go.click()
export = driver.find_element(By.NAME, value = "ctl00$cphBody$ButtonExcel")
export.click()