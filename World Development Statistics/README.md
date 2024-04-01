# World Development Statistics - An Analysis of the Human Development Index

The Human Development Index (HDI) is a summary measure of average achievement in key dimensions of human development: a long and healthy life, being knowledgeable and having a decent standard of living [1]. 
From this definition, we can see that the HDI is a summary measure of achievement in three dimensions: life expectancy, education, and income. The purpose of this project is to analyze the life expectancy and Gross National Income (GNI) per capita of countries in the world to determine if they contribute to a high HDI.

# Data Dictionary
|Feature|Type|Dataset|Description|
|---|---|---|---|
|[1800-2050]|float|gni_per_cap_atlas_method_con2021.csv|Gross National Income (GNI) by Country for the years 1800-2050
|country|object|gni_per_cap_atlas_method_con2021.csv|Country present as row level information of GNI dataset

|Feature|Type|Dataset|Description|
|---|---|---|---|
|[1800-2100]|float|life_expectancy.csv|Life Expectency (LE) by Country for the years 1800-2100
|country|object|life_expectancy.csv|Country present as row level information of LNI dataset

|Feature|Type|Dataset|Description|
|---|---|---|---|
|[1990-2021]|float|hdi_human_development_index.csv|Human Development Index (HDI) by Country for the years 1990-2021
|country|object|hdi_human_development_index.csv|Country present as row level information of HDI dataset

|Feature|Type|Dataset|Description|
|---|---|---|---|
|[1990-2021]_le|float|life_expectancy.csv|Life Expectency (LE) by Country for the years 1990-2021
|[1990-2021]_gni|float|gni_per_cap_atlas_method_con2021.csv|Gross National Income (GNI) per capita by Country for the years 1990-2021
|[1990-2021]_hdi|float|hdi_human_development_index.csv|Human Developement Index (HDI) by Country for the years 1990-2021
|country|object|hdi_human_development_index.csv, gni_per_cap_atlas_method_con2021.csv, life_expectancy.csv|Country present as row level information of HDI, LE and GNI datasets

# Executive Summary

The project aims to analyze the relationship between life expectancy, Gross National Income (GNI) per capita, and the Human Development Index (HDI) of countries in the world.
The datasets used were not identical in shape and availability of values so some transformations were performed. Each dataset was reduced to date ranges between 1990 and 2021 to ensure comparability. 
In preparation for the analysis, the datasets were merged to ensure consistency and completeness of the data. The resulting dataset contains information on the associated countries from 1990 to 2021.

Initially, a number of summary statistics were obtained to understand the distribution of the variables, namely the mean and median of the GNI, LE and HDI within each year. 
To obtain country specifc GNI, LE and HDI, a transposed dataset was used that offered a more intuitive way to view the data. The top and bottom 5 countries in terms of average GNI, LE and HDI, as well as the range of the respective metrics, were identified. 

Further analysis was conducted to understand the relationship between the three variables. A correlation matrix was created to visualize the strength of the relationships. The results indicated a positive correlation between GNI and HDI, as well as a positive correlation between LE and HDI. To further explore these relationships, a scatter plot was created, which allowed for the examination of some pairwise relationships between all three variables. A boxplot was also used to determine if the data had outliers while the use of the histogram allowed for an understanding of the skewness of the data.

In conclusion, the project was able to confirm the positive relationship between GNI and HDI, as well as between LE and HDI. It was also able to identify the countries that had interesting metrics, such as the top and bottom 5 countries in terms of average GNI, LE and HDI, as well as the range of the respective metrics.

Next steps - To further support the analysis, introducing other relevant datasets can provide a better understanding of the factors affecting HDI.

# Citations
[1] - https://hdr.undp.org/data-center/human-development-index#:~:text=The%20Human%20Development%20Index%20HDI,a%20decent%20standard%20of%20living

[2] - https://chat.openai.com/

[3] - Miladinov, G. Socioeconomic development and life expectancy relationship: evidence from the EU accession candidate countries. Genus 76, 2 (2020). https://doi.org/10.1186/s41118-019-0071-0

[4] - https://fredblog.stlouisfed.org/2020/06/national-incomes-connection-to-life-expectancy/