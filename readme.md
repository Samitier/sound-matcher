# Technical test BMAT

## Installation & execution

This app needs Phython, Django and Django Rest Framework installed in order to execute the backend. It also needs Node to install and transpile the Vue frontend app.

The data will be persisted in a PostgreSQL database, and its credentials have to be provided in `settings.py -> DATABASES`.

When everything is installed, some commands must be executed from the root directory of the project.

```
// Executing database migrations
> python manage.py migrate
```
```
// Starting server
> python manage.py runserver
```
```
// Installing node_modules and executing build script
> cd client
> npm i
> npm run build
```

If there are no errors, you should be able to open `http://localhost:8000` and access to the vue app:

![Screenshot of the app](./capture.gif "Screenshot of the app")
 


Your database should be filled with all the sound data & candidates too.


## Part 1 (Getting the candidates)

### Introduction:

First of all, this is the first time I use Django. Sorry if the code is a bit messy or I break some Python or Django style conventions.

Since this exercise is about seeding a database I decided to put all the code as a Django migration in the folder `soundmatcher/migrations`.

I also created 3 models: `Recording` (the data from `sound_recordings.csv`), `Search` (the data from `sound_recordings_input_report.csv`), and `Match` (the relationship between a `Search` and a `Recording`, with a score).

### The matching method (Question 1)

For the matching method, I decided to count the "changes" needed for the fields of a search to "reach" the equivalent fields of a sound.

For example: if an author is `Mose` and we compare it to `Muse`, the score for this matching will be 1, since we need a change of one character to transform `Mose` to `Muse`.

I used the Levenshtein Distance algorithm (https://en.wikipedia.org/wiki/Levenshtein_distance) to calculate this scores for each property and then generate the final score as the average of the scores of all the properties.

For the ISRC I also set that if both ISRC are equal, then we assume that the search is exactly equal than the sound, since it's a unique identifier.

For the duration of the sound, I only compared the difference between both integers.

Finally, I transformed this average of scores to a percentage in a given range. I thought that a percentage of "confidence" would be much clearer and easier to work with.

### Scalability (Question 2)

No, this solution is not scalable for a lot of reasons.

The main problem is that we will be comparing and potentially storing results for the combination of all the inputs with all the sounds. That can quickly create a table too big to handle.

Besides, we are looking through all the songs each time we load a search. This will probably break too, since we are calculating millions of scores each time.

### Improvements (Question 3)

I think this project is the exact use case for a service like Elastic Search.

Elastic Search is basically a search engine for large collections of data where performance is critical. Exactly what we would be doing if we had a large collection of sounds.

Other ideas could be storing the songs in an in-memory database like redis and calculate the scores on demand without storing the results in a database.

## Part 2 (Interactive matcher)

### Introduction

For this part, I implemented an app with Vue, Vuex and Typescript. I also made a JSON api in Django with Django Rest Framework, for fetching the data from the DB.

### Layout (Question 1)

I designed this UI with simplicity in mind. I think that simplicity and minimalism is what improves usability the most in an interface.

For this use case we want to make the user select an input from a list of available inputs. 

I thought that a dropdown list would be great for this, since it will not fill a lot of space in the screen and its one of the most common elements in a UI and everybody knows how to use it.

When the user selects something, another list will appear with all the matches. Until then, there is nothing occupying space and distracting the user.

The matches will be sorted by their score, and they color will fade the lower their score is. This will cause a contrast between the important matches and the false positives.

### Improvements (Question 2)

First of all I would add some animations (like a loading animation for the matches). Animations guide the user between interactions and gratly improve the usability of an interface.

Another improvement could be filtering the elements of the dropdown with a text search field on the dropdown itself.

Finally, I would make the interface a bit better for desktop. I designed this for desktop and mobile, but for desktop there is a lot of empty space.
