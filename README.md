
# Comparison-for-Text-Classification-pre-trained-models-through-Topsis

## Overview
Text Classification is the task of assigning a label or class to a given text. Some use cases are sentiment analysis, natural language inference, and assessing grammatical correctness.

## Key Elements:

1. **Methodology:**
   - The Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method is employed for the comparison. This method considers both the similarity to the ideal solution and the dissimilarity to the negative ideal solution, providing a comprehensive ranking.
     
2. **Metrics included:**
   - The comparison is based on metrics including Precision, Recall, F1-Score and AUC Score.

3. **Models Evaluated:**
   - Models such as ann_without_stemming, simple_rnn, bi-lstm, glove-cnn-bigru, glove-bilstm are included for the comparison.

## Project Structure:

- Summary_df.csv: CSV file containing ecaluation metrics for each model.
- topsis_result.csv: CSV file with ranked results.
- BarChart.png: Bar chart visualizing the model comparison.

## Results:

**Ranked Table:** 

|MODELS	              |Precision	|Recall	  |F1-Score	|AUC-Score|Performance	      |Rank|
|---------------------|-----------|---------|---------|---------|-------------------|----|
|ann_without_stemming	|0.806122	  |0.618153	|0.699734	|0.753972	|0.4825020772202160 |4.0 |
|simple_rnn	          |0.797642	  |0.635368	|0.707317	|0.757939	|0.5916155663516381	|3.0 |
|bi-lstm	            |0.847222	  |0.57277	|0.683473	|0.748102	|0.3046443798605809	|5.0 |
|glove-cnn-bigru	    |0.852595	  |0.615023	|0.714545	|0.768069	|0.6506581657251116	|2.0 |
|glove-bilstm	        |0.798464	  |0.651017	|0.717241	|0.764604	|0.6743973839814837	|1.0 |

**Bar Chart:**

![Bar Chart](https://github.com/rohanthakur336/topsis_pretrained_BestModel_for_TextClassification/blob/main/BarChart.png)
