#  Analysis of TfL Station Entry and Exit Data (2007-2021) 🚇
This repository contains an analysis of the Transport for London (TfL) station entry and exit data from 2007 to 2021. The goal of this project is to explore and visualize the data to gain insights into how people use the London Underground and other supporting TfL services.

The data used in this analysis was obtained from the TfL Open Data portal and data buckets, which provides access to a wide range of data about London's transportation system. The station entry and exit data is published on an annual basis and contains information about the number of entries and exits at each station, broken down by time of day and day of the week.

## Project Structure
The project is structured as follows:
* 📁 [data](https://github.com/Osakwe1/TFL_Stations/tree/master/data): contains all the raw data files downloaded from the TfL Open Data portal.
* 📁 [output](https://github.com/Osakwe1/TFL_Stations/tree/master/output): contains the final output files generated by the notebooks, such as CSV files, maps and images.
* 📁 [tube_maps](https://github.com/Osakwe1/TFL_Stations/tree/master/tube_maps): contains tube maps of the TfL network from as early as Dec 2013, showing the evolution of the network.

#### Notes
- In the *['data'](https://github.com/Osakwe1/TFL_Stations/tree/master/data)*  folder, I created a dataset of all stations on the TfL Network (including Tramlink stops) under the name *'Stations_20220221.csv'*. To the best of my knowledge, all data provided in this file is correct as of the 22nd of February, 2023. You are welcome to use this as you please for any projects you may have. 

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

  
* Clone the project repository to your local machine.
To set up your own local copy of this project, you will need to 'clone' this repo. To create a clone, run this in your terminal 
```
gh repo clone Osakwe1/TFL_Stations
```  
 
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

### Acknowledgement
All TfL transport data used in this project is provided by the [Transport for London open access](https://tfl.gov.uk/info-for/open-data-users/our-open-data). 
Statistical GIS Boundary Files used in this project are provided by the [Office of National Statistics](https://data.london.gov.uk/dataset/statistical-gis-boundary-files-london). All files and data has been used in accordance with the  Open Government Licence and UK Government Licensing Framework.

## Results & Charts
In the course of this project, several charts and indexes were produced to conduct analyses. Here I will provide a few samples of what you can find in this project:

- Here is a map of all the tube, rail and tram stations on the Transport for London Network. 
![gdf](https://user-images.githubusercontent.com/42135459/221436171-0b66359d-b70b-423f-8e7d-1ed50ebad781.png)

- Presented below is the Transport for London Entry & Exit figures over the years¹. 
![bokeh_plot](https://user-images.githubusercontent.com/42135459/221436610-26acb247-37ac-46fb-ba1b-49848bfcbf7c.png)

- Presented below is the Annual Top 10 TfL stations by official Entry & Exit figures¹.
![newplot (6)](https://user-images.githubusercontent.com/42135459/222843170-0cc63450-6187-4eba-bac0-0cafde1fc839.png)

¹ - *Figures prior to 2017 **only** include the London Underground*

- Finally, here is the breakdown of Entry & Exit data on the TfL network since 2017.
![image](https://user-images.githubusercontent.com/42135459/222136679-28554ace-7bc4-4dc0-bf8f-c568365250ca.png)

## Conclusion
In conclusion, this Transport for London Data Visualization project has provided us with valuable insights into the usage patterns of London's Underground and other supporting TfL services. By exploring and analyzing the station entry and exit data from 2007 to 2021, we were able to identify the busiest stations, peak travel times, and trends in passenger behavior over the years. The project has also produced several informative charts and maps, which have made it easier to visualize and understand the data.

I hope that this project has been both informative and enjoyable for anyone who has had the chance to explore it. As the data is updated annually, there is always an opportunity to update the analysis and uncover new insights about how people travel in and around London.

### Further Suggestions
Due to limitations I had with available data and available time, I was not able to explore all facets of this project. These are a list of ideas I believe would be interesting and insightful and may be future extensions of this project. 
If you're looking to take this project further, here are some suggestions:

- Use machine learning algorithms to predict future usage patterns of the TfL network, which could help TfL optimize their services and improve the passenger experience.
- Visualize the data in new and creative ways, such as through interactive 3D models of Entry/Exit data, to provide a more engaging view of the busiest areas of London.
- Conduct a sentiment analysis of social media posts related to TfL and public transportation in London, to gain insights into what people are saying about the services and identify areas for improvement.
- Explore interchange data in the ['NUMBAT'](https://github.com/Osakwe1/TFL_Stations/tree/master/data/NUMBAT) files to see which interchanges are the most frequented and explore potential future interchange possibities to make journeys faster and more accessible.
- and maybe try to explain what is going on with Poplar and West India Quay's DLR stations? (Please, I would love to hear any explanations)

I hope that you enjoyed this project and it inspires you to dig deeper into the world of data visualization and analysis! Thank you!


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
