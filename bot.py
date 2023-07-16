import streamlit as st
import openai
import requests
import json
import Constants

openai.api_key = Constants.OPENAI_API_KEY



# Below is the url and the params on which the thrid API will be called
def stock_screener(market_cap_more_than=None, market_cap_less_than=None, price_more_than=None, price_less_than=None, beta_more_than=None, beta_less_than=None, volume_more_than=None, volume_less_than=None, dividend_more_than=None, dividend_less_than=None, is_etf=False, is_actively_trading=False, sector=None, industry=None, country=None, exchange=None, limit=None):
    base_url = 'https://financialmodelingprep.com/api/v3/stock-screener'
    api_key = Constants.FINANCIAL_MODEL_API_TOKEN

    params = {
        'apikey': api_key,
        'marketCapMoreThan': market_cap_more_than,
        'marketCapLowerThan': market_cap_less_than,
        'priceMoreThan': price_more_than,
        'priceLowerThan': price_less_than,
        'betaMoreThan': beta_more_than,
        'betaLowerThan': beta_less_than,
        'volumeMoreThan': volume_more_than,
        'volumeLowerThan': volume_less_than,
        'dividendMoreThan': dividend_more_than,
        'dividendLowerThan': dividend_less_than,
        'isEtf': is_etf,
        'isActivelyTrading': is_actively_trading,
        'sector': sector,
        'industry': industry,
        'country': country,
        'exchange': exchange,
        'limit': limit,
    }

    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url, params=params)

    # Format the request URL and params for display
    request_url = response.url
    st.expander("API Call").write(request_url)

    return json.dumps(response.json())



def annual_income_statement(stock_symbol=None,limit=None):
    base_url = 'https://financialmodelingprep.com/api/v3/income-statement/'
    api_key = Constants.FINANCIAL_MODEL_API_TOKEN 

    params = {
        'apikey': api_key,
        'stock_symbol': stock_symbol,
        'limit': limit,
    }

    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url + stock_symbol, params = params)

    # Format the request URL and params for display
    request_url = response.url
    st.expander("API Call").write(request_url)

    return json.dumps(response.json())



def balance_sheet_statement(stock_symbol=None, limit=None):
    base_url = 'https://financialmodelingprep.com/api/v3/balance-sheet-statement/'
    api_key = Constants.FINANCIAL_MODEL_API_TOKEN

    params = {
        'apikey': api_key,
        'stock_symbol': stock_symbol,
        'limit': limit,
    }

    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url + stock_symbol, params=params)

    # Format the request URL and params for display
    request_url = response.url
    st.expander("API Call").write(request_url)

    return json.dumps(response.json())



def cash_flow_statement(stock_symbol=None,limit=None):
    base_url = 'https://financialmodelingprep.com/api/v3/cash-flow-statement/'
    api_key = Constants.FINANCIAL_MODEL_API_TOKEN

    params = {
        'apikey': api_key,
        'stock_symbol': stock_symbol,
        'limit': limit,
    }

    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url + stock_symbol, params=params)

    # Format the request URL and params for display
    request_url = response.url
    st.expander("API Call").write(request_url)

    return json.dumps(response.json())



def company_financial_ratios(stock_symbol=None,limit=None):
    base_url = 'https://financialmodelingprep.com/api/v3/ratios/'
    api_key = Constants.FINANCIAL_MODEL_API_TOKEN

    params = {
        'apikey': api_key,
        'stock_symbol': stock_symbol,
        'limit': limit,
    }

    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url + stock_symbol, params=params)

    # Format the request URL and params for display
    request_url = response.url
    st.expander("API Call").write(request_url)

    return json.dumps(response.json())



def financial_statement_growth(stock_symbol=None,limit=None):
    base_url = 'https://financialmodelingprep.com/api/v3/income-statement-growth/'
    api_key = Constants.FINANCIAL_MODEL_API_TOKEN

    params = {
        'apikey': api_key,
        'stock_symbol': stock_symbol,
        'limit': limit,
    }

    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url + stock_symbol, params=params)

    # Format the request URL and params for display
    request_url = response.url
    st.expander("API Call").write(request_url)

    return json.dumps(response.json())



def most_gainer_stocks(limit = None):
    base_url = 'https://financialmodelingprep.com/api/v3/stock_market/gainers'
    api_key = Constants.FINANCIAL_MODEL_API_TOKEN

    params = {
        'apikey': api_key,
        'limit': limit,
    }

    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url, params=params)

    # Format the request URL and params for display
    request_url = response.url
    st.expander("API Call").write(request_url)

    return json.dumps(response.json())



def most_loser_stocks(limit = None):
    base_url = 'https://financialmodelingprep.com/api/v3/stock_market/losers'
    api_key = Constants.FINANCIAL_MODEL_API_TOKEN

    params = {
        'apikey': api_key,
        'limit': limit,
    }

    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url, params=params)

    # Format the request URL and params for display
    request_url = response.url
    st.expander("API Call").write(request_url)

    return json.dumps(response.json())



def most_active_stocks(limit=None):
    base_url = 'https://financialmodelingprep.com/api/v3/stock_market/actives'
    api_key = Constants.FINANCIAL_MODEL_API_TOKEN

    params = {
        'apikey': api_key,
        'limit': limit,
    }

    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url, params=params)

    # Format the request URL and params for display
    request_url = response.url
    st.expander("API Call").write(request_url)

    return json.dumps(response.json())








# Below are the methods to convert response of third party API into function_response which will be fed to openAi's API to change it into human readable form.

def generate_response_stock_screener(data):
    function_response = ""
    for i in range(len(data)):
        stock_info = data[i]
        function_response += f"\n\nStock {i+1}:\n- Symbol: {stock_info['symbol']}\n- Country: {stock_info['country']}\n- Company Name: {stock_info['companyName']}\n- Market Cap: {stock_info['marketCap']}\n- Sector: {stock_info['sector']}\n- Industry: {stock_info.get('industry', 'N/A')}\n- Beta: {stock_info['beta']}\n- Volume: {stock_info['volume']}\n- Exchange: {stock_info['exchange']}\n- Last Annual Dividend: {stock_info['lastAnnualDividend']}"
    return function_response


def generate_response_for_annual_income_statement(data):
    function_response = ""
    for i in range(len(data)):
        stock_info = data[i]
        function_response += f"\n\nStock {i+1}:\n- Symbol: {stock_info['symbol']}\n- Currency: {stock_info['reportedCurrency']}\n- Filling Date: {stock_info['fillingDate']}\n- Revenue: {stock_info['revenue']}\n- Gross Profit: {stock_info['grossProfit']}\n- R&D Expenses: {stock_info['researchAndDevelopmentExpenses']}\n- General Administrative Expenses: {stock_info['sellingGeneralAndAdministrativeExpenses']}\n- Operating Expenses: {stock_info['operatingExpenses']}\n- Interest Income: {stock_info['interestIncome']}\n- Depreciation And Amortization: {stock_info['depreciationAndAmortization']}\n- Ebita: {stock_info['ebitda']}, Operating Income: {stock_info['operatingIncome']}\n- Income Before Tax: {stock_info['incomeBeforeTax']}\n- Net Income: {stock_info['netIncome']}\n- EPS: {stock_info['eps']}"
    return function_response


def generate_response_for_balance_sheet_statement(data):
    function_response=""
    for i in range(len(data)):
        stock_info = data[i]
        function_response += f"\n\nStock {i+1}:\n- Symbol: {stock_info['symbol']}\n- Currency: {stock_info['reportedCurrency']}\n- Filling Date: {stock_info['fillingDate']}\n- Total Cash: {stock_info['cashAndCashEquivalents']}\n- Short Term Investments: {stock_info['shortTermInvestments']}\n- Total Currency Assets: {stock_info['totalCurrentAssets']}\n- Long Term Assets: {stock_info['longTermInvestments']}\n- Total Assets: {stock_info['totalAssets']}\n- Amount Payable: {stock_info['accountPayables']}\n- Short Term Debt: {stock_info['shortTermDebt']}\n- Total Long Term Debt: {stock_info['longTermDebt']}\n- Total Current Liabilities: {stock_info['totalLiabilities']}\n- Total Debt: {stock_info['totalDebt']}\n- Net Debt: {stock_info['netDebt']}"
    return function_response


def generate_response_for_cash_flow_statement(data):
    function_response=""
    for i in range(len(data)):
        stock_info = data[i]
        function_response += f"\n\nStock {i+1}:\n- Symbol: {stock_info['symbol']}\n- Currency: {stock_info['reportedCurrency']}\n- Filling Date: {stock_info['fillingDate']}\n- Net Income : {stock_info['netIncome']}\n- Depreciation And Amortization: {stock_info['depreciationAndAmortization']}\n- Change In Working Capital: {stock_info['changeInWorkingCapital']}\n- Net Cash Provided By Operating Activities: {stock_info['netCashProvidedByOperatingActivities']}\n- Investments In Property Plant And Equipment: {stock_info['investmentsInPropertyPlantAndEquipment']}\n- Acquisitions Net: {stock_info['acquisitionsNet']}\n- Net Cash Used For Investing Activites: {stock_info['netCashUsedForInvestingActivites']}\n- Debt Repayment: {stock_info['debtRepayment']}\n- Dividends Paid: {stock_info['dividendsPaid']}\n- Capital Expenditure: {stock_info['capitalExpenditure']}\n- Free Cash Flow: {stock_info['freeCashFlow']}"
    return function_response


def generate_response_for_company_financial_ratios(data):
    function_response = ""
    for i in range(len(data)):
        stock_info = data[i]
        function_response += f"\n\nStock {i+1}:\n- Symbol: {stock_info['symbol']}\n- Operating Cycle: {stock_info['operatingCycle']}\n- Gross Profit Margin: {stock_info['grossProfitMargin']}\n- Operating Profit Margin: {stock_info['operatingProfitMargin']}\n- Net Profit Margin: {stock_info['netProfitMargin']}\n- Debt To Equity Ratio: {stock_info['debtEquityRatio']}\n- Effective Tax Rates: {stock_info['effectiveTaxRate']}\n- Return to Equity: {stock_info['returnOnEquity']}\n- Debt to Equity Ratio: {stock_info['debtEquityRatio']}\n- Free Cash Per Share: {stock_info['freeCashFlowPerShare']}\n- Dividend Payout Ratio: {stock_info['dividendPayoutRatio']}\n- Price to Book Value Ratio: {stock_info['priceBookValueRatio']}\n- Price Earnings Ratio: {stock_info['priceEarningsRatio']}\n- Dividend Yield: {stock_info['dividendYield']}\n- Price Fair Value: {stock_info['priceFairValue']}"
    return function_response


def generate_response_for_financial_statement_growth(data):
    function_response = ""
    for i in range(len(data)):
        stock_info = data[i]
        function_response += f"\n\nStock {i+1}:\n- Symbol: {stock_info['symbol']}\n- Growth in Revenue: {stock_info['growthRevenue']}\n- Growth in Gross Profit: {stock_info['growthGrossProfit']}\n- Growth in Gross Profit Ratio: {stock_info['growthGrossProfitRatio']}\n- growth in Research And Development Expenses: {stock_info['growthResearchAndDevelopmentExpenses']}\n- Growth in Operating Expenses: {stock_info['growthOperatingExpenses']}\n- Growth in Depreciation And Amortization: {stock_info['growthDepreciationAndAmortization']}\n- Growth EBITDA: {stock_info['growthEBITDA']}\n- Growth in Operating Income: {stock_info['growthOperatingIncome']}\n- Growth in Income Before Tax: {stock_info['growthIncomeBeforeTax']}\n- Growth in Net Income: {stock_info['growthNetIncome']}\n- Growth in EPS: {stock_info['growthEPS']}"
    return function_response


def generate_response_for_most_gainer_stocks(data):
    function_response = ""
    for i in range(len(data)):
        stock_info = data[i]
        function_response += f"\n\nStock {i+1}:\n- Symbol: {stock_info['symbol']}\n- Name: {stock_info['name']}\n- Change: {stock_info['change']}\n- Price: {stock_info['price']}\n- Percentage Change: {stock_info['changesPercentage']}"
    return function_response


def generate_response_for_most_losers_stocks(data):
    function_response = ""
    for i in range(len(data)):
        stock_info = data[i]
        function_response += f"\n\nStock {i+1}:\n- Symbol: {stock_info['symbol']}\n- Name: {stock_info['name']}\n- Change: {stock_info['change']}\n- Price: {stock_info['price']}\n- Percentage Change: {stock_info['changesPercentage']}"
    return function_response


def generate_response_for_most_active_stocks(data):
    function_response = ""
    for i in range(len(data)):
        stock_info = data[i]
        function_response += f"\n\nStock {i+1}:\n- Symbol: {stock_info['symbol']}\n- Name: {stock_info['name']}\n- Change: {stock_info['change']}\n- Price: {stock_info['price']}\n- Percentage Change: {stock_info['changesPercentage']}"
    return function_response






# Below are the list of function calls out of which openAI will choose which to use to extract params according to the input query.

function_descriptions_multiple = [
    {
        "name": "stock_screener",
        "description": "Fetch stock details based on various details like marketCapMoreThan, marketCapLowerThan, priceMoreThan, priceLowerThan, betaMoreThan, betaLowerThan, volumeMoreThan, volumeLowerThan, dividendMoreThan, dividendLowerThan, isEtf, isActivelyTrading, sector and industry",
        "parameters": {
            "type": "object",
            "properties": {
                "market_cap_more_than": {
                    "type": "number",
                    "description": "This contains the minimum value of market capitalisation required",
                    },
                "market_cap_less_than": {
                    "type": "number",
                    "description": "This contains the maximum value of market capitalisation required",
                    },
                "price_more_than": {
                    "type": "number",
                    "description": "This contains the minimum required price of stock",
                    },
                "price_less_than": {
                    "type": "number",
                    "description": "This contains the maximum required price of stock",
                    },
                "beta_more_than": {
                    "type": "number",
                    "description": "This contains the minimum required beta value of stock",
                    },
                "beta_less_than": {
                    "type": "number",
                    "description": "This contains the maximum required beta value of stock",
                    },
                "volume_more_than": {
                    "type": "number",
                    "description": "This contains the minimum required volume of stock",
                    },
                "volume_less_than": {
                    "type": "number",
                    "description": "This contains the maximum required volume of stock",
                    },
                "dividend_more_than": {
                    "type": "number",
                    "description": "This contains the minimum required dividend of stock",
                    },
                "dividend_less_than": {
                    "type": "number",
                    "description": "This contains the maximum required dividend of stock",
                    },
                "is_etf": {
                    "type": "boolean",
                    "description": "if the stock is a type of etf",
                    },
                "is_actively_trading": {
                    "type": "boolean",
                    "descriptioin": "Is the stock currently trading actively",
                    },
                "sector": {
                    "type": "string",
                    "description": "the sector of the stock",
                    },
                "industry": {
                    "type": "string",
                    "description": "industry of the stock",
                    },
                "country": {
                    "type": "string",
                    "description": "the 2 digit abbriviated value of country in which the stock is listed",
                    }, 
                    "unit": {"type": "string", "enum": ["IN", "US", "JP", "BR", "GB", "CN", "FR", "AU"]},
                "exchange": {
                    "type": "string",
                    "description": "the stock exchange on the basis of country in which the stock is listed",
                    },
                "limit": {
                    "type": "number",
                    "description": "total number of stocks expected in the result",
                    },
            },
            "required": [],
        },
    },
    {
        "name":"annual_income_statement",
        "description": "Fetch annual income statement of the stock",
        "parameters": {
            "type": "object",
            "properties": {
                "stock_symbol":{
                    "type": "string",
                    "description": "The symbol of stock listed in the market, e.g. RELIANCE, TCS",
                },                      
                "limit": {
                    "type": "number",
                    "description": "Total number of stocks to be fetched, e.g. 1",
                    },
            },
            "required": ["stock_symbol"],
        },
    },
    {
        "name": "balance_sheet_statement",
        "description": "Fetch balance statement of the stock",
        "parameters": {
            "type": "object",
            "properties": {
                "stock_symbol":{
                    "type": "string",
                    "description": "The symbol of stock listed in the market, e.g. RELIANCE, TCS",
                },                      
                "limit": {
                    "type": "number",
                    "description": "Total number of stocks to be fetched, e.g. 1",
                    },
            },
            "required": ["stock_symbol"],
        }
    },
    {
        "name": "cash_flow_statement",
        "description": "Fetch cash flow statement of the stock",
        "parameters": {
            "type": "object",
            "properties": {
                "stock_symbol":{
                    "type": "string",
                    "description": "The symbol of stock listed in the market, e.g. RELIANCE, TCS",
                },                      
                "limit": {
                    "type": "number",
                    "description": "Total number of stocks to be fetched, e.g. 1",
                    },
            },
            "required": ["stock_symbol"],
        }
    },
    {
        "name": "company_financial_ratios",
        "description": "Gives all the financial ratios of the stock",
        "parameters": {
            "type": "object",
            "properties": {
                "stock_symbol":{
                    "type": "string",
                    "description": "The symbol of stock listed in the market, e.g. RELIANCE, TCS",
                },                      
                "limit": {
                    "type": "number",
                    "description": "Total number of stocks to be fetched, e.g. 1",
                    },
            },
            "required": ["stock_symbol"],
        }
    },
    {
    
        "name": "financial_statement_growth",
        "description": "Gives all the growth realted attributes of the stock",
        "parameters": {
            "type": "object",
            "properties": {
                "stock_symbol":{
                    "type": "string",
                    "description": "The symbol of stock listed in the market, e.g. RELIANCE, TCS",
                },                      
                "limit": {
                    "type": "number",
                    "description": "Total number of stocks to be fetched, e.g. 1",
                    },
            },
            "required": ["stock_symbol"],
        }
    },
    {
        "name": "most_gainer_stocks",
        "description": "Gives out list of stocks which gained most in recent times",
        "parameters": {
            "type": "object",
            "properties": {                  
                "limit": {
                    "type": "number",
                    "description": "Total number of stocks to be fetched, e.g. 1",
                    },
            },
            "required": [],
        }
    },
    {
        "name": "most_loser_stocks",
        "description": "Gives out list of stocks which lost most in recent times",
        "parameters": {
            "type": "object",
            "properties": {                  
                "limit": {
                    "type": "number",
                    "description": "Total number of stocks to be fetched, e.g. 1",
                    },
            },
            "required": [],
        }
    },
    {
        "name": "most_active_stocks",
        "description": "Gives out list of stocks which was most volatile in recent times",
        "parameters": {
            "type": "object",
            "properties": {                  
                "limit": {
                    "type": "number",
                    "description": "Total number of stocks to be fetched, e.g. 1",
                    },
            },
            "required": [],
        }
    },
]





# Extracting the parameters with the help of functions
def run_conversation(user_message):
    print("\nPrinting User Message ")
    print(user_message)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {
                "role": "user", 
                "content": user_message
            }
        ],
        functions=function_descriptions_multiple,
        function_call="auto",
        max_tokens=100,
    )


    # openai will give some response
    message = response["choices"][0]["message"]
    print("\nPrinting Message")
    print(message)
    # st.write(message)


    # Made this dummy dictonary to initialize data variable in line 567
    dummy_dict = {'a':34, 'b':61, 'c':82}


    # Calling the third party API which will give us our desiered result in raw format
    if message.get("function_call"):
        function_name = message["function_call"]["name"]
        function_args = json.loads(message["function_call"]["arguments"])
        data = json.dumps(dummy_dict, indent=4)

        if function_name == "stock_screener":
            data = json.loads(stock_screener(
            market_cap_more_than=function_args.get("market_cap_more_than"),
            market_cap_less_than=function_args.get("market_cap_less_than"),
            price_more_than=function_args.get("price_more_than"),
            price_less_than=function_args.get("price_less_than"),
            beta_more_than=function_args.get("beta_more_than"),
            beta_less_than=function_args.get("beta_less_than"),
            volume_more_than=function_args.get("volume_more_than"),
            volume_less_than=function_args.get("volume_less_than"),
            dividend_more_than=function_args.get("dividend_more_than"),
            dividend_less_than=function_args.get("dividend_less_than"),
            is_etf=function_args.get("is_etf"),
            is_actively_trading=function_args.get("is_actively_trading", "True"),
            sector=function_args.get("sector"),
            industry=function_args.get("industry"),
            country=function_args.get("country"),
            exchange=function_args.get("exchange", "NSE,BSE,NASDAQ,NYSE,AMEX"),
            limit=function_args.get("limit", 5)  
            ))
        elif function_name == "annual_income_statement":
            data=json.loads(annual_income_statement(
            stock_symbol=function_args.get("stock_symbol"),
            limit=function_args.get("limit", 1),
            ))
        elif function_name == "balance_sheet_statement":
            data = json.loads(balance_sheet_statement(
                stock_symbol=function_args.get("stock_symbol"),
                limit=function_args.get("limit", 1),
            ))
        elif function_name == "cash_flow_statement":
            data=json.loads(cash_flow_statement(
            stock_symbol=function_args.get("stock_symbol"),
            limit=function_args.get("limit", 1),
            ))
        elif function_name == "company_financial_ratios":
            data=json.loads(company_financial_ratios(
            stock_symbol=function_args.get("stock_symbol"),
            limit=function_args.get("limit", 1),
            ))
        elif function_name == "financial_statement_growth":
            data=json.loads(financial_statement_growth(
            stock_symbol=function_args.get("stock_symbol"),
            limit=function_args.get("limit", 1),
            ))
        elif function_name == "most_gainer_stocks":
            data=json.loads(most_gainer_stocks(
            limit=function_args.get("limit", 1),
            ))
        elif function_name == "most_loser_stocks":
            data=json.loads(most_loser_stocks(
            limit=function_args.get("limit", 1),
            ))
        elif function_name == "most_active_stocks":
            data=json.loads(most_active_stocks(
            limit=function_args.get("limit", 1),
            ))

        print("\nPrinting function_name")
        print(function_name)


        # Data holds the data about the stock which will be printed in a human readable format using openai's API.
        print("\n Printing data fetch from thrid party API")
        print(data)
    
    else:
        function_name = "invalid-input-function"



 # This will hold the output of the thrid party API which will now be converted into more readable format using openai
    function_response = ""

    if function_name == "stock_screener":
        function_response = generate_response_stock_screener(data)
    elif function_name == "annual_income_statement":
        function_response = generate_response_for_annual_income_statement(data)
    elif function_name == "balance_sheet_statement":
        function_response = generate_response_for_balance_sheet_statement(data)
    elif function_name == "cash_flow_statement":
        function_response = generate_response_for_cash_flow_statement(data)
    elif function_name == "company_financial_ratios":
        function_response = generate_response_for_company_financial_ratios(data)
    elif function_name == "financial_statement_growth":
        function_response = generate_response_for_financial_statement_growth(data)
    elif function_name == "most_gainer_stocks":
        function_response = generate_response_for_most_gainer_stocks(data)
    elif function_name == "most_loser_stocks":
        function_response = generate_response_for_most_losers_stocks(data)
    elif function_name == "most_active_stocks":
        function_response = generate_response_for_most_active_stocks(data)
    else:
        function_response = "Please throw invalid input error"


    print("\nPrinting function_response")
    print(function_response)

    # Generating better readable text
    # Create a placeholder to stream the assistant's responses to Streamlit
    placeholder_response = st.empty()

    # Make a new API call to OpenAI with the previous message's content and the function response, and apply streaming
    second_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[
        {"role": "system", "content": """ You are supposed to convert the input data into human readable format, some of the fields you will be given are groosProfitMargin, operatingProfitMargin, netProfitMargin, debtEquityRatio, returnOnEquity.
            Follow these instructions in your response:
            - Use human readable format for price (i.e write in billion , trillion, million)
            - Use conversion according to country (i.e USD for US and Rupee for IN)
            - Convert margins into percentage
            - Write ratio upto 2 decimal places only
            - Always specify the Currency if the currency value is present
            - If you find throw invalid input error then return Please enter valid input
            - Only respond if there is an API response, if not say that the input is invalid
            """},
        {
            "role": "user", 
            "content": user_message
        },
        {
            "role": "assistant", 
            "content": message["content"] if message["content"] else 'Initiating function call...'
        },
        {
            "role": "function",
            "name": function_name,
            "content": function_response,
        },
    ],
    stream=True,
    max_tokens=128
    )


    # Display the response in Streamlit in real-time as chunks are received
    assistant_response = ""
    for chunk in second_response:
        if "role" in chunk["choices"][0]["delta"]:
            continue
        elif "content" in chunk["choices"][0]["delta"]:
            r_text = chunk["choices"][0]["delta"]["content"]
            assistant_response += r_text
            placeholder_response.markdown(assistant_response, unsafe_allow_html=True)

    print(assistant_response)
    return assistant_response
    


# Start the bot

def stock_screener_app():
    st.title('Trading Helper Bot')
    st.write('Please enter your stock screening query below:')
    
    user_input = st.text_input("Eample Query: Give me list of 5 Indian Stocks with market cap more than 10 billions.")
    if st.button('Run'):
        run_conversation(user_input)
    
if __name__ == "__main__":
    stock_screener_app()
    
    

    