# investor_assessment_app

#Overview - business purpose
This FinTech app is designed to help financial advisors attract new client by providing a free report. The app takes basic information 
input by the advisor and/ or client and provides a recommended portfolio of ETFs based on the potential client's risk profile.
The report includes monte carlo simulations and portfolio comparisons.
The advisor can then leverage this free report into an ongoing client relationship.

#Financial details
The app uses 6 profiles that are simplified versions of profiles created by RBC Wealth Management.
The RBC Welath Management Model: !(Resources/RCC_wealth_mgt_model.png)

ETFs are mapped to the 6 profiles using the risk percentages provided by RBC.
RBC percentages mapped to ETFs: (input graph link)

ETFs were chosen by xxxx



#Overview - technology
This app (portfolio_suitability.ipynb) uses python, pandas and various libraries to collect data, process data, create graphs and develop a pdf.
Market data is pulled into the app using the Alpaca API.
User information is gathered through a CLI leveraging questionary.
The monte carlo simulations are done using MCForecastTools.py
The pdf is developed using FPDF

Please note: the pdf functionality does not work in Jupyter Notebook. We recommend Visual Studio.
Please note: You must create your own Alpaca account and related .env file for this app to function.


#The following libraries and imports are required:

'''
import os
import requests
import json
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from fpdf import FPDF
from MCForecastTools import MCSimulation
from pathlib import Path
%matplotlib inline
# from mailer import Mailer
import questionary
import fire
from questionary.constants import NO, YES, YES_OR_NO
import sqlalchemy
import hvplot.pandas
'''

#Technical details
Please note: the pdf functionality does not work in Jupyter Notebook. We recommend Visual Studio.

Create a database: sqlite is used to create a local database to hold data input by the user

Gather user data: The user inputs client data into a CLI using questionary technology stored in the
questionary_info.py file. This file is modularized and called into the main app. Questionary asks the following questions:
            What is your name?
            What is your phone number?
            What is your email address?
            What’s your annual income?
            How many years of investing experience do you have?
            What is the amount you want to start investing?
            What are your annual expenses?
            Is your source of income stable?
            What is your level of risk? (Low, Moderate, High, Speculative)
            What do you want to do with this investment? (Income, Growth, Value, Income/ Growth, Income/ Value, Growth/ Value, Income/Growth/ Value)
            How long do you plan to invest the money in years?

Getting Market Data: Using keys stored in a .env file, the app connect to Alpaca and pulls market data for ETFs. Please note: You must create your own Alpaca
account and related .env file for this app to function.

Cleaning Market Data:

Calculate a risk score:

Matching etfs to portfolios:

Calculate daily returns and cumulative returns

Run monte carlo simulations

Create graphs

Create pdf report





#created by
This app is brought to you by Jack Investments founded by Charles Brown, Jacob Burnett, Kevin Gross, Ann Howell
"We are with you however the market moves."

#License
MIT