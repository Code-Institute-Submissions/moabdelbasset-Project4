# **CalorieCompass Testing**

## **Testing Overview**

A wide range of testing was carried out during development by myself.

## **Contents**


## **Automated Testing**

### **Unit Testing**

Unit tests were created to test the functionality of the apps. These can be found in the tests.py files in the respective apps.

#### **Home**

![Home](/docs/unit_testing/test_home.png)


#### **Profiles**

**Views**

![Profiles Views](/docs/unit_testing/test_profile_views.png)

**Models**

![Profiles Models](/docs/unit_testing/profile_test_models.png)

#### **Tracker**

**Views**

![Tracker Views](/docs/unit_testing/tracker_test_views.png)

**Models**

![Tracker Models](/docs/unit_testing/tracker_test_models.png)


### **Site Coverage Report**

Through my testing, I was able to get a total of 90% coverage across the site. The remaining 5% will be covered through manual testing.

![Coverage 1](/docs/unit_testing/coverage_report.png)

[Back to top &uarr;](#contents)


## **Manual Testing**
| Test Case | Description  | Steps    | Excpected Results | Actual Results | Pass/Fail |
|-----------|--------------|----------|-------------------|----------------|-----------|
| TC-01     | Home page loads explaining the application purpose for non logged in users | Login to the app | Home page loads explaining the app and give the option to login or sign up | Home page loads explaining the app and give the option to login or sign up | Pass |
| TC-02.    | As a new user I should be able to sign up and create an account | Login to the home page Then click sign up | Sign up page loads and user should add their information | Sign up page loads and user should add their information | Pass |
| TC-03     | As a user I should able to login from a login page | Go the home page then click on Login | A login page should load and user should be able to login using the username and password created | A login page should load and user should be able to login using the username and password created | Pass |
| TC-04     | As a logged in user I should view the home page that contains a summary of my added calories | Go the application and Login | The user should be redirected to the home page and see a graphical representation of the last entered calories | The user should be redirected to the home page and see a graphical representation of the last entered calories | Pass |
| TC-05     | As a logged in user I should able to view all my entered meals | Login to the application then click on Tracker | The logged in user should be able to see all his entered meals | The logged in user is able to see all his entered meals | Pass |
| TC-06     | Meals in the tracker page are grouped according to the date entered | Login to the app > Go to Tracker > Insert couple of meals | The logged in user should be able to see the meals entered grouped according to the date of the meal | The logged in user should be able to see the meals entered grouped according to the date of the meal | Pass |
| TC-07     | As a user I should be able to edit entered meals | Go to the Tracker page and Edit one of the entered meals | Once changing the meals it should update the calories and meal and the quantity | The meal, calories and quantities changes | Pass |
| TC-08     | As I user I should be able to delete an entered meal | Go to the Tracker page and choose one of the meals and click on delete | The meal should be deleted | The meals is deleted | Pass |
| TC-09     | As a user I should be able to view my profile information | Login to the app and click on the profile link | The profile page should load | Profile page loaded and views user information | Pass |
| TC-10     | As a user I should be able to edit my profile information such as weight | Go to the profile page and click on Edit | User should be able to edit his wieght | User was able to edit his wieght | Pass |
| TC-11     | As a user I should be able to edit my profile information such as picture | Go to the profile page and click on Edit | User should be able to edit his wieght | User was able to edit his picture | Pass |
| TC-12     | As a user I should be able to edit my profile information such as age | Go to the profile page and click on Edit | User should be able to edit his wieght | User was able to edit his age | Pass |
| TC-13     | In the profile section it should load the correct recorded meal information | Login to the app and check how many entered meals then compare it to the entered meals in the profile section | Results should be the same | Results is the same | Pass | 
| TC-14     | As a user I shoule be able to access record meal page | Login to the app and click on record your meal link | Record your meal link should open | Record your meal page loaded properly | Pass |
| TC-15     | As a user I should be able to add my meals | Login to the app and click on record your meal link and start filling out the information then click Add your meal | The meal should be added successfully | Meal was added successfully | Pass |
| TC-16     | The entered meals should has a real value and accept real food | Login to the app and click on record your meal link and in the meal name enter any random characters | An error should appear | Error appeared telling that the food is not found in the database | Pass |
| TC-17     | Users cannot enter meal in future dates |  Login to the app and click on record your meal link check the date of the meal | Users should be able to add meals in the past till todays date only | Users are able to add meals in the past till todays date only | Pass |
| TC-18     | The app should be able to automatically calculate the calories using API calls | Go to the record meal page  enter a meal name and quantity | The app should calculate the calories of the entered meal | The app calculated the calories of the entered meal | Pass |
| TC-19     | As a user I should be able to logout | Click on logout | User should be able to logout | User logged out | Pass |
| TC-20     | As a user I should not be able to see other user meals | - | Users are not able to view each other meals | Pass | 
| TC-21     | As a user I should be able to access the nutrition page | From the app go to nutrition page | Nutrition page should load | Nutritiion page loaded | Pass |
| TC-22     | As a user I should be able to view nutritional values of an entered meal | From the nuturition page enter any meal and click searh | Nutrition values should appear | Nutrition values appeared | Pass |
| TC-23     |  As a user I should be able to view the amount of work needed to burn the amount of calories | - | - | Amount of work appeared | Pass |
| TC-24     |  As a user I should be able to view the nutrional values in a graphical representation | - | - | Nutritional values appeared in graphical representation| Pass |
| TC-25     | As a user when I click on LinkedIn Icon in the footer it should redirect me to the developer linkedin profile in a new page| On any page click on the linkedin icon | a new page will open with the profile of the developer | a new page was opened with the developer profile | Pass |
| TC-26     | As a user when I click on Github Icon in the footer it should redirect me to the developer Github project in a new page| On any page click on the Github icon | a new page will open with the project page | a new page was opened with the project page | Pass |
| TC-27     | As a user when I click on Twitter Icon in the footer it should redirect me to Twitter in a new page| On any page click on the linkedin icon | a new page will open   | a Twitter page was opened | Pass |
| TC-28     | As a user when I click on Youtube Icon in the footer it should redirect me to Youtube in a new page| On any page click on the Youtube icon | a new page will open   | a Youtube page was opened | Pass |
| TC-29     | As a user when I click on Instagram Icon in the footer it should redirect me to Instagram in a new page| On any page click on the Instagram icon | a new page will open   | a Instagram page was opened | Pass |
| TC-30     | Warning should appear if the food contains high sugar | Go the nutrition page and search for pepsi | a warning should appear because food contains high amount of sugar | Warning appeared | Pass |
| TC-31     | Warning should appear if the food contains high sugar | Go the nutrition page and search for chicken | a warning should appear because food contains high amount of sodium | Warning appeared | Pass |

