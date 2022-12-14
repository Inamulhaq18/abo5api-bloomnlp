import requests
import psycopg2



API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def pushdbupdate(desc,productname):
    conn=psycopg2.connect("postgresql://hkmuctkbhmlhsr:59563300aab6c650f8bbc9cc4153df6a42054b71e9be00dda420f40bbbf791b2@ec2-54-76-43-89.eu-west-1.compute.amazonaws.com:5432/dd8a5bspvhrk8c") 
    curr=conn.cursor()
    sql_select_query = """UPDATE master_product_table SET "Product_describtion_en" = %s WHERE "Product_Name_en" = %s"""

    print(desc)
    curr.execute(sql_select_query, (str(desc),productname,))
    conn.commit()
    conn.close()
    print("productname____________________________"+productname)
    print("pushdb completed")

def generate(productname):
    text="""
    Product Description for "White and Gold Knives":
    Beautiful and functional, these cutlery sets are perfect for every kitchen. The knives are designed to have a beautiful look, but are also strong and durable. With a range of different colors, you can find the perfect set for your kitchen. The sets come with an assortment of kitchen knives, including a chef knife, bread knife, and carving knife. The sets also come with a sheath for safe storage. These knives are dishwasher safe.

    Product Description for "Paper Plates":
    Paper plates are often used for take-out or in situations where disposable plates are needed. Paper plates are durable and can be reused. They are environmentally friendly, as they can be recycled or composted. They are also lightweight and don't break easily. Paper plates are great for parties and family gatherings.

    Product Description for "Big Broom":
    The Big Broom is the perfect household item for anyone with a lot of floors to sweep. It's lightweight and durable, making it easy to sweep and maintain your floors. The handle is long enough to get under couches and other furniture, and the bristles are durable enough to clean deep down in cracks and crevices.

    Product Description for "Men's Wallet":
    Sleek and lightweight, this is the perfect wallet for the man on the go. With enough room for your ID, credit cards, and cash, this wallet is perfect for a night out on the town.

    Product Description for "Cleaning Towel":
    The place where you and your family can unwind and relax. But it can be difficult to keep up with the day-to-day cleaning. Keep your home looking fresh and clean with the Cleaning Towel. This is a towel that has been infused with the power of microfiber. This technology makes it possible for the towel to clean your home from top to bottom without any extra effort on your part. The towel can clean floors, countertops, windows, mirrors, and more. The towel is also durable and will last for years.

    Product Description for {}:
    """.format(productname)

    output = query({
                "inputs": text,
                "parameters": {"max_new_tokens": 100,
                            "min_length":100,
                            "return_full_text": False,
                            "repetition_penalty":0.00,


                            }
        })
    desc=(output[0]["generated_text"]).replace(text,"")
    pushdbupdate(desc,productname)

    return(desc)
