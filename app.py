import streamlit as st
from model import load_rules, get_ai_response, check_response_against_rules, request_modified_response, add_rule

# Load rules from the JSON file
rules_data = load_rules()

# Function to handle user queries
def user_query(prompt):
    response = get_ai_response(prompt)
    is_valid, missing_rule = check_response_against_rules(response, rules_data)
    if not is_valid:
        response = request_modified_response(prompt, missing_rule)
        # Re-check the modified response
        is_valid, missing_rule = check_response_against_rules(response, rules_data)
        if not is_valid:
            response += f"\nNote: Further refinement needed to comply with the rule: {missing_rule}"
    return response

# Streamlit UI for users
st.title("Ethical AI Interaction Monitor")
st.header("User Interface")

user_input = st.text_area("Enter your query here:", "")
if st.button("Get AI Response"):
    response = user_query(user_input)
    st.write("AI Response:")
    st.write(response)

# Streamlit UI for trainers
st.header("Trainer Interface")
category = st.text_input("Category (e.g., financial, law, medical)")
query_keywords = st.text_input("Query Keywords (comma-separated)")
rules_list = st.text_area("Rules (separated by semicolon ';')")

if st.button("Add Rule"):
    query_keywords_list = [kw.strip() for kw in query_keywords.split(',')]
    new_rules = [rule.strip() for rule in rules_list.split(';')]
    add_rule(category, query_keywords_list, new_rules, rules_data)
    st.success(f"New rules added under category '{category}'.")
