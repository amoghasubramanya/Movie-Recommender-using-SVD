# Movie-Recommender-using-SVD
Movie Recommender for MovieLens 100K Dataset using Singular Value Decomposition
<dt>
1) Dataset.txt - Simple dataset for Movie recommender using SVD <br/>
   	svd.py - Simple Movie recommender using SVD (sample output-svd.png)<br/>
		</br>
2)</br>
u.data      --The full u data set, 100000 ratings by 943 users on 1682 items. 
                Each user has rated at least 20 movies.  Users and items are
                numbered consecutively from 1.  The data is randomly 
                ordered. This is a tab separated list of <br/>
	              user id | item id | rating | timestamp. <br/>
                The time stamps are unix seconds since 1/1/1970 UTC<br/>
								<br/>
  u.item     -- Information about the items (movies); this is a tab separated
                list of<br/>
                movie id | movie title | release date | video release date |
                IMDb URL | unknown | Action | Adventure | Animation |
                Children's | Comedy | Crime | Documentary | Drama | Fantasy |
                Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
                Thriller | War | Western |<br/>
                The last 19 fields are the genres, a 1 indicates the movie
                is of that genre, a 0 indicates it is not; movies can be in
                several genres at once.
                The movie ids are the ones used in the u.data data set.<br/>
  </br>
	i)svdtest.py -- To ensure proper working of Recommender system for 100K Dataset with 600 principal components 
	preserving 92% variance of the data  (sample output-svdtest1.png)<br/>  
  ii)svd_movielens.py -- Movie Recommender system for 100K Dataset with 600 principal components 
	preserving 92% variance of the data. (sample output-svd_movielens1.png)</br>
	iii)svd_dr.py -- Movie Recommender to choose Principal components based on the 
	percentage of variance of data to be preserved.(sample output-svd_dr1.png)</br>
</dt>
       
