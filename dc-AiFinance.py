#from apiKey import apikey
#from apiKey import serpapi
import streamlit as st
import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from PIL import Image



st.set_page_config(
    page_title="Finance News",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "Demo Page by AdCreativeDEv"
    }
)
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


image = Image.open("stock.png")
st.image(image, caption='created by MJ')

st.title("Finance News ")

system_openai_api_key = os.environ.get('OPENAI_API_KEY')
system_openai_api_key = st.text_input(":key: OpenAI Key :", value=system_openai_api_key)
os.environ["OPENAI_API_KEY"] = system_openai_api_key

system_serpapi_api_key = os.environ.get('SERPAPI_API_KEY')
system_serpapi_api_key ="2412a22f7b5670afb53a687e0432d84cad408de0ee6bfc11db9c76be08ffec71"
system_serpapi_api_key = st.text_input(":key: SERPAPI Key :", value=system_serpapi_api_key)
os.environ["SERPAPI_API_KEY"] = system_serpapi_api_key



llm = OpenAI(temperature=0)

# tool to interact the world 
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# https://js.langchain.com/docs/modules/agents/agents/
# The agent you choose depends on the type of task you want to perform
# If you're using a text LLM, first try zero-shot-react-description
agent = initialize_agent(tools,
                         llm,
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                         verbose=True)


query1 = "TSLA and compare price performance between may 2023 and june 2023"
query2 = "Analyze apple stock and craft investment recommendations"
query3 = "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?"
query4 = "how many females have stayed more than 3 years? "
query5 = "how many females from city category A purchase product_Category_1 ?"
query6 = "What is the total number of Product Category_1 purchased by female from city category B whose age is 0-17 ?"

Qstr1 = "TSLA background and price performance"
Qstr2 = "Analyze apple stock"
Qstr3 = "Who is Leo DiCaprio's girlfriend?"
Qstr4 = "Leo DiCaprio's girlfriend?"
Qstr5 = "Purchase by gender, city and product"
Qstr6 = "Purchase by gender, city and age group"
Qstr7 = ""


finalQuery = "Select Query Type"
queryselection =st.radio ("Step 1 : Select some Promot : ",
                            (Qstr1, Qstr2, Qstr3))

# default choice
finalQuery = query1

if queryselection == Qstr1:
    finalQuery = query1

if queryselection == Qstr2:
    finalQuery = query2

if queryselection == Qstr3:
    finalQuery = query3

if queryselection == Qstr4:
    finalQuery = query4

if queryselection == Qstr5:
    finalQuery = query5
    

finalQuerySubmit = st.text_input('Step 2 : You can amend it : ', finalQuery)
st.write('Final Prompt Submit to Agnet : ', finalQuerySubmit)


if st.button("Submit"):
    result=agent.run(finalQuerySubmit)
    st.success(result )



log = """

> Entering new AgentExecutor chain...
I need to compare the stock price of TSLA between two dates
Action: Search

Action Input: "TSLA stock price may 2023 june 2023"
Observation: No good search result found

Thought: I should try a different search query
Action: Search

Action Input: "TSLA stock price performance may 2023 june 2023"

Observation: Based on analyst stock evaluations for TSLA over the last three months, the average price forecast for the next year is $205.11; the target ...

Thought: I now know the final answer

Final Answer: Based on analyst stock evaluations for TSLA over the last three months, the average price forecast for the next year is $205.11.

> Finished chain.
"""


with st.expander("explanation"):
    st.code(log)