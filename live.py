#from thefirstock import thefirstock
import json
import requests

class thefirstock1():

    def __init__(self):
        self.user_id = None
        self.jKey = None
    def login(self,userId,password,TOTP,vendorCode,apiKey):
        ''' This is login function it takes 2 parameter marketdata api_key and secret_key'''
        try:
            uri="https://connect.thefirstock.com/api/V3/login"
            headers = {"Content-Type":"application/json"}
            params={"userId":userId,
            "password":password,
            "TOTP":TOTP,
            "vendorCode":vendorCode,
            "apiKey":apiKey}
            #paramss = json.dumps(params)
            response = requests.post(uri,json.dumps(params),headers)
            
            # response = response.content.decode('utf-8')
            response = json.loads(response.content)
            if response['status'] == 'Success':
                self.user_id  = response["data"]["actid"]
                self.jKey = response["data"]["susertoken"]
            return response
        except Exception as e:
            return e
        
    def get_quote(self,exchange,tradingSymbol):
        ''' This is login function it takes 2 parameter marketdata api_key and secret_key'''
        try:
            uri="https://connect.thefirstock.com/api/V3/getQuote"
            headers = {"Content-Type":"application/json"}#"Authorization":"00b713d070b62401c2ab4acbd1201ff524e31ab68bd65f7660e0f42beba02409"
            params={"userId":self.user_id,#"HS1765"
            "exchange":exchange,
            "token":tradingSymbol,
            "jKey":self.jKey}#"00b713d070b62401c2ab4acbd1201ff524e31ab68bd65f7660e0f42beba02409"
            #paramss = json.dumps(params)
            response = requests.post(uri,json.dumps(params),headers=headers)
            
            response = response.content.decode('utf-8')
            response = json.loads(response)
            # if response['status'] == 'Success':
            #     self.user_id  = userId
            #     self.jKey = response["data"]["susertoken"]
            return response
        except Exception as e:
            return e

    def search_script(self,stext):
        ''' This is login function it takes 2 parameter marketdata api_key and secret_key'''
        try:
            uri="https://connect.thefirstock.com/api/V4/searchScrips"
            headers = {"Content-Type":"application/json"}#"Authorization":"00b713d070b62401c2ab4acbd1201ff524e31ab68bd65f7660e0f42beba02409"
            params={"userId":self.user_id,#"HS1765"
            "stext":stext,
            "jKey":self.jKey}#"00b713d070b62401c2ab4acbd1201ff524e31ab68bd65f7660e0f42beba02409"
            #paramss = json.dumps(params)
            response = requests.post(uri,json.dumps(params),headers=headers)
            
            response = response.content.decode('utf-8')
            response = json.loads(response)
            # if response['status'] == 'Success':
            #     self.user_id  = userId
            #     self.jKey = response["data"]["susertoken"]
            return response
        except Exception as e:
            return e


    def get_option_chain(self,exchange,tradingSymbol,strikePrice,count):
        ''' This is login function it takes 2 parameter marketdata api_key and secret_key'''
        try:
            uri="https://connect.thefirstock.com/api/V3/optionChain"
            headers = {"Content-Type":"application/json"}#"Authorization":"00b713d070b62401c2ab4acbd1201ff524e31ab68bd65f7660e0f42beba02409"
            params={"userId":self.user_id,#"HS1765"
            "exchange":exchange,
            "tradingSymbol":tradingSymbol,
            "strikePrice":strikePrice,
            "count":count,
            "jKey":self.jKey}#"00b713d070b62401c2ab4acbd1201ff524e31ab68bd65f7660e0f42beba02409"
            #paramss = json.dumps(params)
            response = requests.post(uri,json.dumps(params),headers=headers)
            
            response = response.content.decode('utf-8')
            response = json.loads(response)
            # if response['status'] == 'Success':
            #     self.user_id  = userId
            #     self.jKey = response["data"]["susertoken"]
            return response
        except Exception as e:
            return e

    def get_ohlc_min(self,exchange,token,startTime,endTime,interval):
        ''' This is login function it takes 2 parameter marketdata api_key and secret_key'''
        try:
            uri="https://connect.thefirstock.com/api/V3/timePriceSeries"
            headers = {"Content-Type":"application/json"}#"Authorization":"00b713d070b62401c2ab4acbd1201ff524e31ab68bd65f7660e0f42beba02409"
            params={"userId":self.user_id,#"HS1765"
            "exchange":exchange,
            "token":token,
            "startTime":startTime,
            "endTime":endTime,
            "jKey":self.jKey,
            "interval":interval}#"00b713d070b62401c2ab4acbd1201ff524e31ab68bd65f7660e0f42beba02409"
            #paramss = json.dumps(params)
            response = requests.post(uri,json.dumps(params),headers=headers)
            
            response = response.content.decode('utf-8')
            response = json.loads(response)
            # if response['status'] == 'Success':
            #     self.user_id  = userId
            #     self.jKey = response["data"]["susertoken"]
            return response
        except Exception as e:
            return e

    def placeOrder(self,exchange,tradingSymbol,quantity,price,triggerPrice,product,transactionType,priceType,retention,remarks):
        ''' This is login function it takes 2 parameter marketdata api_key and secret_key'''
        try:
            uri="https://connect.thefirstock.com/api/V3/placeOrder"
            headers = {"Content-Type":"application/json"}#"Authorization":"00b713d070b62401c2ab4acbd1201ff524e31ab68bd65f7660e0f42beba02409"
            params={"userId":self.user_id,#"HS1765"
            "exchange":exchange,
            "tradingSymbol":tradingSymbol,
            "quantity":quantity,
            "price":price,
            "triggerPrice":triggerPrice,
            "product":product,
            "transactionType":transactionType,
            "priceType":priceType,
            "retention":retention,
            "remarks":remarks,
            "jKey":self.jKey}#"00b713d070b62401c2ab4acbd1201ff524e31ab68bd65f7660e0f42beba02409"
            #paramss = json.dumps(params)
            response = requests.post(uri,json.dumps(params),headers=headers)
            
            response = response.content.decode('utf-8')
            response = json.loads(response)
            # if response['status'] == 'Success':
            #     self.user_id  = userId
            #     self.jKey = response["data"]["susertoken"]
            return response
        except Exception as e:
            return e
