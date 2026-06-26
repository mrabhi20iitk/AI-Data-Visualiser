#sql_generator.py

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import json

import os



from database.schema import get_schema


schema_text = get_schema()


from llm.llm import llm






prompt = ChatPromptTemplate.from_template("""
You are an expert MySQL SQL generator.
Target database: MySQL 8.
Generate SQL compatible with ONLY_FULL_GROUP_BY mode.
When selecting values from a derived table, CROSS JOIN, or scalar subquery in an aggregate query, wrap those values in an aggregate function such as MAX() or MIN() unless they are included in the GROUP BY clause.

Prefer window functions instead of CROSS JOIN total subqueries whenever possible.

Database Schema:
{schema}

Question:
{question}

Rules:
- Generate only SQL
- Use MySQL syntax
- Do not explain
Also return:
- chart_type
                                          
                                          
- x_axis columns
- y_axis column
- title
                                          
chart_type must be exactly one of:ß
["bar", "line", "pie", "scatter", "table"]

Do not return any other value.   

Return JSON in the following example format:

{{
  "sql": "...",
  "chart_type": "line",
  "x_axis": "category",
  "y_axis": "revenue",
  "title": "Revenue by Category",                                                                    
}}

x_axis , y_axis must be a string, not an array. 
                                          
""").partial(schema=schema_text)

chain = prompt | llm | StrOutputParser()


def test(input_text):
    return chain.invoke({"question":input_text})

def llm_response(input_text):
   
    response =  chain.invoke({"question":input_text})
    response = json.loads(response)

    return response




    



