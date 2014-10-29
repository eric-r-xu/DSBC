PROJECT FLETCHER: ERIC XU

<b>1.  Who is your client / user / audience ?</b>
<br><u>Audience:
I want my project to be accessible and interesting to everyone and not just foodies and/or restauranteurs.  I believe most people receive some type of enjoyment out of nice restaurants, and we all need food to survive.   I'd like to make something that would be interesting for yelp (since that is where I am pulling data from), fivethirtyeight, the national restaurants news (nrn.com), and the tourism industry in general.

<b>2.  What is the central question your project addresses?</b>
<br><u>Central question:</u>
What should I eat of a particular type of cuisine in a particular city?

<b>3.  What is theme of your project?
What would make a good, informative title (or subtitle) for your project?
Write a prioritized list of more specific sub-questions, if applicable, or an elaboration of the central question.</b>
<br>"CuisinArt: Cuisine, Art, and Data about Ethnic Cuisine in the U.S"
<br>Question breakdown:
<br>Out of 119 different types of ethnic cuisine, what types of cuisines and dishes are rated the highest in the top 10 most populated cities in the U.S.?  What are common comments given to each type of cuisine and are there differences between cities?
<br>
<b>4a. What data will you use to address the question, from which source(s)?</b>
<br>I will use restaurant data from yelp (www.yelp.com)
<br>
<b>4.. b. How will you acquire the data?</b>
<br>I will acquire using the yelpAPI as well as scraping comments on yelp using Python's 'requests' package

<b>4.. c. How much data will there be?</b>
<br>There will be data from 40 top restaurants per category of cuisine per city, 119 different categories of cuisine, and 
10 cities.  Each restaurant will have an overall yelp rating and number of ratings as well as the top 5 positive comments and the top 5 negative comments.  Each comment will also have its own rating score.  Thus, I will have upwards to 47,600 restaurants in my dataset and upwards to 476,000 comments from all these restaurants combined.

<b>4.. d. How will you organize and store the data?</b><br>
I will store each restaurant's data (along with city, rating, reviews, etc.) as a document in a mongoDB collection.  These collections will be stored locally in a mongoDB database.

<b>5.  How will you approach the analysis of your data? </b><br>
I will use pairwise t-tests to test if a specific city has a significantly higher average rating of a particular ethnic cuisine.  I will do td-idf of the high and low restaurant comment words/phrases to find highly rated and lowly rated dishes and common highly rated and lowly rated comments of particular types of cuisine.

<b>6.  What will be the form of your final deliverable? How will you present your findings? </b><br>
Blog Post about top cities of a certain type of cuisine as well as number of those restaurants in that city (sampling bias!).  with a word cloud d3 visualization of most common words used to positively and negatively describe specific ethnic restaurants

<b>7.  What challenges do you anticipate? </b><br>
I anticipate that some cities may not have many (or any) of a certain type of ethnic restaurants.  If that is the case, I will either (a) take those ethnic restaurants out of all analyses or (b) combine certain types of ethnic restaurants or (c) take a percentile of the top restaurants of a particular ethnic cuisine in a city.


