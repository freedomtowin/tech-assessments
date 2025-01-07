# Lead Data Engineer Case Study

Rohan Kotwani  
0//23/2023

# Problem Statement

The Commodities USA publication has metrics including the Key Commodities figure. A data pipeline should extract the information in this figure across different years of the publication. The position, (x, y), of this figure on a page can vary slightly, i.e., (x \+/- 10%, y \+/- 10%). The page number of this figure can also vary. The information of this figure is in unstructured text, in a table.

# Success Metrics

The stakeholders of this extracted data are those that use downstream financial models. They have previously extracted these metrics manually. This implies that they are “used to” a high accuracy rate of the information they receive and use. A potential data extraction algorithm  should have a comparable accuracy rate and should be able to alert for when the extraction process produces uncertain results. The accuracy of the extraction should be 100% of the different test cases of the historical documents. 

# Algorithm

It was stated that the documents are in unstructured text, i.e., PDFs, Word docs, plain text, etc. A document reader would first need to be created, and would need to parse each document type into a standardized format. For example, tables should have the same format regardless of the document type.

**Note:** The text format might need to handle UTF-8 or special characters, as shown by the colored circles above. These might need to be addressed/extracted in the loading process.

An empty  data structure could be created for the expected format of the “Key Commodities” figure to hold the extracted data. For example, the commodity “coal” might have “market size” and “stability” as metrics. 

If there are expected commodities to be in each table, these should be added as a validation metric and an output metric of this process. The range and types  of potential values for certain metrics could also be validated for each commodity. The validation metric  would be used to determine the accuracy of the extraction process.

**Note:** OCR might be a good option for reading tables in PDF if there is a reliable OCR algorithm available. The validation metric could be the same as the process above.

The packages in a variety of programming languages can accomplish this task, i.e., Python, Golang, etc. After document loading, an algorithm can produce tables in a standardized format with REGEX or even a combination of REGEX and a Large Language Model (LLM). LLMs are capable of producing structured text, JSON data which could be used for validation. Then, the algorithm could find then extract out the correct table, i.e., the Key Commodities table. This includes searching for the table across the document’s pages. 

**Note:** A page-number range could be used to limit processing, however, it is not required. 

A validation step could be used to see if the process should re-run the extraction process with another table. While LLMs can be reliable with an appropriate prompt, the “temperature” hyper parameter  might cause the LLM to produce incorrect results from time to time, i.e., malformatted JSON.

**Note:** I am assuming that I can use the \`transformer\` library in python.

# Deployment

The frequency of this extract process seems to be yearly. To minimize cost, a batch job could be used to extract the information. To ensure transparency, a containerized process with version control could be created to run either locally or in the cloud. In the cloud, tools like AWS Step Functions and a Dockerized Lambda/Fargate could be used to begin the extraction process. Other orchestration tools like AirFlow could also be used depending on if a similar extraction process will need to be used in the future. 

Note: This is assuming that the extraction process will extract data from historical documents, then potentially run in the future.

# Algorithm Success

The success of the algorithm depends on 1\) the accuracy of the extracted data on the historical data 2\) the effectiveness of the algorithm running on new documents with cases it hasn’t “seen”, i.e., different page numbers, varying locations of tables, potentially different commodities, etc. The overall success for this algorithm is determined by whether the extracted data provides the correct validated data format or facilitates the manual extraction process for when the algorithm fails.

Note: the validation output above primarily focuses on extracting the table structure/metrics correctly. The accuracy of the model is the comparison of the manually extracted output and the algorithmic extracted data. New anticipated test cases can also be created for checking the accuracy.

