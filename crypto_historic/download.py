from cryptocmd import CmcScraper
import pandas as pd


tokens = ['ETH','MATIC','DAI','USDC']
start_date = "01-01-2017"
end_date = "31-03-2023"

def start():
    for token in tokens:
        scraper = CmcScraper(token, start_date, end_date)
        
        df = scraper.get_dataframe()

        exportDf = pd.DataFrame()

        exportDf["date"] = df["Date"]
        exportDf["price_usd"] = df["Close"]
        exportDf["market_cap_usd"] = df["Market Cap"]
        exportDf["token"] = token
        
        
        exportDf.to_csv(f"./data/{token}_price.csv", index=False)