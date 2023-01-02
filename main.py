from blizzardapi import BlizzardApi
import humanize
import fastapi

api_client = BlizzardApi("7d4b61f081a54497b7823e243c8602c1", "8EmB2xOHKoidvtHmLby5ncIyr2LEX1pv")

x = api_client.wow.game_data.get_token_index("EU", "en_gb")

g = int(x["price"])/10000

t = g/15

app = fastapi.FastAPI()

def to_price(s):
	s = str(round(float(s), 2)).split(".")
	return f"£{humanize.intcomma(s[0])}.{s[1]}"
	

def gold_to_gbp(gold=1, silver=0, copper=0):
	total = gold + (silver/100) + (copper/10000)
	return to_price(total/t)#, total/t
	
def gbp_to_gold(gbp):
	return humanize.intcomma(int(t * gbp)) + "g"#,  t * gbp




@app.get("/gbp/{gold}")
async def gbp(gold: float):
    results = {"gold": gold, "gbp": gold_to_gbp(gold)}
    return results
   
@app.get("/gold/{gbp}")
async def gold(gbp: float):
    results = {"gold": gbp_to_gold(gbp), "gbp": gbp}
    return results
    
