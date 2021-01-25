# surfs_up
SQLite, Jupyter Notebook, SQLAlchemy

# Overview of the analysis
The purpose of the analysis is to provide W. Avy weather information about the weather trends in Oahu. This information will be used to make investment and feasibility decisions regarding the opening of the surf shop. 

The routes created in the app.py file enables investors to view the various weather data using a local host. This will help investors view the data they need. 

Lastly, this repository includes a comparison of June and December temperatures. 

# Results

June and December temperature results are as follows:

![June Results](https://github.com/patrickryanpo/surfs_up/blob/main/Resources/June%20Desc.png)


![Dec Results](https://github.com/patrickryanpo/surfs_up/blob/main/Resources/Dec%20Desc.png)

- The difference of the June and December average temperatures are not that far apart. June reported a mean of 75 degrees, while December reported a mean of 71 degrees. 

- The difference in the minimum temperatures are more pronounced but no significant. June's minimum temperature was recorded at 64 degrees, and December's minimum temperature was recorded at 56 degrees. 

- When it comes to the maximum temperature, there was also insignificant different. June's maximum temperature was recorded at 85 degrees, and December's maximum temperature was recorded at 83 degrees. 

Both results data was queried from the hawaii.sqlite file available in this repository. The rows of June and December were gathered by using the SQLAlchemy query method, wherein, specific months were extracted. 

# Summary

Based on the results, it can be said that the weather in Oahu is fairly static during the months of June and December. Although December posted a maximum temp of 83, it was only one time that this occured. 

![Dec Max loc]()

## Additional Query: Precipitations
![June Precip]()

![Dec Precip]()

Based on the findings, precipitation will not be a factor in both June and December. W. Avy should not feel concerned about constant rain affecting the Surfshop. 