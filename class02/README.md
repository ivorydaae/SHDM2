# Class02
[Class02 Slides](https://docs.google.com/presentation/d/1EBtm9mgS6r-DPs7ZQ3HBbXT3vNkh98pUI1njgxQIHYQ/edit#slide=id.g7294067f54_0_0)

## First Hands On: discovering basic and advanced capabilities of a data science platform

The second session will be dedicated to the core features of Dataiku DSS. The students will be guided through a typical Data Science use case and will import the data, clean them, enrich them and build their first predictive model with the software. We will insist on core concepts of Data Science along with various features and technologies used in companies.  

**Our Use case**: Titanic  
This use case is probably one of the most famous use case in machine learning (it would not be suprising if you are familiar with it already!). Our goal will be to predict whether a person in the Titanic will survive.  
To build a predictive model, we will work a `train` dataset, with known data and a `test` dataset with unknown data. Once prepared & enriched, we will train some models on our train dataset and score our unknown data.  
The data we will work with include socio-demographic information, tickets information and some other interesting features! 

## Content
Working on the famous `Titanic` use case, we will discover core functionalities of Dataiku DSS along with the visual machine learning part.
- Importing datasets in Dataiku
- Understanding our data
- Working with visual recipes to clean and enrich our data
- Building our first predictive model with the DSS visual machine learning & Analyse results
- Export relevant visualisations to a dashboard

### Importing datasets in Dataiku
Dataiku integrates with various databases and connectors to answer our client needs. Out of curiosity, you can [check all the connectors](https://doc.dataiku.com/dss/latest/connecting/connections.html) we integrate with as of today.  

In this first hands on (and all the following), we will look for our files in the server with the `filesystem` connector. All datasets are available on [this repository](../datasets) and you will also be able, on your own to upload your files directly if you want!  

### Understanding our data 
Here, we will work with core features of DSS in the explore view of our datasets.  
We will also build our first visualisations and publish them to a dashboard!  

### Working with visual recipes
Visual recipes in Dataiku are powerful. They allow coders and non coders to process their data easily, in an intuitive way. Beyond that, they allow a vast amount of operations and we will use some of them, from the **stack** recipe to the **prepare** and **split** recipe. We wil have a look at other recipes in the next lessons.  

In the **prepare** recipe, we will clean our data and do some feature engineering (adding information that could be relevant for our model).  
Cleaning and feature engineering will include:  
- Harmonization of some socio-demo data (`title` might be to accurate? how to deal with some missing values?)
- Counting family members
- ... and some other steps, with recommendations or your own imagination!

### Building our predictive model

After preparing and spltting our data, we will train some models and pick up the best one.  
- How to make sure our data is ready to be trained?
- Which criteria to choose to pick up the best model? 
- How to interpret our results? 
We will answer these questions hopefully! And deploy the model afterwards.  

### Export results to a dashboard

Finally, we will export our results to a dshboardd. Remember to always think of the ed user who will aalyse our results!  
With some Dataiku features, we will make these results as insightful as possible.  

## Resource & external links
- [Titanic on Kaggle](https://www.kaggle.com/c/titanic)
- [Basic Dataiku tutorial to go further](https://www.dataiku.com/learn/portals/tutorials/)


