# Hindi_Summarizer
The Machine Learning website takes in Hindi text as input from user and generates a summary for the text in Hindi.
To access the application on the web, use the following url to use the deployed heroku app: https://hindisummary.herokuapp.com 

## Work Flow
The Hindi text is first translated into English by using the python's googletrans module. This corresponding English text is then parsed through various NLP techniques to generate(discussed later)
to generate the summary of the text. The summarised text is then again translated into Hindi text using the same googletrans module. 

These processes are encapsulated within a python function which returns values such as: Original text in Hindi, Summarised text in Hindi, Length of Original text and Length of the summarised text.

The Machine Learning model is then deployed on the web using Flask. The webpage takes input from the user using a form and generates the output on the server using the function mentioned ago.


## Summariser
The translated text is processed through Natural Language Processing. The Library used for this purpose is 'spaCy' which is used for removing all the stop words and punctuations present in the text. These operations are carried out withing the defined function. For generating the summary, the first step was to calculate the frequency of all the words which gives the measures of central tendency, dispersion, percentiles, etc. In other words it gives an idea of the most important parts of the text. 
Next the word with maximum frequency was selected and this frequency was used to normalise all the other word frequencies. 
Similarly the same operation was done for sentences with the word frequencies and the most important sentences were found. 

Alternatively all of these steps could have been skipped by just using BERT, but this project takes a step by step approach.

The summary was calculated as the 2/3 of the given input by using the nlargest function on the selected sentences, so that the generated summary is grammatically sound and coherent.

## Deployment
The website was made using Flask. The first webpage takes in the input from user which upon submitting shows result on the second webpage as the original text and the summarised text both in Hindi language.
The webpage also gives the word count for each.

## Set up and Running
To run the applpication first extract the code in your desired computer directory. Through this directory open command prompt and activate the virtual environment by navigating to the path: ...\text_summary\venv\Scripts and activate. After that download all the packages through the requirements.txt file. 
Run the application app.py by using python command.


# AWS 
1. First an S3 bucket was created on which all the project fiiles were uploaded. 
2. The bucket Next an AWS service role was created with AmazonS3 Full Access. Custom security rules were created for SSH, HTTP and HTTPS with source tag as 'anywhere' so they can be accessed freely. 
3. Next a keypair was generated with extension .ppk so it can be opened with PuTTY ffor connecting the SSH. 
4. Then EC2 instance was launched using with Amazon Linux 2 AMI and the IAM role created earlier was selected along with the security group and keypair made earlier. 5. To run the remote session PuTTY is launched with our IPv4 public IP and the keypair. The apache web server was installed using the command window(see pictures below) and the files from the bucket were downloaded as well. 

### Issues
The only issue this process faces is the next and last step where the service for httpd needs to be started.
This service failure is recurring even when the service is in Active runnning state.
The error message displayed is:  "Redirecting to /bin/systemctl status httpd.service"



![456](https://user-images.githubusercontent.com/74537886/183264201-85feb3fb-dfac-4933-953a-1e789212d4bd.jpg)




![123](https://user-images.githubusercontent.com/74537886/183137913-a3ff3d53-7a5a-41d7-8537-5da04b8d21f3.jpg)

![234](https://user-images.githubusercontent.com/74537886/183137926-83bb42bf-08d5-4dd4-bfc0-7904bb4b6421.jpg)
