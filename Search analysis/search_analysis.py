import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()


# for example: createing a DataFrame of the top 10 countries which search for “Machine Learning” on Google:
trends.build_payload(kw_list=["Machine Learning"])
data = trends.interest_by_region()
data = data.sort_values(by="Machine Learning", ascending=False)
data = data.head(10)
print(data)



#  visualizing data using a bar chart:
data.reset_index().plot(x="geoName", y="Machine Learning", figsize=(15,12), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()



# have a look at the trend of searches to see how the total search queries based on “Machine Learning” increased or decreased on Google:
data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=['Machine Learning'])
data = data.interest_over_time()
fig, ax = plt.subplots(figsize=(15, 12))
data['Machine Learning'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches for Machine Learning', fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()

######################


# Now try this code with "Data analysis" :
trends.build_payload(kw_list=["Data analysis"])
data = trends.interest_by_region()
data = data.sort_values(by="Data analysis", ascending=False)
data = data.head(10)
print(data)


data.reset_index().plot(x="geoName", y="Data analysis", figsize=(15,12), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()