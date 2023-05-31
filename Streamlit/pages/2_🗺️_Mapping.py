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

st.divider() # Divider

tube_lines = {
    "Bakerloo":             {"id":"B", "colour":"#B36305", "network":"Tube"},
    "Central":              {"id":"C", "colour":"#E32017", "network":"Tube"},
    "Circle":               {"id":"I", "colour":"#FFD300", "network":"Tube"},
    "Elizabeth line":       {"id":"X", "colour":"#7156A5", "network":"Rail"},
    "DLR":                  {"id":"L", "colour":"#00A4A7", "network":"Rail"},
    "District":             {"id":"D", "colour":"#00782A", "network":"Tube"},
    "Hammersmith & City":   {"id":"H", "colour":"#F3A9BB", "network":"Tube"},
    "Jubilee":              {"id":"J", "colour":"#A0A5A9", "network":"Tube"},
    "Metropolitan":         {"id":"M", "colour":"#9B0056", "network":"Tube"},
    "Northern":             {"id":"N", "colour":"#000000", "network":"Tube"},
    "London Overground":    {"id":"O", "colour":"#EE7C0E", "network":"Rail"},
    "Piccadilly":           {"id":"P", "colour":"#003688", "network":"Tube"},
    "Tramlink":             {"id":"T", "colour":"#84B817", "network":"Tramlink"},
    "Victoria":             {"id":"V", "colour":"#0098D4", "network":"Tube"},
    "Waterloo & City":      {"id":"W", "colour":"#95CDBA", "network":"Tube"}
} # The Tube lines and their corresponding colour scheme and network.

# Define the style function for
def style_function(feature):
    line_id = feature["properties"]["id"]
    line_colour = tube_lines[line_id]["colour"]
    return {
        "color": line_colour,
        "weight": 4,
        "opacity": 0.8,
    }

ldn_df = gpd.read_file("data/Geodata/statistical-gis-boundaries-london/ESRI/London_Borough_Excluding_MHW.shp")
ldn_df.sample(3)

df1 = pd.read_csv('data/Geodata/Stations_20220221.csv')
df1 = df1.drop(df1[df1.LINES == 'Tramlink'].index)
df1.drop(columns=['NETWORK',
                  'LINES',
                  'London Underground',
                  'Elizabeth Line',
                  'London Overground',
                  'DLR'], inplace=True)
df1.sample(4)

df1["Coordinates"] = list(zip(df1.EASTING, df1.NORTHING))
df1["Coordinates"] = df1["Coordinates"].apply(Point)
gdf = gpd.GeoDataFrame(df1, geometry="Coordinates")

url = (
    "https://raw.githubusercontent.com/Osakwe1/vis/master/tubecreature/data"
)
tfl_network = f"{url}/tfl_lines.json"
london_ug = f"{url}/lu_lines.geojson"
nighttube = f"{url}/night_tube.geojson"


from streamlit_folium import st_folium

# Create the GeoJson layer with the style function
m = folium.Map(location=[51.55, 0.2], tiles="Stamen Terrain", zoom_start=10)

tfl_layer = folium.GeoJson(
    tfl_network,
    name="Tfl map",
    style_function=style_function
)
tube_layer = folium.GeoJson(
    london_ug,
    name="Tube map",
    style_function=style_function
)
# Add the layer to the map
tfl_layer.add_to(m)
# nighttube.add_to(map)

# Create a legend using the tube_lines dictionary
legend_html = """
<div style="position: fixed;
     bottom: 50px;
     left: 50px;
     width: 160px;
     height: 500px;
     border: 2px solid grey; z-index:9999; font-size:14px;
     background-color:white;
     ">
     &nbsp; TfL Lines <br>
"""
for i,row in gdf.iterrows():
    #Setup the content of the popup
    iframe = folium.IFrame(str(row["NAME"] + ' St.'))

    #Initialise the popup using the iframe
    popup = folium.Popup(iframe, min_width= 100, max_width=200)
    #Add each row to the map
    folium.Marker(location=[row['y'],row['x']],
                  popup = popup).add_to(m)

folium.GeoJson(tfl_network, name="Tube map", style_function=style_function).add_to(m)

folium.LayerControl().add_to(m)

for line_name, line_info in tube_lines.items():
    legend_html += f"""
     &nbsp; <span style="color:{line_info['colour']};
                  font-size: 20px;">&#9679;</span>
                  {line_name} <br>
    """

legend_html += "</div>"

m.get_root().html.add_child(folium.Element(legend_html))

st_data = st_folium(m, width=2000, height=500)
