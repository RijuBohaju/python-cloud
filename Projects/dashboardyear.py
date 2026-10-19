import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go

def load_data(fl):
    if fl is not None:
        filename = fl.name
        st.write("Uploaded file name:", filename)
        if filename.endswith('.csv'):
            df = pd.read_csv(fl, encoding="ISO-8859-1")
        elif filename.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(fl, engine='openpyxl')
        else:
            st.error("Invalid file format. Please upload a CSV or Excel file.")
            return None
    else:
        st.warning("No file uploaded. Loading default CSV file.")
        os.chdir(r"C:\Users\RIJU\Desktop\python")  # Replace with your default file path
        df = pd.read_csv("gdp.csv", encoding="ISO-8859-1")
    return df

def main(df):
    st.title("CSV/XLSX File Uploader and Interactive Line Chart")

    fl = st.file_uploader(":file_folder: Upload a file", type=["csv", "txt", "xlsx", "xls"])

    df = load_data(fl)

    if df is not None:
        st.subheader("Data Preview")
        st.dataframe(df)

        # Print DataFrame columns to check the actual column names
        st.write("DataFrame Columns:", df.columns)

        # Create a multiselect widget to select multiple countries, including "All" option
        countries_selected = st.multiselect("Select countries to compare:", ["All"] + df["Country Name"].unique().tolist())

        if not countries_selected:
            st.warning("Please select at least one country.")
        else:
            if "All" in countries_selected:
                # Calculate total GDP for each country
                gdp_data = df.groupby("Country Name")["Value"].sum().reset_index()

                # Display total GDP for all countries
                st.subheader("Total GDP for All Countries")
                st.dataframe(gdp_data)

                # Display interactive Plotly line chart for all countries' GDP visualization
                fig = go.Figure()

                for country in gdp_data["Country Name"]:
                    country_data = df[df["Country Name"] == country]
                    fig.add_trace(go.Scatter(x=country_data["Year"], y=country_data["Value"], mode="lines+markers", name=country))

                fig.update_layout(title="GDP Over Time - All Countries", xaxis_title="Year", yaxis_title="GDP")
                st.plotly_chart(fig)

            else:
                # Filter DataFrame based on the selected countries
                filtered_df = df[df["Country Name"].isin(countries_selected)]

                # Calculate total GDP for each selected country
                gdp_data = filtered_df.groupby("Country Name")["Value"].sum().reset_index()

                # Display total GDP for the selected countries
                st.subheader("Total GDP for Selected Countries")
                st.dataframe(gdp_data)

                # Display interactive Plotly line chart for the selected countries' GDP visualization
                fig = go.Figure()

                for country in countries_selected:
                    country_data = filtered_df[filtered_df["Country Name"] == country]
                    fig.add_trace(go.Scatter(x=country_data["Year"], y=country_data["Value"], mode="lines+markers", name=country))

                fig.update_layout(title="GDP Over Time - Selected Countries", xaxis_title="Year", yaxis_title="GDP")
                st.plotly_chart(fig)


if __name__ == "__main__":
    df = None  # Initialize the df variable
    main(df)
