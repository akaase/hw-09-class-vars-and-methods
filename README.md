# Assignment: Object-Oriented Programming - Class Variables and Methods

In this assignment, you'll practice:

* `if/else` statements
* Lists and iteration
* Defining classes and instantiating objects/instances
* Defining and using instance variables
* Defining and calling instance methods
* Defining and using class variables
* Defining and calling class methods

This assignment can be challenging! Feel free to collaborate with other students on this assignment, but you should still hand in your own assignment.

## Deliverables and Submitting

You know what you're doing by now! :grin:

---

# Exercise 1: Bank Account

Write your code in a file named `exercise1.py`.

1. Create a class called `BankAccount`.
1. Add a *class variable* called `interest_rate` that is a **float** representing the interest rate for all the accounts in the bank. This is a class variable because it is used across all of the accounts.
1. Add another class variable called `accounts` that starts as an empty list. This will eventually store the collection of all bank accounts in the bank.
1. Add an `__init__` instance method that sets the bank account's `balance` to zero.
   The `balance` is stored in an instance variable because the value needs to be different from account to account.
1. Add an instance method called `deposit` that accepts a number as an argument and adds that amount to that account's balance.
   `deposit` needs to be an instance method because it pertains to a *single, specific* account.
1. Add an instance method called `withdraw` that accepts a number as an argument and subtracts that amount from the account's balance.
   (What should happen if you try to withdraw more money than you have?)
1. Add a *class method* called `create` that makes a new instance of `BankAccount` and adds it to the `accounts` class variable so that it is kept track of.
  `create` should return the new account object.
  `create` needs to be a class method because *at the time we run it* there is no *single, specific* account instance that we are working on.
1. Add a class method called `total_funds` that returns the sum of all balances across all accounts in the `accounts` class variable.  
   `total_funds` needs to be a class method because it *does not* pertain to any *single, specific* account.
1. Add a class method called `add_interest` that iterates through all accounts and increases their balances according to the `interest_rate` in effect for all accounts.
   `add_interest` needs to be a class method because it operates on _all_ bank accounts, not a _single, specific_ account.

### Example output

Assuming that you have set the `interest_rate` to `0.01`:

```
my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance) #==> 0
print(BankAccount.total_funds()) #==> 0
my_account.deposit(200)
your_account.deposit(1000)
print(my_account.balance) #==> 200
print(your_account.balance) #==> 1000
print(BankAccount.total_funds()) #==> 1200
BankAccount.add_interest()
print(my_account.balance) #==> 202.0
print(your_account.balance) #==> 1010.0
print(BankAccount.total_funds()) #==> 1212.0
my_account.withdraw(50)
print(my_account.balance) #==> 152.0
print(BankAccount.total_funds()) #==> 1162.0
```

---

# Exercise 2: Vampire Infestation

There's a vampire infestation! But that doesn't mean we don't have time to practice using class variables and methods.

Write your code in a file named `exercise2.py`.

Now that you've had some experience using class variables and methods it's time to test your knowledge of _when_ to use them.

Your task is to create a `Vampire` class that stores a list of vampires (a `coven`, if you will).

Every vampire has a `name`, `age`, an `in_coffin` boolean, and a `drank_blood_today` boolean.

Every day at sunset the vampires leave their coffins in search of blood. If they don't drink blood and get back to their coffins before sunrise, they die.

Your class should have the following methods:

* `__init__`, which creates a new vampire and assigns values for each of its attributes
* `create`, which creates a new vampire and adds it to the coven
* `drink_blood`, which sets a vampire's `drank_blood_today` boolean to true
* `sunrise`, which removes from the coven any vampires who are out of their coffins or who haven't drank any blood in the last day
* `sunset`, which sets `drank_blood_today` and `in_coffin` to false for the entire coven, as they go out in search of blood
* `go_home`, which sets a vampire's `in_coffin` boolean to true

It's up to you to determine whether each method should be an instance method or a class method.

You'll also have to decide what instance and class variables you need.

If you're not sure whether a method should be an instance method or a class method, starting to write the body of the method may help you figure it out based on what data you need access to. 

If you're still uncertain, don't be afraid to ask an instructor for help during office hours.

Good luck!



---

# Food for Thought

You're done! But here's a parting thought:

Isn't it strange how, in most vampire fiction, vampires are lavishly wealthy, often living in expensive homes and wearing fine clothing?

![](https://media.giphy.com/media/Quauv5GIn3WR9OY7RS/source.gif)
