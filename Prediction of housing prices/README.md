Housing Price Prediction - Iterative Machine Learning Process

This project demonstrates a complete Data Science workflow focused on predicting real estate prices using the Ames Housing Dataset. The primary goal was to showcase how data engineering, feature selection, and model optimization impact prediction accuracy.


Project Evolution & Results SummaryThe project was not a single attempt but a conscious, iterative process of improving results from a baseline error of ~$40,000 down to ~$21,000.


|.......Stage........|..........Features Count..........|.......Model.......|...Scaling...|Mean Absolute Error (MAE)|
|....................|..................................|...................|.............|.........................|
|.Baseline...........|.2 (Area, Rooms)..................|Linear Regression..|...Linear....|.........$40,013.........|
|.Improved Features..|.4 (Added Quality, Year)..........|Random Forest......|...Linear....|.........$23,748.........|
|.Logarithmic Shift..|.8 (Added Location, Garage, etc.).|Linear Regression..|.Logarithmic.|.........$22,003.........|
|.Final Optimized....|.11 (Added Lot, Bath, Ext.).......|Random Forest......|.Logarithmic.|.........$21,048.........|


The Process

1. Initial Approach (The "Fatal" Start)The project began with a basic Linear Regression model using only two features: living area and number of rooms. The error was massive ($40k+), proving that "Garbage In, Garbage Out" is the most important rule in ML.

2. Feature Engineering & SelectionRealizing that real estate value is complex, I systematically expanded the feature set:
  Stage 1: Added OverallQual and YearBuilt. Quality became the most important predictor.
  Stage 2: Introduced categorical data like Neighborhood and KitchenQual using Label Encoding.
  Final Stage: Added LotArea (Land size), FullBath, and ExterQual (Exterior Quality) to capture the physical appeal of the property.

3. Transition to Logarithmic ScalingOne of the most critical turning points was switching the target variable (SalePrice) to a logarithmic scale (np.log1p).
  Why? Housing prices are often skewed. A $10,000 difference on a $100k house is huge, but on a $1M house, it's negligible.
  Effect: Log-scaling allowed the models to learn percentage relationships rather than fixed dollar amounts, significantly "straightening" the data for the algorithms.

4. Comparing Linear Models vs. Ensembles (Forest)I deliberately compared a single Linear Regression against a Random Forest (500 trees) to observe the gain from complexity:
  - On improved data, Linear Regression achieved $22,003.
  - On the same data, Random Forest pushed this further to $21,048.

Conclusion: Once the data is well-prepared and log-scaled, even simple models perform remarkably well, but ensembles capture the final "nonlinear" nuances.


Visualizing Success

The final prediction vs. actual price chart shows a strong linear correlation, with most predictions clustering tightly around the ideal red line.


Key Conclusions & Insights

  - Data > Algorithm: Improving the quality and quantity of features had a much larger impact on the error than simply switching from a single line to 500 trees.
  - Domain Knowledge Matters: Adding features like OverallQual (subjective quality) and Neighborhood (location) was more effective than just increasing mathematical complexity.
  - Logarithmic Scaling is Essential: For financial data with high variance, log-transformation is the key to preventing the model from being distracted by "outlier" luxury properties.
  - The Diminishing Returns Point: After reaching an error of ~$21k with 11 features, the model hit a "plateau." Further improvement would require deep data cleaning or advanced boosting techniques like XGBoost.
