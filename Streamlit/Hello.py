import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import geopandas as gpd
import folium
# from streamlit_folium import st_folium
from shapely.geometry import Point
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Set page title
st.set_page_config(page_title='TfL Cooling Project',
                   layout="wide",
                   page_icon=":bullettrain_side:",
                   menu_items={
    'Report a bug': "mailto:OOsakwe1@icloud.com?subject=Bug%20found%20in%20website",
    'About': "# Built by Olisa Osakwe."
    })


# Loading in TFL Station Exit & Entry Spreadsheet for 2007 to 2016
file_name='data/TFL Station Counts/Annual_Counts/multi-year-station-entry-and-exit-figures.xlsx'

sheet07='2007 Entry & Exit'
df2007 = pd.read_excel(io=file_name, sheet_name=sheet07, skiprows=6).drop(columns=[
                                                                        'Weekday',
                                                                        'Saturday',
                                                                        'Sunday',
                                                                        'Weekday.1',
                                                                        'Saturday.1',
                                                                        'Sunday.1'])
sheet08='2008 Entry & Exit'
df2008 = pd.read_excel(io=file_name, sheet_name=sheet08, skiprows=6).drop(columns=[
                                                                        'Weekday',
                                                                        'Saturday',
                                                                        'Sunday',
                                                                        'Weekday.1',
                                                                        'Saturday.1',
                                                                        'Sunday.1'])

sheet09='2009 Entry & Exit'
df2009 = pd.read_excel(io=file_name, sheet_name=sheet09, skiprows=6).drop(columns=[
                                                                        'Weekday',
                                                                        'Saturday',
                                                                        'Sunday',
                                                                        'Weekday.1',
                                                                        'Saturday.1',
                                                                        'Sunday.1'])

sheet10='2010 Entry & Exit'
df2010 = pd.read_excel(io=file_name, sheet_name=sheet10, skiprows=6).drop(columns=[
                                                                        'Weekday',
                                                                        'Saturday',
                                                                        'Sunday',
                                                                        'Weekday.1',
                                                                        'Saturday.1',
                                                                        'Sunday.1'])

sheet11='2011 Entry & Exit'
df2011 = pd.read_excel(io=file_name, sheet_name=sheet11, skiprows=6).drop(columns=[
                                                                        'Weekday',
                                                                        'Saturday',
                                                                        'Sunday',
                                                                        'Weekday.1',
                                                                        'Saturday.1',
                                                                        'Sunday.1'])

sheet12='2012 Entry & Exit'
df2012 = pd.read_excel(io=file_name, sheet_name=sheet12, skiprows=6).drop(columns=[
                                                                        'Weekday',
                                                                        'Saturday',
                                                                        'Sunday',
                                                                        'Weekday.1',
                                                                        'Saturday.1',
                                                                        'Sunday.1'])

sheet13='2013 Entry & Exit'
df2013 = pd.read_excel(io=file_name, sheet_name=sheet13, skiprows=6).drop(columns=[
                                                                        'Weekday',
                                                                        'Saturday',
                                                                        'Sunday',
                                                                        'Weekday.1',
                                                                        'Saturday.1',
                                                                        'Sunday.1'])
sheet14='2014 Entry & Exit'
df2014 = pd.read_excel(io=file_name, sheet_name=sheet14, skiprows=6).drop(columns=[
                                                                        'Weekday',
                                                                        'Saturday',
                                                                        'Sunday',
                                                                        'Weekday.1',
                                                                        'Saturday.1',
                                                                        'Sunday.1'])

sheet15='2015 Entry & Exit'
df2015 = pd.read_excel(io=file_name, sheet_name=sheet15, skiprows=6).drop(columns=[
                                                                        'Weekday',
                                                                        'Saturday',
                                                                        'Sunday',
                                                                        'Weekday.1',
                                                                        'Saturday.1',
                                                                        'Sunday.1'])
sheet16='2016 Entry & Exit'
df2016 = pd.read_excel(io=file_name, sheet_name=sheet16, skiprows=6).drop(columns=[
                                                                        'Weekday',
                                                                        'Saturday',
                                                                        'Sunday',
                                                                        'Weekday.1',
                                                                        'Saturday.1',
                                                                        'Sunday.1'])

# Loading in TFL Station Exit & Entry Spreadsheet for 2017 to 2021
file_name2017 =  'http://crowding.data.tfl.gov.uk/Annual%20Station%20Counts/2017/AnnualisedEntryExit_2017.xlsx'
file_name2018 =  'http://crowding.data.tfl.gov.uk/Annual%20Station%20Counts/2018/AnnualisedEntryExit_2018.xlsx'
file_name2019 =  'http://crowding.data.tfl.gov.uk/Annual%20Station%20Counts/2019/AnnualisedEntryExit_2019.xlsx'
file_name2020 =  'http://crowding.data.tfl.gov.uk/Annual%20Station%20Counts/2020/AC2020_AnnualisedEntryExit.xlsx'
file_name2021 =  'http://crowding.data.tfl.gov.uk/Annual%20Station%20Counts/2021/AC2021_AnnualisedEntryExit.xlsx'
sheet =  'Annualised'

# Some Rows are skipped and irrelevant columns are dropped to standardize the DataFrame
df2017 = pd.read_excel(io=file_name2017, sheet_name=sheet, skiprows=6)
df2018 = pd.read_excel(io=file_name2018, sheet_name=sheet, skiprows=6)
df2019 = pd.read_excel(io=file_name2019, sheet_name=sheet, skiprows=6)
df2020 = pd.read_excel(io=file_name2020, sheet_name=sheet, skiprows=6)
df2021 = pd.read_excel(io=file_name2020, sheet_name=sheet, skiprows=6)

# Formatting dfs to be consistent
df2017=df2017.drop(columns=['entries',
                            'entries.1',
                            'entries.2',
                            'Unnamed: 7',
                            'exits',
                            'exits.1',
                            'exits.2',
                            'Unnamed: 11']).round()
df2018=df2018.drop(columns=['entries',
                            'entries.1',
                            'entries.2',
                            'entries.3',
                            'exits',
                            'exits.1',
                            'exits.2',
                            'exits.3']).round()
df2019=df2019.drop(columns=['entries',
                            'entries.1',
                            'entries.2',
                            'entries.3',
                            'exits',
                            'exits.1',
                            'exits.2',
                            'exits.3']).round()
df2020=df2020.drop(columns=['Entries',
                            'Entries.1',
                            'Entries.2',
                            'Entries.3',
                            'Exits',
                            'Exits.1',
                            'Exits.2',
                            'Exits.3']).round()
df2021=df2021.drop(columns=['Entries',
                            'Entries.1',
                            'Entries.2',
                            'Entries.3',
                            'Exits',
                            'Exits.1',
                            'Exits.2',
                            'Exits.3']).round()

# Creating dfs with only London Underground data
df2017LU=df2017[df2017['Mode']=='LU']
df2018LU=df2018[df2018['Mode']=='LU']
df2019LU=df2019[df2019['Mode']=='LU']
df2020LU=df2020[df2020['Mode']=='LU']
df2021LU=df2021[df2021['Mode']=='LU']

# Grouping dfs
df_grouped2007=df2007.groupby(['nlc', 'Station'], as_index=False).sum(numeric_only=True)
df_grouped2007['million']=df_grouped2007['million']*1_000_000
df_grouped2007.rename(columns={"nlc": "NLC",
                               "million": "En/Ex 2007"}, inplace=True)

df_grouped2008=df2008.groupby(['nlc', 'Station'], as_index=False).sum(numeric_only=True)
df_grouped2008['million']=df_grouped2008['million']*1_000_000
df_grouped2008.rename(columns={"nlc": "NLC",
                               "million": "En/Ex 2008"}, inplace=True)

df_grouped2009=df2009.groupby(['nlc', 'Station'], as_index=False).sum(numeric_only=True)
df_grouped2009['million']=df_grouped2009['million']*1_000_000
df_grouped2009.rename(columns={"nlc": "NLC",
                               "million": "En/Ex 2009"}, inplace=True)

df_grouped2010=df2010.groupby(['nlc', 'Station'], as_index=False).sum(numeric_only=True)
df_grouped2010['million']=df_grouped2010['million']*1_000_000
df_grouped2010.rename(columns={"nlc": "NLC",
                               "million": "En/Ex 2010"}, inplace=True)

df_grouped2011=df2011.groupby(['nlc', 'Station'], as_index=False).sum(numeric_only=True)
df_grouped2011['million']=df_grouped2011['million']*1_000_000
df_grouped2011.rename(columns={"nlc": "NLC",
                               "million": "En/Ex 2011"}, inplace=True)

df_grouped2012=df2012.groupby(['nlc', 'Station'], as_index=False).sum(numeric_only=True)
df_grouped2012['million']=df_grouped2012['million']*1_000_000
df_grouped2012.rename(columns={"nlc": "NLC",
                               "million": "En/Ex 2012"}, inplace=True)

df_grouped2013=df2013.groupby(['nlc', 'Station'], as_index=False).sum(numeric_only=True)
df_grouped2013['million']=df_grouped2013['million']*1_000_000
df_grouped2013.rename(columns={"nlc": "NLC",
                               "million": "En/Ex 2013"}, inplace=True)

df_grouped2014=df2014.groupby(['nlc', 'Station'], as_index=False).sum(numeric_only=True)
df_grouped2014['million']=df_grouped2014['million']*1_000_000
df_grouped2014.rename(columns={"nlc": "NLC",
                               "million": "En/Ex 2014"}, inplace=True)

df_grouped2015=df2015.groupby(['nlc', 'Station'], as_index=False).sum(numeric_only=True)
df_grouped2015['million']=df_grouped2015['million']*1_000_000
df_grouped2015.rename(columns={"nlc": "NLC",
                               "million": "En/Ex 2015"}, inplace=True)

df_grouped2016=df2016.groupby(['nlc', 'Station'], as_index=False).sum(numeric_only=True)
df_grouped2016['million']=df_grouped2016['million']*1_000_000
df_grouped2016.rename(columns={"nlc": "NLC",
                               "million": "En/Ex 2016"}, inplace=True)

df_grouped2017LU=df2017LU.groupby(['NLC', 'Station'], as_index=False).sum('en/ex')
df_grouped2017LU.rename(columns={"en/ex": "En/Ex 2017"}, inplace=True)
df_grouped2017=df2017.groupby(['NLC', 'Station'], as_index=False).sum('en/ex')
df_grouped2017.rename(columns={"en/ex": "En/Ex 2017"}, inplace=True)

df_grouped2018LU=df2018LU.groupby(['NLC', 'Station'], as_index=False).sum('en/ex')
df_grouped2018LU.rename(columns={"en/ex": "En/Ex 2018"}, inplace=True)

df_grouped2018=df2018.groupby(['NLC','Station'], as_index=False).sum('en/ex')
df_grouped2018.rename(columns={"en/ex": "En/Ex 2018"}, inplace=True)

df_grouped2019LU=df2019LU.groupby(['NLC','Station'], as_index=False).sum('en/ex')
df_grouped2019LU.rename(columns={"en/ex": "En/Ex 2019"}, inplace=True)
df_grouped2019=df2019.groupby(['NLC','Station'], as_index=False).sum('en/ex')
df_grouped2019.rename(columns={"en/ex": "En/Ex 2019"}, inplace=True)

df_grouped2020LU=df2020LU.groupby(['NLC','Station'], as_index=False).sum('En/Ex')
df_grouped2020LU.rename(columns={"En/Ex": "En/Ex 2020"}, inplace=True)
df_grouped2020=df2020.groupby(['NLC','Station'], as_index=False).sum('En/Ex')
df_grouped2020.rename(columns={"En/Ex": "En/Ex 2020"}, inplace=True)

df_grouped2021LU=df2021LU.groupby(['NLC','Station'], as_index=False).sum('En/Ex')
df_grouped2021LU.rename(columns={"En/Ex": "En/Ex 2021"}, inplace=True)
df_grouped2021=df2021.groupby(['NLC','Station'], as_index=False).sum('En/Ex')
df_grouped2021.rename(columns={"En/Ex": "En/Ex 2021"}, inplace=True)

# Merging all the Datasets prior to 2017
pt1 = pd.merge(
        pd.merge(
            pd.merge(
                pd.merge(
                    pd.merge(
                        pd.merge(
                            pd.merge(
                                pd.merge(
                                    pd.merge(df_grouped2007,
                                             df_grouped2008.drop(columns=['Station']),
                                             on='NLC',
                                             how='outer'),
                                    df_grouped2009.drop(columns=['Station']),
                                    on='NLC',
                                    how='outer'),
                                df_grouped2010.drop(columns=['Station']),
                                on='NLC',
                                how='outer'),
                            df_grouped2011.drop(columns=['Station']),
                            on='NLC',
                            how='outer'),
                        df_grouped2012,
                        on='NLC',
                        how='outer'),
                    df_grouped2013.drop(columns=['Station']),
                    on='NLC',
                    how='outer'),
                df_grouped2014.drop(columns=['Station']),
                on='NLC',
                how='outer'),
            df_grouped2015.drop(columns=['Station']),
            on='NLC',
            how='outer'),
        df_grouped2016.drop(columns=['Station']),
        on='NLC',
        how='outer')

# Merging all the Datasets post-2017.
pt2=pd.merge(
    pd.merge(
        pd.merge(
            pd.merge(df_grouped2017.drop(columns=['Station']),
                     df_grouped2018.drop(columns=['Station']),
                     on='NLC',
                     how='outer'),
            df_grouped2019.drop(columns=['Station']),
            on='NLC',
            how='outer'),
        df_grouped2020.drop(columns=['Station']),
        on='NLC',
        how='outer'),
    df_grouped2021, # NLC is dropped in all other DFs to avoid duplicate columns
    on='NLC',
    how='outer')

# Merging all the Datasets.
pt3=pd.merge(
    pd.merge(
        pd.merge(
            pd.merge(df_grouped2017LU.drop(columns=['Station']),
                     df_grouped2018LU.drop(columns=['Station']),
                     on='NLC',
                     how='outer'),
            df_grouped2019LU.drop(columns=['Station']),
            on='NLC',
            how='outer'),
        df_grouped2020LU.drop(columns=['Station']),
        on='NLC',
        how='outer'),
    df_grouped2021LU, # NLC is dropped in all other DFs to avoid duplicate columns
    on='NLC',
    how='outer')

# Merging the two merged DFs - All of TfL
df_merged=pd.merge(pt1,
                   pt2,
                   on='NLC',
                   how='outer')

# Merging the two merged DFs - Only London Underground
df_mergedLU=pd.merge(pt1,
                     pt3,
                     on='NLC',
                     how='outer')



df_merged = df_merged[['Station_x'] + [x for x in df_merged.columns if x != 'Station_x']]
df_merged = df_merged[['Station_y'] + [x for x in df_merged.columns if x != 'Station_y']]
df_merged = df_merged[['Station'] + [x for x in df_merged.columns if x != 'Station']]
df_merged = df_merged[['NLC'] + [x for x in df_merged.columns if x != 'NLC']]
# st.write("Column Names:", df_merged.columns)
df_merged.rename(columns={'Station_x': 'Station 2007',
                            'Station_y': 'Station 2012',
                            'Station': 'Station 2021'}, inplace=True, errors='raise')
df_merged['Station 2007'] = df_merged['Station 2007'].str.strip()
df_merged['Station 2012'] = df_merged['Station 2012'].str.strip()
df_merged.at[142,'Station 2021'] = 'New Cross'
df_merged.at[143,'Station 2021'] = 'New Cross Gate'
df_merged.at[178,'Station 2021'] = 'Rotherhithe'
df_merged.at[188,'Station 2021'] = 'Shadwell'
df_merged.at[190,'Station 2021'] = 'Shoreditch'
df_merged.at[211,'Station 2021'] = 'Surrey Quays'
df_merged.at[232,'Station 2021'] = 'Wapping'
df_merged.drop(columns=['Station 2007', 'Station 2012'], inplace=True)
df_merged.rename(columns={"Station 2021": "Station"}, inplace=True)

df_mergedLU = df_mergedLU[['Station_x'] + [x for x in df_mergedLU.columns if x != 'Station_x']]
df_mergedLU = df_mergedLU[['Station_y'] + [x for x in df_mergedLU.columns if x != 'Station_y']]
df_mergedLU = df_mergedLU[['Station'] + [x for x in df_mergedLU.columns if x != 'Station']]
df_mergedLU = df_mergedLU[['NLC'] + [x for x in df_mergedLU.columns if x != 'NLC']]
# st.write("Column Names:", df_mergedLU.columns)
df_mergedLU.rename(columns={'Station_x': 'Station 2007',
                            'Station_y': 'Station 2012',
                            'Station': 'Station 2021'}, inplace=True, errors='raise')
df_mergedLU['Station 2007'] = df_mergedLU['Station 2007'].str.strip()
df_mergedLU['Station 2012'] = df_mergedLU['Station 2012'].str.strip()
df_mergedLU=df_mergedLU.drop(columns=['Station 2007', 'Station 2021'])
df_mergedLU.at[142,'Station 2012'] = 'New Cross'
df_mergedLU.at[143,'Station 2012'] = 'New Cross Gate'
df_mergedLU.at[178,'Station 2012'] = 'Rotherhithe'
df_mergedLU.at[188,'Station 2012'] = 'Shadwell'
df_mergedLU.at[190,'Station 2012'] = 'Shoreditch'
df_mergedLU.at[211,'Station 2012'] = 'Surrey Quays'
df_mergedLU.at[232,'Station 2012'] = 'Wapping'
df_mergedLU.at[275,'Station 2012'] = 'Nine Elms'
df_mergedLU.at[276,'Station 2012'] = 'Battersea Power Station'
df_mergedLU=df_mergedLU.rename(columns={"Station 2012": "Station"})

# Importing in the lines file to give further information on each station
df_lines = pd.read_csv('data/Geodata/Stations_20220221.csv').drop(columns=['EASTING','NORTHING','Zone','x','y'])

# Merging to form full df - All of TfL
df_stations=pd.merge(df_merged,
                     df_lines,
                     on='NLC',
                     how='left' # Left merge since not all the stations in df_lines are in our df_merged dataset
                    ).drop(columns='NAME')
# df_stations

# Merging to form full df - All of London Underground
df_stationsLU=pd.merge(df_mergedLU,
                       df_lines,
                       on='NLC',
                       how='left' # Left merge since not all the stations in df_lines are in our df_merged dataset
                      ).drop(columns='NAME')

df_stations.to_csv("output/Streamlit_stations.csv") # Saves our dataframe to the output folder

st.divider() # Divider

# Sorting df to use commuter figures instead of NLC
df_stationsLU.sort_values(by='En/Ex 2017', ascending=False, inplace=True)
# Creating plot of all the busiest Underground stations in London since 2007
fig = go.Figure()

    # Add traces for top 50 stations
for station in df_stationsLU['Station'].head(50):
    x = df_stationsLU.loc[df_stationsLU['Station'] == station, [f'En/Ex {year}' for year in range(2017, 2020)]].values[0]
    fig.add_trace(go.Scatter(x=list(range(2017, 2020)), y=x, mode='lines+markers', name=station))

    # Set layout
fig.update_layout(
    title={
        'text': "Top 50 London Underground Stations by Entry/Exit (2007-2021)",
        'x': 0.5,  # Center the title
        'y': 0.93,  # Set the y position of the title
        'xanchor': 'center',  # Center the title horizontally
        'yanchor': 'top'  # Anchor the title to the top of the figure
    },
    xaxis_title='Year',
    yaxis_title='Entry/Exit',
    yaxis_type='log',  # Set the y-axis scale to logarithmic
    height=1100,
    width=1000,
    plot_bgcolor='whitesmoke'
    )
st.plotly_chart(fig)

st.divider() # Divider

# Sample data
data = {
    "Year": ["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"],
    "Entries_Exits": [df_stations["En/Ex 2007"].sum(), df_stations["En/Ex 2008"].sum(), df_stations["En/Ex 2009"].sum(),
                      df_stations["En/Ex 2010"].sum(), df_stations["En/Ex 2011"].sum(), df_stations["En/Ex 2012"].sum(),
                      df_stations["En/Ex 2013"].sum(), df_stations["En/Ex 2014"].sum(), df_stations["En/Ex 2015"].sum(),
                      df_stations["En/Ex 2016"].sum(), df_stations["En/Ex 2017"].sum(), df_stations["En/Ex 2018"].sum(),
                      df_stations["En/Ex 2019"].sum(), df_stations["En/Ex 2020"].sum(), df_stations["En/Ex 2021"].sum()]
}
df = pd.DataFrame(data)
# Streamlit app
st.title('Transport for London Entry & Exit figures over the years')

fig = px.bar(df, x='Year', y='Entries_Exits', title='Transport for London Entry & Exit figures over the years',
             labels={'Entries_Exits': 'Figures (in Billions)'})
fig.update_layout(xaxis={'title': 'Period'}, yaxis={'title': 'Figures (in Billions)'}, xaxis_tickangle=-45)
fig.update_layout(width=800, height=400)

st.plotly_chart(fig)
