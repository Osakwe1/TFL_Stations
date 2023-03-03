# Transport for London Data Visualization 🚇
This repository contains an analysis of the Transport for London (TfL) station entry and exit data from 2007 to 2021. The goal of this project is to explore and visualize the data to gain insights into how people use the London Underground and other supporting TfL services.

The data used in this analysis was obtained from the TfL Open Data portal and data buckets, which provides access to a wide range of data about London's transportation system. The station entry and exit data is published on an annual basis and contains information about the number of entries and exits at each station, broken down by time of day and day of the week.

## Project Structure
The project is structured as follows:
* 📁 data: contains all the raw data files downloaded from the TfL Open Data portal.
* 📁 output: contains the final output files generated by the notebooks, such as CSV files, maps and images.
* 📁 tube maps: contains tube maps of the TfL network from as early as Dec 2013, showing the evolution of the network.

#### Notes
- In the *'data'* folder, I created a dataset of all stations on the TfL Network (including Tramlink stops) under the name *'Stations_20220221.csv'*. To the best of my knowledge, all data provided in this file is correct as of the 22nd of February, 2023. You are welcome to use this as you please for any projects you may have. 

## Getting Started
If you need help setting up your copy of the project, click the drop down below. If not, skip ahead.

<details>
<summary>So how do I set it up?</summary>
<br>
These instructions will get you a copy of the project up and running on your local machine for testing and development purposes.

First of all, this project makes use of all the following python libraries and packages:

### Built With
In working on this project, the following libraries were utilized.
- Python 🐍 - Programming language
- Pandas 🐼 - Data manipulation library
- Numpy 🔢 - Scientific maths library
- Geopandas 🗺️ - Geographical data manipulation library
- Matplotlib 📊 - Data visualization library
- Seaborn 🌊 - Data visualization library
- Plotly 📈 - Interactive data visualization library
- Folium 🍃 - Interactive map plotting library
- Shapely 🌍 - Geocoding library
- hvplot 📈 - Data visualization library

### Prerequisites
You will need to have Python 3 and the necessary libraries installed. You can install these libraries using pip by running the below :
```
pip install -r requirements.txt 
```
- Clone the project repository to your local machine.
- Open a command prompt or terminal window and navigate to the project directory.
- If you have VS Code or Jupyter Notebook, you can open up the folder by running:
```
code .  # for VS Code
```  
OR 
```
jupyter notebook  # for Jupyter Notebook
```  
If you do have either, I have linked the download link for [VS code](https://code.visualstudio.com/Download)   
</details>
Once in the file, you can run the notebook, review the analysis and make edits of your own.


## Data
The data used in this project is provided by TfL and can be found here. You will need to download the appropriate CSV files and place them in the data directory.

## Running the code
The code for the data visualization is in the Jupyter Notebook file *'TFL_Stations.ipynb'*. You can run the code by opening the notebook and running the cells.

<!--- ## Results
The results of our analysis show some interesting trends and patterns in the TfL station entry and exit data from 2007 to 2021. Some of the key findings include:

The total number of station entries and exits has steadily increased over time, with a peak in 2019 and a sharp decline in 2020 due to the COVID-19 pandemic.
Some stations are much busier than others, with the busiest stations being in central London and the quieter stations being in the suburbs.
The data shows clear patterns by time of day and day of the week, with peak usage during weekday rush hours and lower usage on weekends and holidays.
These results can be further explored and used to inform transportation planning and policy decisions.

## Conclusion
In conclusion, this project has demonstrated the power of data analysis and visualization in gaining insights into complex systems such as the London transportation network. By cleaning and exploring the TfL station entry and exit data from 2007 to 2021, we have been able to identify key patterns and trends that can be used to inform transportation planning and policy decisions. The Jupyter notebooks and code in this repository provide a foundation for further analysis and exploration of this rich dataset. --->




### Acknowledgement
All TfL transport data used in this project is provided by the [Transport for London open access](https://tfl.gov.uk/info-for/open-data-users/our-open-data). 
Statistical GIS Boundary Files used in this project are provided by the [Office of National Statistics](https://data.london.gov.uk/dataset/statistical-gis-boundary-files-london). All files and data has been used in accordance with the  Open Government Licence and UK Government Licensing Framework.

## Results & Charts
In the course of this project, several charts and indexes were produced to conduct analyses. Here I will provide a few samples of what you can find in this project:

- Here is a map of all the tube, rail and tram stations on the Transport for London Network. 
![gdf](https://user-images.githubusercontent.com/42135459/221436171-0b66359d-b70b-423f-8e7d-1ed50ebad781.png)

- Presented below is the Transport for London Entry & Exit figures over the years¹. 
![bokeh_plot](https://user-images.githubusercontent.com/42135459/221436610-26acb247-37ac-46fb-ba1b-49848bfcbf7c.png)

- Presented below is the Top 5 TfL stations by official Entry & Exit figures¹.
![newplot (5)](https://user-images.githubusercontent.com/42135459/221932470-0bab7270-06a2-4379-be09-67c3776332a8.png)

¹ - *Figures prior to 2017 **only** include the London Underground*

- Finally, here is the breakdown of Entry & Exit data on the TfL network since 2017.
![image](https://user-images.githubusercontent.com/42135459/222136679-28554ace-7bc4-4dc0-bf8f-c568365250ca.png)


<!--- TfL Station Entry and Exit Data Analysis
This repository contains an analysis of the Transport for London (TfL) station entry and exit data from 2007 to 2021. The goal of this project is to explore and visualize the data to gain insights into how people use the London Underground and other TfL services.

Results
The results of our analysis show some interesting trends and patterns in the TfL station entry and exit data from 2007 to 2021. Some of the key findings include:

The total number of station entries and exits has steadily increased over time, with a peak in 2019 and a sharp decline in 2020 due to the COVID-19 pandemic.
Some stations are much busier than others, with the busiest stations being in central London and the quieter stations being in the suburbs.
The data shows clear patterns by time of day and day of the week, with peak usage during weekday rush hours and lower usage on weekends and holidays.
These results can be further explored and used to inform transportation planning and policy decisions.

Conclusion
In conclusion, this project has demonstrated the power of data analysis and visualization in gaining insights into complex systems such as the London transportation network. By cleaning and exploring the TfL station entry and exit data from 2007 to 2021, we have been able to identify key patterns and trends that can be used to inform transportation planning and policy decisions. The Jupyter notebooks and code in this repository provide a foundation for further analysis and exploration of this rich dataset. --->
