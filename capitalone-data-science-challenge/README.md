# CapOne Data Science Challenge

### Computer Specs

Operating System: OS X

Computer: 2018 MacBook Pro (16G ram)

### Notebook Structure

The solutions to each question was positioned after the code that was used to find the answer. These answers can be found in a markdown cell.

Please see the HTML version of this notebook: capone-challenge-kotwani.html

### Thank You


Thank you for giving me the opportunity to complete this challenge. I have learned a lot by completing this assessment. I am aware there are many great scientists and engineers out there. I hope this work helps me build my case for why I can learn and adapt to new technologies and situations.

### Question 1: Load

Programmatically download and load into your favorite analytical tool the transactions data. This data, which is in line-delimited JSON format, can be found here
Please describe the structure of the data. Number of records and fields in each record?
Please provide some additional basic summary statistics for each field. Be sure to include a count of null, minimum, maximum, and unique values where appropriate.

### Question 2: Plot

Plot a histogram of the processed amounts of each transaction, the transactionAmount column.
Report any structure you find and any hypotheses you have about that structure.

### Question 3: Data Wrangling - Duplicate Transactions

You will notice a number of what look like duplicated transactions in the data set. One type of duplicated transaction is a reversed transaction, where a purchase is followed by a reversal. Another example is a multi-swipe, where a vendor accidentally charges a customer's card multiple times within a short time span.

Can you programmatically identify reversed and multi-swipe transactions?
What total number of transactions and total dollar amount do you estimate for the reversed transactions? For the multi-swipe transactions? (please consider the first transaction to be "normal" and exclude it from the number of transaction and dollar amount counts)
Did you find anything interesting about either kind of transaction?

### Question 4: Model

Fraud is a problem for any bank. Fraud can take many forms, whether it is someone stealing a single credit card, to large batches of stolen credit card numbers being used on the web, or even a mass compromise of credit card numbers stolen from a merchant via tools like credit card skimming devices.

Each of the transactions in the dataset has a field called isFraud. Please build a predictive model to determine whether a given transaction will be fraudulent or not. Use as much of the data as you like (or all of it).
Provide an estimate of performance using an appropriate sample, and show your work.
Please explain your methodology (modeling algorithm/method used and why, what features/data you found useful, what questions you have, and what you would do next with more time)


### Column Inspection

The dataframe was able to infer the following data types:

1. isFraud (boolean)
2. cardPresent (boolean)
3. expirationDateKeyInMatch (boolean) 
4. availableMoney (float)
5. creditLimit (float)
6. currentBalance (float)
7. transactionAmount (float)



There are a few columns labelled as objects. Further inspection is require to determine the data types for these columns. The following analysis is used to logically reduce the set of data types.

1. accountNumber (id)
2. accountOpenDate (date)
3. acqCountry (cat)
4. cardCVV (int) (id)
5. cardLast4Digits (int) (id)
6. currentExpDate (date)
7. customerId (id)
8. dateOfLastAddressChange (date)
9. echoBuffer (?)
10. enteredCVV (int) (id) **potentially a useful attribute
11. merchantCategoryCode (cat)
12. merchantCity (cat)
13. merchantCountryCode (cat)
14. merchantName (id) (cat)
15. merchantState (cat)
16. merchantZip (cat)
17. posConditionCode (cat)
18. posEntryMode (cat)
19. posOnPremises (?)
20. recurringAuthInd (bool?)
21. transactionDateTime (datetime)
22. transactionType (cat)

### Unique Value Counts

There appears to be a total of 5000 customers and 2490 merchant names in the dataset. There are 5246 unique last4digits in the datset which is more than the number of customers. 

Interestingly, there are fewer transaction datetimes than the number of records. What are the changes of that if the transactions are down to the second values?

### Transaction Amount

The structure of the transaction amount data element seems to follow a negative exponential distribution. The mean value is somewhere around $150 dollars. 

After further inspection and by using a logorithmic transformation it can be seen that there are a large number of transaction with a value of 0. These might be psuedo transactions which are not related to purchases. 

In the larger context of the problem, there could be an adverserial strategy that uses these transaction to determin the viability of fraud. A seperate indicator could be created for these cases. After removing the zero values from the plot, it can be seen that the distribution follows the exponential distribution more closely. 

In the context of building a model, taking the log transformation might be useful for building a predictive model. It minimizes the effect of outliers. A seperate feature could be create to indicate large or anomalous values.

If I has more time, I plot the various categorical variables for when the transaction value was zero. For example, a bar plot of tranaction type could be created for when this is condition.


### Duplicate Transactions

Duplicate transaction can be multi-swipe or reversals. Multi-swipe transaction are described as when the vendor accidently charges the same transaction more than once. Reversals are described as a purchases followed by a reversals. It will be assumed that in order for the transaction to be considered duplicate, the transactions need to occur within 0-10 seconds of each other. 


### Multiswipe Transactions

It is implied by the definition for multi-swipe transaction that the vendor accidently charges the credit credit card multiple times for the same transaction amount. There were only 5 transaction that met the multi-swipe conditions that did not have the same transaction value.

Multi-swipe algorithm 1:
1. fuzzy inner join on the dataset
2. customerID+merchantName are the same
3. the transactions happen between 0 and 10 seconds apart
4. the rowIds are different
5. the transaction amounts are the **same**
6. the second transaction is a purchase

Multi-swipe algorithm 2:
1. fuzzy inner join on the dataset
2. customerID+merchantName are the same
3. the transactions happen between 0 and 10 seconds apart
4. the rowIds are different
5. the transaction amounts are **different**
6. the second transaction is a purchase

Multi-swipe algorithm 1:
1. fuzzy inner join on the dataset
2. customerID+merchantName are the same
3. the transactions happen between 0 and 10 seconds apart
4. the rowIds are different
5. the transaction amounts are the **same**
6. the second transaction is a reversal

Multi-swipe algorithm 2:
1. fuzzy inner join on the dataset
2. customerID+merchantName are the same
3. the transactions happen between 0 and 10 seconds apart
4. the rowIds are different
5. the transaction amounts are **different**
6. the second transaction is a reversal

### Notes

A multi-swipe can be fraud for one or many of the transactions.

Transaction types labelled as ADDRESS VERIFICATION or REVERSALS will not be not considered multi-swipe transaction. 

There are many transactions that happen within 0 seconds of each other, but not all of these are from the same customer and merchant.

### Additional Considerations

While this algorithm finds and join duplicate transactions, it doesn't effectively deal with multiple transaction. With more time, I would implement run this algorithm multiple times to deal with multi-transactions not just duplicates. In addition, reversals can potentially happend outside of the 10 second window, finding whether these are still considered duplicates, i.e. same amounts, or whether it is part of some other business process.

### Results

1. There were 405 multi-swipe transactions with the same transaction amount that resulted in an total amount of 60.5K.

2. There were 59 multi-swipe transactions with different transaction amounts that resulted in an total amount of 10.7K.

3. There were 328 reversal transactions with the same transaction amount that resulted in an total amount of 46.9K.

4. There were 39 reversal transactions with different transaction amounts that resulted in an total amount of 2.5K.

It was found that that multiswipe 2 carried a much higher risk for fraud with an average fraud value of 6.9%. This is much higher than the dataset's value of 1.5% fraud. The other multi-swipe transactions also carried slightly more risk that non-multiswipe transactions. Could be possible that these transactions are happening online and programmatically?



### Data Exploration

It is unknown whether a sample of customers or transactions were collected. Creating a sequence of purchase patterns might not be applicable if the transactions were already sampled from another database. 

Various plots were used to determine the sampling methodology used in the dataset. A plot of fraud over by date showed that the number of fraud cases per day stays relatively close to 35 +- 10 cases.

A chart of transactions over time for a sample of 20 customers was also created. It showed a consistent transaction pattern with periodic breaks. This is possibly evidence that all transactions were collected within this 1 year time frame.

A percentile plot of total transaction and daily transaction across customers was also created. These plots showed that customers that had at least 1 case of fraud had a tendency to make more total transactions (in 1 year) and more daily transactions.

How were the customers chosen to be included in the dataset?


### Data Engineering

There are some constrains on the dataset and the objective. We only have a sample for 1 year of data. This data has already been down sampled and probably contain some bias. The objective of predicting fraud with 12417 cases will probably be enough to generalize risk, but outliers and anomalies might need to be removed to improve the model's performance.

How is the isFraud assigned? Knowing whether isFraud is available could make it viable as a feature. For example, are customer's with previous fraud more likely to have another case of fraud? Is a card number that has had prior fraud more likely to have another case of fraud? These featues were excluded due to the process being unknown.

**Feature engineering was split into two different types of features: 1) transactional features 2) customer features.**

1. Transactional features are in relation to the current transaction, i.e., is the card expired, how close was the entered CVV to the actual CVV, how many days between the transaction to an address change, etc.

2. Customer related features are in relation to an account, i.e., has customer used this company or particular merchant in the last 30 days, has this customer used this card in the last 30 days, what was the average transaction amount in the last 30 days, etc.

The only excluded feature was the customer's current balance, and it was excluded because the objective is to indentify fraud not credit risk. The effectiveness of this feature could be tested later.

### ML Pipeline

How the model will be used is unknown, i.e., decision support, automated flagging, research and development, etc. The model will predict whether a particular customer, card number, and transaction will be a fraud case. 

Ideally, the model will be used to automatically flag potential fraud cases. The cost of a false positive (predicting fraud when it is not) is much less than a false negative (not predicting fraud when it is). The model's effectiveness will be based on the model's ability to indentify most of the fraud cases. A custom metric was designed to choose the best model.

custom metric: **(true positives)/(false positives) where true positives>30 per day (average)**

The reasoning behind using this metric is that it shows which model effectively detects most fraud cases and segments the data from the most likely non-fraud cases. Additional models could be overlayed to this baseline model.

The goal of this modeling cycle was to develop a baseline model, determine the most important features, and theorize additional improvement that can be made.

Modeling pipeline:
1. Choose model type
2. Develop a search set of tuning hyperparameters
3. Use stratified K-fold to create 5 training and validation splits
4. Use smart downsampling on non-fraud cases
5. Optimize the model using log-loss
6. Define early stopping to be AUC on the validation
7. Compute model on custom metric
8. Save to leaderboard of models

A total of 4 cross-validated catboost models were assessed with various hyperparameters. The metrics were calcuated on the validation dataset for each model. After the stratified k-fold split, the data was downsampled to balance the positive and negative classes for training. This helps the model distinguish the objective of modeling fraud cases from labeling non-fraud cases.

The decision to use catboost was mostly due to its efficiency and easy of use. If I had more time, I would explore using neural network approaches (tensorflow) and utilize anomaly detection methods. Specifically, I would be interested in building a deep neural network to model/characterize the purchase patterns of the customer's in the dataset. This could potentially helpful as a semi-supervised approach to dig into individual cases. 

The best model was chosen based on the model's effectiveness at the probability threshold where most of the fraud cases were captured, i.e, 30 fraud cases per day.

If I had more time to work on this problem, additional hyper-parameter tuning and different models would be built. For example, at the bottom of this notebook, a one-hot encoding, perceptron network was built using tensorflow. In the interest of time, this model was not run.


### Results



The best model was saved as a binary file called: best_catboost_model

Average Metrics for Cross-Validation:
1. Average AUC for the best model on validation: 0.7905702202985669
2. Best TP/FP for 30 TP a day: 0.028578225849315055

The AUC metrics can be interpreted at the model performance above random. I chose the custom metric to determine the effeciency of the model where most of the fraud cases were capture. It turned out that the model with the best AUC also had the best custom metric.

**Note: the AUC metric was compute on the unbalanced validation set**

Operational Performance (calculated on all data):
1. Probability threshold  0.3943943943943944
2. Accuracy  0.604365922608261
3. 88% of the positives were captured
4. 60% of the negatives were excluded

The probability threshold was select for where 30 fraud cases were detected per day, where the average fraud cases per day is 35 +- 10 cases. If this model were to be put into production, it would incorrectly flag 40% of all transactions of fraud, but it would correctly flag 88% of fraud cases. 

The feature importance was ranked as follows:
0. merchantCategoryCodeLabelEncoded
1. transactionCount_30DY
2. transactionLogAmount
3. daysSinceAccountOpen
4. posEntryModeLabelEncoded
5. percentOfCreditUsed
6. avgLogTransactionAmount_30DY
7. daysSinceAddressChange
8. cardPresent
9. posConditionCodeLabelEncoded
10. transactionTypeLabelEncoded
11. minAbsHourDiff_30DY
12. previouscompanyNameOnly_30DY
13. previousMerchantName_30DY
14. previousMerchantCategory_30DY
15. editDistanceCVV
16. previousCardNumber_30DY
17. expirationDateKeyInMatch
18. sameCountryInd
19. multiSwipeType
20. zeroAmount

The top feature was the merchant category code which shows a potential bias in the data for a particular type of fraud. The best feature from the customer-aggregate features turned out to be the number of non-multiswipe transaction in the last 30days for a customer (ranked 2). A larger time window might have improved the effectiveness of the customer aggregate variables. Also, a linear model would have probably used these aggregate feature in a more effective fashion.

### What are the POS variables?

#### POS Entry Codes - his field contains a code identifying transaction conditions at the point-of-sale or point-of-service. For messages that follow an original request, this code identifies the type of processing being done. The following table lists POS condition codes:

1. 02 - Magnetic stripe read. For Plus transactions, this code also means that the exact Track 2 content is included and CVV checking is possible.
2. 05 - Integrated circuit card read; card data reliable.
3. 09 - PAN entry via electronic commerce, including chip.
4. 80 - Chip card was unable to process/magnetic stripe read default.
5. 90 - Magnetic stripe read and extract content of Track 1 or Track 2 included (CVV check is possible).

#### POS Condition Code - This two-digit code identifies the actual method used to enter the cardholder account number and card expiration date. This code specifies whether the entire magnetic stripe is included in an authorization request:

1. 00 - Normal transaction of this type
2. 01 - Cardholder not present
3. 02 - Unattended terminal, customer operated (for example, an Automated Dispensing Machine)
4. 08 - Mail/telephone order (includes Visa phone and reoccurring transactions)