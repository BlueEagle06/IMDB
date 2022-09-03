import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd

class IMDB_Spider(scrapy.Spider):
    name="imdbspider"

    def start_requests(self):
        yield scrapy.Request(url=r'https://www.imdb.com/chart/top/?ref_=nv_mv_250',callback=self.parse)

    def parse(self,response):
        Movie_names=response.css('td.titleColumn > a::text').extract()
        links=response.xpath('//td[@class="titleColumn"]/a/@href')
    
        for link in links:
            url = response.urljoin(link.extract())
            yield response.follow(url=url,callback=self.parse_movie_page)

        

    def parse_movie_page(self,response):
        #imdb rating
        IMDB_Rating=response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]/text()').extract_first()
        list_ratings.append(IMDB_Rating)

        #movie names
        Movie_names=response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/h1/text()').extract_first()
        list_names.append(Movie_names)

        #release year
        release_year=response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div/ul/li[1]/a/text()').extract_first()
        list_year.append(release_year.strip())

        #duration
        duration=response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div/ul/li[3]/text()').extract()
        duration1=""
        for letter in duration:
            duration1=duration1+letter
        list_duration.append(duration1.strip())
        
        #genres
        genres=response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/div/a/span/text()').extract()
        genres1=""
        for genre in genres:
            genres1=genres1+" "+genre
        genres=genres1.strip()
        genres=genres.replace(" ",", ")
        list_genres.append(genres)

        #director
        directors=response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]/div/ul/li/a/text()').extract()
        directors1=""
        for director in directors:
            directors1=directors1+"  "+director
        directors=directors1.strip()
        directors=directors.replace("  ",", ")
        list_directors.append(directors)

        #summary
        summary=response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/p/span[3]/text()').extract_first()
        list_summary.append(summary)

        #writers
        writers=response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[2]/div/ul/li/a/text()').extract()
        writers2=""
        for writer in writers:
            writers2=writers2+"  "+writer
        writers=writers2.strip()
        writers=writers.replace("  ",", ")
        list_writers.append(writers)

        #stars
        stars=response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[3]/div/ul/li/a/text()').extract()
        stars1=""
        for star in stars:
            stars1=stars1+"  "+star
        stars=stars1.strip()
        stars=stars.replace("  ",", ")
        list_stars.append(stars)

        #user reviews
        user_reviews=response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/ul/li[1]/a/span/span[1]/text()').extract_first()
        list_user_reviews.append(user_reviews)

        #critic_reviews
        critic_reviews=response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/ul/li[2]/a/span/span[1]/text()').extract_first()
        list_critic_reviews.append(critic_reviews)

        #metacritic
        metacritic=response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/ul/li[3]/a/span/span[1]/span/text()').extract_first()
        list_metacritic.append(metacritic)

        #budget
        budget=response.xpath('//li[@data-testid="title-boxoffice-budget"]//ul/li[@class="ipc-inline-list__item"]/span[@class="ipc-metadata-list-item__list-content-item"]/text()').extract_first()
        list_budget.append(budget)

        #gross
        gross=response.xpath('//li[@data-testid="title-boxoffice-cumulativeworldwidegross"]//ul/li[@class="ipc-inline-list__item"]/span[@class="ipc-metadata-list-item__list-content-item"]/text()').extract_first()
        list_gross.append(gross)

        #certificate
        certificate=response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div/ul/li[2]/span/text()').extract_first()
        list_certificate.append(certificate)

        #popularity
        popularity=response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[2]/div/div[3]/a/div/div/div[2]/div[1]/text()').extract_first()
        list_popularity.append(popularity)

        #consolidation into a dictionary
        dict1["Movie Name"]=list_names
        dict1["IMDB Rating"]=list_ratings
        dict1["Release Year"]=list_year
        dict1["Runtime"]=list_duration
        dict1["Genres"]=list_genres
        dict1["Directors"]=list_directors
        dict1["Summary"]=list_summary
        dict1["Writers"]=list_writers
        dict1["Stars"]=list_stars
        dict1["User Reviews"]=list_user_reviews
        dict1["Critic Reviews"]=list_critic_reviews
        dict1["Metacritic Score"]=list_metacritic
        dict1["Budget"]=list_budget
        dict1["Gross Box Office Worldwide"]=list_gross
        dict1["Certificate"]=list_certificate
        dict1["Popularity Ranking"]=list_popularity
        


        #return dictionary
        yield dict1
    
        

list_names=[]
list_ratings=[]
list_year=[]
list_duration=[]
list_genres=[]
list_directors=[]
list_summary=[]
list_writers=[]
list_stars=[]
list_user_reviews=[]
list_critic_reviews=[]
list_metacritic=[]
list_budget=[]
list_gross=[]
list_certificate=[]
list_popularity=[]

dict1={}


process=CrawlerProcess()
process.crawl(IMDB_Spider)
process.start()
pd.set_option('display.max_columns', 500)
df=pd.DataFrame(dict1)
print(df)
df.to_csv("imdb.csv")
