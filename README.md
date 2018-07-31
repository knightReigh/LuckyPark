# LuckyPark
An unofficial nationalstatepark archive and recommendation system.

## Planning

### Database 
A **mongodb database** stores national park informaiton and state park information. 

*The database is collected by myself so the content is limited. If you are interested in expanding it into a real databse, please contact me.*

National parks list are regularly checked out from: https://www.nps.gov/findapark/index.htm.

State park lists are regularly checked out: I don't know yet.

API:

- [ ] show(): show all parks in database, by state then alphabetical order
- [ ] search({query}): query for one park
- [ ] update(): check repo to update information
  - [ ] \_add_new(id): add an new entry
  - [ ] \_remove(id): remove an entry
  - [ ] \_renew(id): update information for park id
  - [ ] \_renew_all(): renew all park information. taking long time. designedly for monthly schedule. 

### Recommendation System
A **Feeling Lucky** recommendation system. Need to store cookie version or use a **log in** system to tailor customized recommendations.

API:

- [ ] Feel Lucky: randomly recommend one park if NOT trained. recommend a trained choice.
- [ ] My Top 10: recommend 10 "Feel Lucky" item (no duplicate)
- [ ] What's Trendy: Use google trends to serve the current trending choice for national park based on user's geographic preference.
- [ ] Query-level feel lucky: Allow users to get recommendation based on chosen preference (like a search)

### Web Front

Currently I am considering REACT system hosted on Google or AWS or Azure, whichever is free :D


# Disclaimer

This project is for academic use only. It does not support any commercial use.  
