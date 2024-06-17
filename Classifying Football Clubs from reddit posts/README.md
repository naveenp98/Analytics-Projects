# Project 3 - Reddit

## Introduction

Reddit is a social news aggregation, web content rating, and discussion website. Users submit content to subreddits, which are groups of users with similar interests. The website consists of 1000s of subreddits, each with thousands of active users.

## Problem Statement
The purpose of this project is to differentiate 2 similar subreddits using NLP.

The chosen subreddits are - 
1. LiverpoolFC (Liverpool Football Club subreddit)
2. reddevils (Manchester United Football Club subreddit)

## Background
Liverpool and Manchester United are two of the most popular football clubs in the world. Both clubs have a large fan base and are known for their passionate fans. The LiverpoolFC subreddit is a community where fans discuss the team, its players, and the latest news. The reddevils subreddit is a community where fans discuss the team, its players, and the latest news.

The two clubs are eternal rivals that possess the same objective, to win as much silverware as possible. The two fan bases are hostile towards one another, always hoping for the other team to falter whilst rooting for their own to succeed. Due to this intense rivalry, it is not uncommon to have fans talk about each other's teams and players.

## Data
The data for this project is collected from the Reddit API. The API provides access to a wide range of data. The data captured includes titles, self_texts and source of subreddit. The data pulled is from the 'new' category, which is the most recent posts.

The final dataset consists of the following - 

|Feature|Type|Dataset|Description|
|---|---|---|---|
|title|string|LiverpoolFC, reddevils|The title of the post
|self_text|string|LiverpoolFC, reddevils|The self text of the post
|subreddit|string|LiverpoolFC, reddevils|The target variable. The subreddit from which the post is from
|title_count|int|LiverpoolFC, reddevils|The number of characters in the title of the post
|self_text_count|int|LiverpoolFC, reddevils|The number of characters in the self_text of the post
|title_word_count|int|LiverpoolFC, reddevils|The number of words in the title of the post
|self_text_word_count|int|LiverpoolFC, reddevils|The number of words in the self_text of the post

## Executive Summary

Using the PRAW module, essential information of the Liverpool and Manchester United subreddits is collected from the Reddit API. The character and word counts are generated using helper functions. A number of visualizations are created to understand the data. 

To get the data into a usable format, a TFIDF vectorizer is used to generate frequencies of occuring words from the title and self_text, with english stop words handled. Then the entire dataset is scaled using a standard scaler.

The data is then split into training and test sets. The training set is used to train the models, and the test set is used to evaluate the models.

The two models developed are Logitic Regression and Random Forest Classifier models. The accuracy of both models are measured and the following is the result - 
The Logistic Regression model generated an accuracy of 84.7% on test data.
The Random Forest Classifier model generated an accuracy of 90.6% on test data.

## Conclusion 

The two models are able to differentiate between the two subreddits. The Logistic Regression model is less accurate than the Random Forest Classifier model.

## Future Work

The model can be improved by adding more features to the dataset.
The model can be improved by using a more advanced NLP model.
