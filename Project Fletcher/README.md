<b>1.  Who is your client / user / audience ?<b>
<u>Audience:<u>
I want my project to be accessible and interesting to everyone and not just foodies and/or restauranteurs.  I believe most people receive some type of enjoyment out of nice restaurants, and we all need food to survive.   I'd like to make something that would be interesting for yelp (since that is where I am pulling data from), fivethirtyeight, the national restaurants news (nrn.com), and the tourism industry in general.

<b>2.  What is the central question your project addresses?<b>
<u>Central question:<u>
What should I eat of a particular type of cuisine in a particular city?

<b>3.  What is theme of your project?
What would make a good, informative title (or subtitle) for your project?
Write a prioritized list of more specific sub-questions, if applicable, or an elaboration of the central question.<b>
"CuisinArt & Data"
Question breakdown:
Out of 119 different types of ethnic cuisine, what types of cuisines and dishes are rated the highest in the top 10 most populated cities in the U.S.?  What are common comments given to each type of cuisine and are there differences between cities?


<b>4a. What data will you use to address the question, from which source(s)?<b>

4.. b. How will you acquire the data?

4.. c. How much data will there be?

4.. d. How will you organize and store the data?

How will you approach the analysis of your data? 
(This can be a complete plan or a description of planned first steps and conditional later steps)

What will be the form of your final deliverable? How will you present your findings? 
Anticipated formats are blog post or dashboard.

What challenges do you anticipate?
(eg: Where might surprise challenges be lurking? Are their any weak points in your plan? Are you counting on something coming out statistically significant? Are you using something fuzzy like sentiment analysis to create sub-populations? Can you think of a failsafe? Something interesting to do or say if your "gamble" comes up bust?)


Central question:
Are the Chicago Blackhawks destined to win the 2012 Stanley Cup based on their season-opening point streak?

Question breakdown:

how does the statistic "season-opening point streak" (the number of games a team makes it into a hockey season before their first regulation loss) relate to stanley cup victory? if this relationship is statistically significant, stop here.
how does season-opening point streak relate to success in the playoffs in general?
Data: 
a. Opening season point streaks and end-of-season outcomes for all teams in all hockey seasons in the modern era. b. Scrape from hockey-reference.com
c. Not much space (30 teams * 100 seasons * << 50kb per season record = < 150MB raw data) 
d. Write a script that calculates the opening season point streak from the schedule and results page, get the season outcome from the main season page, and store with team and season in a flatfile (pickle) / python dictionary in memory.

Analysis:
Start with logistic regression to see if the point streak relates to Stanley Cup outcome (1,0). If this is not interesting, do either linear regression or categorical regression with playoff outcome (numerical values for no playoffs, eliminated in first round, ..., Stanley cup loss, Stanley cup victory). If this is not interesting, ... not sure.

Deliverable:
The main event will be the cool d3 dashboard, but it will not make sense without some kind of post/description.

Challenges:
If nothing comes out statistically significant, I hope people like playing with the dashboard controls and seeing the outcomes change. Maybe I could look at additional statistics like strength of schedule or injuries to chase after significance a bit more, but if it is not close (sample size will be very small) I'll just focus on making the dashboard fun to play with.
