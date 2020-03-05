# Project 1 Deliverable

Our plan is to deploy a website that shows a word cloud of all the words in a database, including pre-loaded speeches as well as text that can be entered by users.

## What we will need
At least 2 nodes, one for the front end and one for the back end
A simple database for both pre-loaded speeches as well storing user entered data
webserver host

## Security
We need an architecture that allows users to enter data but not access the underlying database. (Write-only access)

## How?
We plan on using docker and spark to achieve these goals.
For our front end we will be using port: 443 because that is the https port.
for the back end we will be using port: 9000
