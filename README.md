# Assignment: Object-Oriented Programming

In this homework, you'll be writing some object-oriented code (classes). We'll also reinforce our knowledge of  dictionaries.

## Deliverables

You know what you're doing by now! **Fork**/**Clone**/**Commit**/**Push** :grin:

## Submitting

To submit this assignment:

1. Go to the [assignment's main repo](https://git.generalassemb.ly/PYTHR-august-2019/hw-09-oop)
1. Submit a new issue with:
  1. Your name in the Title field
  1. The URL to your assignment repo in the comment field.

---

# Part 1: `Media` Class

For this assignment, write your code in a new file named `movies.py`.

First, create a `Media` class according to the following requirements.

Each instance of `Media` should store two pieces of data, `publisher` and `market`, both of which are strings.

Your `Media ` class should have two instance methods:

1. Write an `__init__` initializer for the class. Whenever this class is instantiated, assume `'USA'` for `market`.

2. In addition to `__init__`, the `Media` class will have one other instance method, `get_media_info()`. This method will print the `self.publisher` and `self.market` instance variables, and return `None`.

Try your code and make sure you can create multiple instances of `Media`.

---

# Part 2: `Movie` Class

Create a `Movie` class. It will inherit from the base `Media` class.

We will use the `Movie` class as a blueprint to create many movie instances, each of which will have different `title`s and `rating`s.

Your `Movie` class should have three instance methods:

1. `__init__`, which will take in `self`, `movie_data` (a dictionary containing `title` and `rating`), `publisher` and `market`.

  `__init__` will set an instance variable, `movie_data`, to be the `movie_data` dictionary passed in.

  Pass on the `publisher` and `market` variables to the `Media` parent (**Hint**: You'll need to use the `super()` built-in function!).

2. `get_title()`, a getter function that returns the value of the `title` key in the `movie_data` instance variable.

3. `get_rating()`, a getter function that returns the value of the `rating` key in the `movie_data` instance variable.

Try your code and make sure you can create multiple instances of `Movie`, and that  `get_title()` and `get_rating()` works as expected.

---

# Part 3: Print All Ratings

Finally, let's make a function `print_all_ratings()`.

* This function will take a *list* of *dictionaries*, each with a `title` string and a `rating` integer
* Iterate through the list. On each iteration, create an instance of `Movie` using the supplied input data
* In addition to the `title` and `rating` which will change with each iteration, use the following hard-coded values when creating the movie:

  | Parameter | Value |
  | --- | --- |
  | `publisher` | `'Universal Studios'` |
  | `market` | `'USA'` |

  * **Hint**: Does something look familiar?

* After receiving the returned `Movie` instance, print out the following: `The movie <movie title> has a rating of <movie rating>`
  * **Hint**: use the `get_title()` and `get_rating()` methods to retrieve the title and ratings of that particular `Movie`

## Starter Code

Use the following starting code:

```python
movie_list = [
  {
    'title': 'Lord of the Rings',
    'rating': 6
  },
  {
    'title': 'Harry Potter',
    'rating': 8
  },
  {
    'title': 'Star Wars',
    'rating': 7
  },
  {
    'title': 'The Matrix',
    'rating': 9
  }
]
```

## Expected Output

The expected output wil be:

```
The movie Lord of the Rings has a rating of 6
The movie Harry Potter has a rating of 8
The movie Star Wars has a rating of 7
The movie The Matrix has a rating of 9
```

---

# Closing Credits

We're done! With all that talk about movies maybe you want to go watch one now?

![](https://media.giphy.com/media/os3eCtuIhKK8U/giphy.gif)
