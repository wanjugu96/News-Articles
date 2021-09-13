# News_Bulletins

## Author

[Wanjugu-Mung'au](https://github.com/wanjugu96)

# Description
This is an application that will help people who want to get realtime news withouth having to watch TV for the news. The website will show news articles from several sources and news sources that a user can click to see morw news. The  application consumes news from the [News API](https://newsapi.org/)

## Live Demo

Click [Link](https://news-bulletins.herokuapp.com/) to visit the site


## User Story

1. A user would see various news sources on the homepage of the application.
2. A user would also be able to select a news source and see all news articles from the selected news source in the application.
3. A user will be able to see the image, description and the time a news article was created from the News-Articles tab.
4. A click on an article and read the full article on the source website.


## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  git clone https://github.com/wanjugu96/News-Articles.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd News articles
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export API_KEY='{Enter your News Api Key}'
  ```
4. Running the application by :
  ```bash
  python3.6 manage.py server
  ```
  OR run the application by :
  ```bash
  bash start.sh on your terminal
  ```

5. Testing the application
  ```bash
  python3.6 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.6](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [shellmithwanjjugu98@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2019 **Wanjugu Mung'au**