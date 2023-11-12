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
| TC-09     | 