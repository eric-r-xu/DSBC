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

2.  A wide release movie plays at 600 theaters or more at its widest release ( reference: http://www.boxofficemojo.com/about/boxoffice.htm ).  Because my client is planning a wide release movie, movies released at less than 600 theaters in its widest release will not be used.  

3.  Since my client is interested in top horror studios, I created a table to find out what they were along with the mean of the log domestic gross of each studio:
![](./img/tableStudioCount.png)

From the table, Universal, Sony, Warner Bros, Fox, Paramount, New Line, and Lionsgate are all studios that have created at least 20 horror films.  I created dummy variables for these top horror studios (and for 'other studio') to see whether my client would benefit in choosing one of these top studios to distribute the movie.

4.  I was also curious whether the year of the horror film as well as the number of theaters at its widest release had an effect on the gross.  I scatterplotted both of these independent measures against gross.

![](./img/Theater_Num.png)
![](./img/Theater_Num_Adj.png)
![](./img/Year.png)
![](./img/Year_Adj.png)





