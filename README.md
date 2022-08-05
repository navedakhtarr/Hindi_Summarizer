# Hindi_Summarizer
The Machine Learning website takes in Hindi text as input from user and generates a summary for the text in Hindi.

## Work Flow
The Hindi text is first translated into English by using the python's googletrans module. This corresponding English text is then parsed through various NLP techniques to generate(discussed later)
to generate the summary of the text. The summarised text is then again translated into Hindi text using the same googletrans module. 

These processes are encapsulated within a python function which returns values such as: Original text in Hindi, Summarised text in Hindi, Length of Original text and Length of the summarised text.

The Machine Learning model is then deployed on the web using Flask. The webpage takes input from the user using a form and generates the output on the server using the function mentioned ago.


## Summariser
The translated text is processed through Natural Language Processing. The Library used for this purpose is 'spaCy' which is used for removing all the stop words and punctuations present in the text. These operations are carried out withing the defined function. For generating the summary, the first step was to calculate the frequency of all the words which gives the measures of central tendency, dispersion, percentiles, etc. In other words it gives an idea of the most important parts of the text.
Next the word with maximum frequency was selected and this frequency was used to normalise all the other word frequencies. 
Similarly the same operation was done for sentences with the word frequencies and the most important sentences were found.
The summary was calculated as the 2/3 of the given input by using the nlargest function on the selected sentences, so that the generated summary is grammatically sound and coherent.

## Deployment
The website was made using Flask. The first webpage takes in the input from user which upon submitting shows result on the second webpage as the original text and the summarised text both in Hindi language.
The webpage also gives the word count for each.

## Set up and Running
To run the applpication first extract the code in your desired computer directory. Through this directory open command prompt and activate the virtual environment by navigating to the path: ...\text_summary\venv\Scripts and activate. After that download all the packages through the requirements.txt file. 
Run the application app.py by using python command.


To access the application on the web, use the following url to use the deployed heroku app: https://hindisummary.herokuapp.com 
