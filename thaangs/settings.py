import os

REDIS_URL_TTL = os.getenv('THAANGS_URL_TTL', 60*60*24*3) # 3 days
REDIS_ENTRY_TTL = os.getenv('THAANGS_ENTRY_TTL', 60*60*24*30) # 30 days
REDIS_PREFIX = os.getenv('THAANGS_REDIS_PREFIX', 'thaangs')
REDIS_URL = os.getenv('THAANGS_REDIS_URL', 'redis://localhost:6379/1')
DATABASE_URL = os.getenv('THAANGS_REDIS_URL', 'sqlite:///test.db')
FEED_WORKERS = os.getenv('THAANGS_FEED_WORKERS', 50)

# a list of rss feeds to poll for listicles
RSS_FEEDS = [
  "http://www.buzzfeed.com/community/justlaunched.xml",
  "http://feeds.mashable.com/Mashable?format=xml",
  "http://feeds.feedburner.com/upworthy?format=xml",
  "http://www.littlethings.com/feed",
  "http://thoughtcatalog.com/feed/",
  "http://www.ranker.com/feed/mostpopularlists.rss",
  "http://www.playbuzz.com/RSS",
  "http://feeds2.feedburner.com/22_words?format=xml",
  "http://feeds.feedburner.com/twistedsifter?format=xml",
  "http://www.vox.com/rss/index.xml",
  "http://www.theverge.com/rss/frontpage",
  "http://www.racked.com/rss/index.xml",
  "http://curbed.com/atom.xml",
  "http://www.eater.com/rss/index.xml",
  "http://recode.net/feed/",
  "http://www.polygon.com/rss/index.xml",
  "http://www.huffingtonpost.com/feeds/index.xml",
  "http://feeds.foxnews.com/foxnews/latest?format=xml",
  "http://www.theguardian.com/uk/rss",
  "http://www.nytimes.com/services/xml/rss/yahoo/myyahoo/nyt_yahoo.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/InternationalHome.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/World.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Africa.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Americas.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Europe.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/MiddleEast.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/US.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Education.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Politics.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Upshot.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/NYRegion.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/EnergyEnvironment.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/InternationalBusiness.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/SmallBusiness.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Economy.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Dealbook.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/MediaandAdvertising.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/YourMoney.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/PersonalTech.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Sports.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/InternationalSports.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Baseball.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/CollegeBasketball.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/CollegeFootball.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Golf.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Hockey.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/ProBasketball.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/ProFootball.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Soccer.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Tennis.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Science.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Environment.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Space.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Health.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Research.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Nutrition.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/HealthCarePolicy.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Views.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Arts.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/InternationalArts.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/ArtandDesign.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Books.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/SundayBookReview.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Dance.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Movies.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Music.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Television.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Theater.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/FashionandStyle.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/InternationalStyle.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/DiningandWine.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/InternationalDiningandWine.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/HomeandGarden.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Weddings.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/tmagazine.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Travel.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/JobMarket.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/RealEstate.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Commercial.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Automobiles.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/Obituaries.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/pop_top.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/MostShared.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/MostViewed.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/sunday-review.xml",
  "http://www.nytimes.com/services/xml/rss/nyt/InternationalOpinion.xml",
  "http://apps.shareholder.com/rss/rss.aspx?channels=632&companyid=YHOO&sh_auth=1543149549%2E0%2E0%2E42418%2Eced3027b591867a3587d5595108cddcc",
  "http://www.boredpanda.com/feed/",
  "http://feeds.feedburner.com/uproxx/features",
  "http://elitedaily.com/feed/",
  "http://diply.com/rss",
  "http://aplus.com/feed",
  "http://www.theblaze.com/stories/feed/"
]