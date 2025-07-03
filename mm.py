import streamlit as st


st.title("🔌 Metadata Viewer ")

account = st.sidebar.text_input("Account")
user = st.sidebar.text_input("User")
password = st.sidebar.text_input("Password", type="password")
warehouse = st.sidebar.text_input("Warehouse")
database = st.sidebar.text_input("Database")
schema = st.sidebar.text_input("Schema")

if st.sidebar.button("Fetch Metadata"):
    try:
        df = get_metadata_from_snowflake(account, user, password, warehouse, database, schema)
        st.success("Metadata retrieved successfully!")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error: {e}")

