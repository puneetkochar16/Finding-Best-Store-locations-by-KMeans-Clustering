# Finding-Best-Store-locations-by-KMeans-Clustering-in-Python-
A company is planning to move into a new city.  The company is trying to decide:
(i)	How many stores should it open?
(ii)	Where should it locate the stores?
Based on data from past cities, the company knows that a customer will visit one of their stores more frequently if the store is located more closely to their home.
The company did some research and modeled the “value” of a customer based on the customer’s location relative to open stores.   They found Value = $2000/(D+1) where D is the distance of the customer’s home to the nearest opened store.  For example, if a customer lives 4 miles from the nearest store of the company, the customer will produce $2000/(4+1) = $400 of marginal profit for the company over his/her lifetime.  If a customer lives 9 miles from the nearest company of the store, the customer will produce only $2000/(9+1) = $200 of marginal profit for the company over his/her lifetime.  As D increases, the customer will visit the company’s stores less frequently, because it is further away, and the result is less marginal profit.
Opening more stores has a benefit – it reduces the average distance a customer is away from the nearest store, thus creating more marginal profit.  However, opening each store costs the company $200,000, a fixed cost.  So each time a store is opened, a cost is incurred by the company.


Goal:
Given a set of customer locations, We are trying to decide how many stores to open and where to place them in order to maximize the company’s total profit.  We assume that we area allowed to open anywhere between 1 and 20 stores in the area.
