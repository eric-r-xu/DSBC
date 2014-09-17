<b>Eric Xu -- luther MVP submission -- 9/16/2014 -- Summary of Progress<b>

Client : A horror filmmaker planning a wide release film and is in the process of choosing a distributor/studio.

Client’s request :  How can I increase the total domestic gross of the movie I create? 

Dataset : All films from BoxOfficeMojo with keyword "Horror":

  - Horror - Period
  - Horror - Slasher
  - Horror - Supernatural
  - Horror - Terror in the Water
  - Horror - Torture
  - Horror - Anthology
  - Horror - Comedy
  - Horror - Remake
  - Sci-Fi Horror

Features (to choose from in dataset) : 

  - domestic total gross 
  - log domestic total gross
  - adjusted total gross (raw and logged) based on number of months since release
  - studio
  - number of theaters at widest release
  - budget
  - month and season of release
  - year of release
  - movie rating (e.g. PG)
  - runtime



1.  The dependent measure that we want to maximize for the client is total domestic gross.  Analysis of this dependent measure via histogram reveals a high positive skew.  
![](./img/dtgHist.png)  
  
By changing this dependent measure to the log of the total domestic gross, we can see a dramatic reduction in the skew.  This will be our dependent measure as the approximation made by the central limit theorem will be improved.
![](./img/dtgLogHist.png)

2.  A wide release movie plays at 600 theaters or more at its widest release (http://www.boxofficemojo.com/about/boxoffice.htm ).  Because my client is planning a wide release movie, movies released at less than 600 theaters in its widest release will not be used in the regression. The following is a histogram of the number of theaters at each wide release horror movie:
![](./img/TheaterNumberHist.png)


3.  The client is only interested in the top studios for distribution.  The client claims that (1) the studio's experience can be a great asset in increasing gross and (2) studios without much experience carry a lot of risk and can simply be lucky.  The following is a table showing the studios making the most horror films as well as the mean of the log total domestic gross of all the studio's horror films:
![](./img/tableStudioCount.png)


From the table, Universal, Sony, Warner Bros, Fox, Paramount, New Line, and Lionsgate are all experienced horror studios with at least 20 horror films distributed.  To help my client choose the most successful horror studio and avoid others, I created dummy variables for these 7 top horror studios and one for all other studios for the regression.  





