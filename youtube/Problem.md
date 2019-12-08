# Analyse Product Sentiment with Youtube

## Summary

The model should take in the ticker symbol of a company and output a company sentiment score which will be a value between -1 and 1.

## Use cases

* The model will primarily be used for consumer facing companies which sell basic products or services with a mass-market or niche market appeal. 
* YouTube is a haven for people to give their opinions on their daily lives and there is no shortage of this. 
* The site is used for product reviews (e.g. make-up, games, technology, home appliances, new product unboxings) with channels boasting millions of subscribers. 
* Firstly we will try to analyse 2 markets: make-up and technology. 
* Within make-up there is scope to analyse videos giving positive or negative opinions on new companies and products. The prime example is the upcoming brand ELF Beauty whose revenues soared after a wave of positive sentiment on YouTube. 
* Within technology we can analyse videos to find the best CPUs, GPUs, phones, headphones, drones, gaming rigs, and cameras on the market and which company will be profiting off of this in the future. 

## Part 1 - Brand Names

* Try to parse consumer facing brands the publicly listed company in question owns. 
* This is because the brand names will be the only relevant names on YouTube. 

## Part 2 - Looking for Videos

* Query a YouTube API with the generated brand names. 
* Investigate how to build the query given a brand name.
* e.g. Gucci + product + review, Gucci + ratings, Gucci + bad + quality? 
* There could be some positive, neutral and negative queries generated looking for specific data and amalgamating this using a weighting. 
* Use a text classifier to judge the relevance of the video based on the video title, tags and description. 

## Part 3 - Video to Signal

* Get the auto generated YouTube subtitles for the specific video and analyse text using a text classifier. 
* This will output a sentiment score for the specific video about a specific brand and should then be weighted using the relevance score.
* Convert product review to sales: estimate number of products sold. A starting point would be to compare to previous products and their volumes sold. In the absence of previous products, look at similarly sized firms in the industry. The model would need to take into account the current and future economic climate. Include error bars for sales figures. Correct the figures if and when sales reports emerge. 
* Convert sales to revenue and profit margins: this needs to take into account the importance of the product within the company. The revenue is the average price * number of sales. This should be converted into gross profit. What percentage of the total profit is due to the specific product? 
* Convert profit margings to EPS and changes in stock price. The change in profit should be correlated to the change in stock price assuming the P/E ratio stays the same throughout. After a given margin of safety a signal should be outputted by the model for the specific financial instrument in question.

## Future Development

* Use auto generated subtitle data to influence the relevance score of a video.
* Try to find a weighting justifying the importance of a specific brand name to the stock price. It might be possible to do this using past correlation data on the brand and the stock. 
* Factor in geographical data to analyse product and service launches/usage/sentiment in a specific region e.g. a soap brand by Unilever might be performing well in emerging markets however influence might be decreasing in developed economies. 
* Analyse advertisments and marketing campaigns companies make on highly influential YouTube channels.
* Analyse relevant video comments for sentiment. 
* Investigate lags for signals from YouTube to movements in the stock price. 