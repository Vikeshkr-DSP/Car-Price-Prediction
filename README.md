# Car Price Prediction
## Introduction
As the name suggest, this project is all about predicting the price of a used car depending upon the current price (in show rooms), how many kilometres it has been drived, whether the transmissin is manual or automatic, etc. The web abb created for this will be useful for a seller as well as for the buyer. If anyone ever wanted to shale their car, it will be useful to get an idea of what should be the correct price of the car for reshale. Similarly any buyer can predit the price of a car depending upon the features of that car. 

## DataSource
The app has been made after training few machine learning algorithms to understand how the price of a car varied depending upon features like Transmissin type, Fuel type, etc. Data used for training the algorithm has been collected from cardekho.com which was shared publically on Kaggle. Data consist of 9 feature including resale value. Features which affects the resale value (independent variable) are Car_Name, Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission and Owner. Variable which needs to be predicted (dependent variable) is Selling_Price. These features can be seen as below.
![image](https://user-images.githubusercontent.com/66907101/123917876-e67eda80-d9a0-11eb-86e4-e453fd1c6fdc.png)

## Model Training
From all the features listed, Car_Name doesn't affects the reshale value of any car and thus is not used for price prediction. Some features like Fuel_Type, Transmission, etc are categorical variables and need to be encoded before being used by any algorith for training. All categorical features has been encoded using pandas One-Hot Encoding technique. Also, Year of purchase has been subtracted from current year which tells how old the car is.  After label encoding, data can be seen as:
![image](https://user-images.githubusercontent.com/66907101/123920856-05cb3700-d9a4-11eb-966c-df10dea1bcc0.png)

Three algorithms used for model training are RandomForest, XGBoost and Linear Regression.
### Random Forest
Random Forest has been trained first using default parameters and gives MSE (Mean Squared Error) score of 0.6982 on validation data. Then Random Forest has been Hyperparameter Tuned. After HPT (Hyperparameter Tuning), Random Forest gives an MSE score of 1.0891 on validation data using cross-validation on 5 folds.

### XGBoost
Firstly, XGBoost was trained on its default parameters and gives MSE (Mean Squared Error) score of 0.7340 on test data which is more than Random Forest. Then I went for HPT (Hyperparameter Tuning) and got an MSE score of 1.0165 on validation data with 10 fold cross validation which is better than MSE score of Random Forest.

### Linear Regression
As we know that Linear Regression is a distance based algorithm and all the features used for training the algorithm needs to scaled, all the features were scaled using Normalizer as none of the features follows Gaussian Distribution. After Rescaling, Linear Regression was trained with its default parameters and got MSE (Mean Squared Error) score of 11.7250 on validation data ans MSE score of 12.0859 on training data. From the MSE score, we can say that model was underfitting and thus using l1 and l2 parameters (used to avoid overfitting) will be of no use.

From RandomForest, XGBoost and Linear Regression, XGBoost gives best MSE (Mean Squared Error) score after HPT (Hyperparameter Tuning) and thus is used for creating the web app.

## Web app
Web app is created using Flask and is deployed on Heroku. The app can be accessed on link https://car-price-prediction-try.herokuapp.com/. The app will ask you to provide the value of features as described above as : ![image](https://user-images.githubusercontent.com/66907101/123926499-8f313800-d9a9-11eb-8397-e033d427a2af.png)
Here, you need to fill all the columns as : ![image](https://user-images.githubusercontent.com/66907101/123927189-37470100-d9aa-11eb-941d-355ca364caba.png)
After providing all the deatails, you need to click on 'Submit for Prediction' and the app will predict the reshale value of that car depending upon the parameter value you have provided. ![image](https://user-images.githubusercontent.com/66907101/123927615-a45a9680-d9aa-11eb-90dc-37fad77136ed.png)
Now you have got the reshale value of a car with specific feature. You can again fill the columns and predit the reshale value of tha car.

## Technology Used
* Jupyter Notebook (Python 3.8)
* Spyder (creating app.py)
* VS Code (creating Front end web page)
* Heroku and Github (for deployment)
