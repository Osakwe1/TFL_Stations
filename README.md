# Transport for London Data Visualization 🚇
This repository contains an analysis of the Transport for London (TfL) station entry and exit data from 2007 to 2021. The goal of this project is to explore and visualize the data to gain insights into how people use the London Underground and other supporting TfL services.

The data used in this analysis was obtained from the TfL Open Data portal and data buckets, which provides access to a wide range of data about London's transportation system. The station entry and exit data is published on an annual basis and contains information about the number of entries and exits at each station, broken down by time of day and day of the week.

Project Structure
The project is structured as follows:

* 📁 data: contains all the raw data files downloaded from the TfL Open Data portal.
* 📁 output: contains the final output files generated by the notebooks, such as CSV files, maps and images.
* 📁 tube maps: contains tube maps of the TfL network from as early as Dec 2013, showing the evolution of the network.

Data Cleaning
The raw data from the TfL Open Data portal was in a format that required some cleaning and preprocessing before it could be analyzed. This involved converting date and time fields to a more usable format, filling in missing values, and aggregating the data to a daily and monthly level. The data cleaning and preprocessing steps are detailed in the Jupyter notebooks in the notebooks directory.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Built With
In working on this project, the following libraries were utilized.
- Python - Programming language
- Pandas - Data manipulation library
- Numpy - Scientific maths library
- Geopandas - Geographical data manipulation library
- Matplotlib - Data visualization library
- Seaborn - Data visualization library
- Plotly - Interactive data visualization library
- Folium - Interactive map plotting library
- Shapely - Geographical data manipulation library
- hvplot - Data visualization library

## Prerequisites
You will need to have Python 3 and the necessary libraries installed. You can install these libraries using pip by running the below :

```
pip install -r requirements.txt 
```

## Data
The data used in this project is provided by TfL and can be found here. You will need to download the appropriate CSV files and place them in the data directory.

## Running the code
The code for the data visualization is in the Jupyter Notebook file *'TFL_Stations.ipynb'*. You can run the code by opening the notebook and running the cells.

## Results
The results of our analysis show some interesting trends and patterns in the TfL station entry and exit data from 2007 to 2021. Some of the key findings include:

The total number of station entries and exits has steadily increased over time, with a peak in 2019 and a sharp decline in 2020 due to the COVID-19 pandemic.
Some stations are much busier than others, with the busiest stations being in central London and the quieter stations being in the suburbs.
The data shows clear patterns by time of day and day of the week, with peak usage during weekday rush hours and lower usage on weekends and holidays.
These results can be further explored and used to inform transportation planning and policy decisions.

## Conclusion
In conclusion, this project has demonstrated the power of data analysis and visualization in gaining insights into complex systems such as the London transportation network. By cleaning and exploring the TfL station entry and exit data from 2007 to 2021, we have been able to identify key patterns and trends that can be used to inform transportation planning and policy decisions. The Jupyter notebooks and code in this repository provide a foundation for further analysis and exploration of this rich dataset.

### Acknowledgement
All TfL transport data used in this project is provided by the [Transport for London open access](https://tfl.gov.uk/info-for/open-data-users/our-open-data). 
Statistical GIS Boundary Files used in this project are provided by the [Office of National Statistics](https://data.london.gov.uk/dataset/statistical-gis-boundary-files-london). All files and data has been used in accordance with the  Open Government Licence and UK Government Licensing Framework.



<!--- TfL Station Entry and Exit Data Analysis
This repository contains an analysis of the Transport for London (TfL) station entry and exit data from 2007 to 2021. The goal of this project is to explore and visualize the data to gain insights into how people use the London Underground and other TfL services.

Data Source
The data used in this analysis was obtained from the TfL Open Data portal, which provides access to a wide range of data about London's transportation system. The station entry and exit data is published on a monthly basis and contains information about the number of entries and exits at each station, broken down by time of day and day of the week.

Project Structure
The project is structured as follows:

Data Cleaning
The raw data from the TfL Open Data portal was in a format that required some cleaning and preprocessing before it could be analyzed. This involved converting date and time fields to a more usable format, filling in missing values, and aggregating the data to a daily and monthly level. The data cleaning and preprocessing steps are detailed in the Jupyter notebooks in the notebooks directory.

Data Exploration
Once the data was cleaned and preprocessed, we performed some exploratory data analysis to understand the patterns and trends in the data. We created various visualizations using Python libraries such as Pandas, Matplotlib, and Seaborn to help us understand how station entry and exit patterns changed over time, how different stations compared to each other, and how the data varied by time of day and day of the week. The data exploration and visualization steps are also detailed in the Jupyter notebooks in the notebooks directory.

Results
The results of our analysis show some interesting trends and patterns in the TfL station entry and exit data from 2007 to 2021. Some of the key findings include:

The total number of station entries and exits has steadily increased over time, with a peak in 2019 and a sharp decline in 2020 due to the COVID-19 pandemic.
Some stations are much busier than others, with the busiest stations being in central London and the quieter stations being in the suburbs.
The data shows clear patterns by time of day and day of the week, with peak usage during weekday rush hours and lower usage on weekends and holidays.
These results can be further explored and used to inform transportation planning and policy decisions.

Conclusion
In conclusion, this project has demonstrated the power of data analysis and visualization in gaining insights into complex systems such as the London transportation network. By cleaning and exploring the TfL station entry and exit data from 2007 to 2021, we have been able to identify key patterns and trends that can be used to inform transportation planning and policy decisions. The Jupyter notebooks and code in this repository provide a foundation for further analysis and exploration of this rich dataset. --->
