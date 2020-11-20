# FarmleadQATest

The automation framework is written using Page Object Model using Python and Pytest architecture. Technology stack used:- Python,Selenium.Pytest, Page Object Model

Goal is to :- Re-Usability Maintainability

Steps Involved:-

Step 1:- Create new project & install Required Packages/plugins -Selenium Libraries -Pytest:Python UnitTest Framework -Allure-pytest: to generate allure reports

Step 2:- Create Folder Structure

ProjectName

|

drivers

|

PageObjects

|

prerequisitedata

|

testscripts

|

utilities

Drivers:- Place we add the webbrowser driver(I used chromebrowser)

PageObjects:-Place we describe about the web elements and the action to be performed in each and every respective pages

prerequisitedata:- Place where we add config.ini file that helps in taking record of all the common used data

testscripts:- basically they are the tesst cases folder where we call the pageobject classes and perform the implementation

utilities:-Place where we implemented readproperty file that read data from config.ini file and prevent the hardcoding
