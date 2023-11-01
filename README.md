# CalorieCompass
## Overview
Welcome to CalorieCompass, your ultimate companion on the journey towards achieving your personal health and fitness goals. This innovative web application is designed to track your daily calorie intake, ensuring you stay on the right path to nutritional wellness.

CalorieCompass is not just a simple calorie counter. It's a comprehensive tool that provides an in-depth view of your eating habits, helping you understand more about your diet and how it affects your overall health. By logging your meals, you can easily monitor your intake of not just calories, but also essential nutrients - from proteins and carbs to vitamins and minerals.

The application is designed with user-friendly features that make it easy for you to log in your daily meals. All you need to do is input the food you've consumed, and CalorieCompass will calculate the calories for you. Whether you're eating out or cooking at home, we've got you covered with our extensive database of food items and their nutritional values.

## Project Goals
This is my fourth portfolio project for Code Institute and my goal with this project is to display my newly acquired skills with frameworks such as Bootstrap and Django. I decided to build a calorie tracker webapp that fetches the information from an API website

## Contents

## The Strategy Plane
CalorieCompass goal is to provide a comprehensive and user-friendly app that enables users to track their nutritional intake, understand the caloric and nutritional content of foods, and suggests activities to offset caloric intake. We want to become the go-to app for individuals looking to maintain a healthy diet, lose weight, or gain insight into their eating habits.

## The Ideal User
- Someone wants to track their caloric intake daily.
- Someone wants to know nutrition facts about the food they eat.
- Someone wants to track sports activities needed to burn the food they ate.

## Site Goals
- Provide users to create their own profile.
- Provide users to add their daily meals.
- Provide users an interface to know nutritional facts about food.
- Provide users a graphical representation of the macro nutrients food.
- Provide users a graphical representation of their caloric intake.

## Agile planning
This project was developed using agile methodologies by delivering small features across the duration of the project. All User Stories were assigned to Epics, prioritized under the labels, Must Have, Should Have and Could Have. They were assigned story points according to complexity. Story points were adjusted mid-project to use the common Fibonacci sequence correctly. "Must Have" stories were completed first, "Should Have's" and then finally "Could Have's".

The Kanban board was created using Github projects and can be located [here](https://github.com/users/moabdelbasset/projects/2/views/1) and can be viewed to see more information on the project cards. All stories have a full set of acceptance criteria to define the functionality that marks that story as complete.


## The Skeleton Plane
This is the prototype of the project that may change during its development. 
<details><summary>Wireframe Example</summary>
<p>
    <img src="./Docs/wireframes/wireframe1.png" alt="Desktop Part 1">
</p>
<p>
    <img src="./Docs/wireframes/wireframe2.png" alt="Desktop Part 1">
</p>
<p>
    <img src="./Docs/wireframes/wireframe3.png" alt="Desktop Part 1">
</p>
<p>
    <img src="./Docs/wireframes/wireframe4.png" alt="Desktop Part 1">
</p>
<p>
    <img src="./Docs/wireframes/wireframe5.png" alt="Desktop Part 1">
</p>
<p>
    <img src="./Docs/wireframes/wireframe6.png" alt="Desktop Part 1">
</p>
</details>

### Security

Views were secured where needed using the Django decorator @login_required. Access to the views using the @login_decorator can only be accessed by registered users. This means that if a user tries to access a view that is decorated with @login_required, but they are not currently logged in, they will be redirected to the login page instead.

Environment variables were stored in an env.py for local development for security purposes to ensure no secret keys, API keys, or sensitive information was added to the repository. In production, these variables were added to the Heroku config vars within the project.


## **The Scope Plane**

* Responsive Design - The site should be fully functional on all devices from 320px up
* Hamburger menu for mobile devices
* Home page describing the site and links to features for registered users

## **The Structure Plane**

### **Features**
`
As a User I would like to view the site on my different devices so that I can view the site on the go
`

**Navbar**

`
As a User I want to see a clear way of navigating the site so that I can find the information relative to my needs
`

The Navbar contains links for Home, Tracked food, Add meals, Nutrion page, and Profile pages.

The following navigation items are available on all pages:
  * Home - Visible to all but for logged in users it will give a summary of caloric intake in the last 7 days
  * Login - Visible to logged out users
  * Signup - Visible to logged out users
  * Tracker - Visible to logged in users
  * Profile -> profile.html - Visible to logged in users
  * Record your meals -> add_tracker.html - Visible to logged in users
  * Nutrition -> nutrition.html - Visible to logged in users
  * Logout -> logout.html - Visible to logged in users

The navigation menu is displayed on all pages and drops down into a hamburger menu on smaller devices. This will allow users to view the site from any device and not take up too much space on mobile devices. It is easily noticeable, intuitive, and easy to use.

![Navbar Desktop 1](./Docs/screenshots/header1.png)

![Navbar Desktop 2](./Docs/screenshots/header2.png)

![Navbar Mobile](./Docs/screenshots/header3.png)  


**Footer**

`
As a User I want to be able to get in touch with the Developer so that I can enquire about issues/suggestions I may have
`

The footer is placed at the bottom of the page. The social media links are displayed with icons provided by Font Awesome. This is where the user can click on a social media link and reach out to the developer for news and updates. A link to the developer's Github repository is provided and displayed using the Font Awesome Github icon. These icons have aria labels added to ensure users with assistive screen reading technology know the purpose of the links. They also open new tabs as they lead users away from the site.

![Footer](./Docs/screenshots/footer.png)  

**Homepage**

There are two variations of the Home page that change based on User login/registration. Users that have not signed up will be met with a welcome message and some information about the site. Details of features available to registered Users are shown and a Sign-Up button is provided.

Users that have registered and logged in will be met with a similar layout but this time there will be buttons linking the user to various functions but they will land on a user dashboard that will display the user caloric consumption during the last seven days.

![Homepage before login](./Docs/screenshots/homepage1.png) 

![Homepage after login](./Docs/screenshots/homepage2.png)   

**Tracker Page**
`
As a User I want to have a section where I can view all my addead meals with the coresponding calories
`

The Tracker page has a similar layout to the Home page as the user can view all the added meals with the date and the calories.

![Tracker page](./Docs/screenshots/tracker1.png)   

`
As a User I want to edit the entered meals in the Tracker page
`

In the tracker page users can edit meals entered 

![Tracker page](./Docs/screenshots/tracker2.png)   

`
As a User I want to delete any entered meal in the Tracker page
`

In the tracker page users can delete meals entered 

**Profile**

`
As a User I would like access to my Profile so that I can upload an image or alter my details where needed
`

Profile features are only available to registered users.

When a user signs up to the site a Profile will automatically be created for them. They can access their Profile page from the Profile Navbar link. On the Profile page, the user can add/change information like their profile image, age and weight. Users can also upload their own Profile image and if they do not want to a default image is provided. 

![Tracker page](./Docs/screenshots/profile1.png)   


**Record your meal**
`
As a User I would like record my meals
`

Record your meal is only available to registered users.

Users can add their meal and the app will calculate the amount of calories for this meal and will record it with the date choosed by the user

![Record your meal page](./Docs/screenshots/record.png)   


**Nutrition**
`
As a User I would like to search for nutritional facts for certain amount of food
`

Users can search for nutritional facts of the searched food. It can give warnings if some food has high of fats, calories or sugar. Also, It will view the nutritonal facts in a graphical representation and it will give the amount of effort needed to burn the amount of calories you will get from this food

![Nutrition Page](./Docs/screenshots/nutrition1.png)   
![Nutrition Page](./Docs/screenshots/nutrition2.png)   


**Error Pages**

**404 Page**

`
As a Developer I can implement a 404 error page so that I can alert users when they have accessed a page that doesn't exist
`

A 404 page has been implemented and will display if a user navigates to a broken link.

The 404 page will allow the user to easily navigate back to the main website if they direct to a broken link / missing page, without the need for the browser's back button.

![Error 404](/docs/readme_screenshots/desktop_404.webp)

**403 & 403_csrf Pages**

`
As a Developer I can implement a 403 error page to redirect unauthorised users so that I can secure my views
`

A 403 error page has been implemented to provide feedback to the user when they try to access unauthorized content. Users will be directed to this page if they alter the URLs and attempt to edit, delete, or access pages that are restricted.
A 403_csrf error page has been implemented to provide feedback to the user when there is an issue with csrf verification. 

![Error 403](/docs/readme_screenshots/desktop_403.webp)
![Error 403_csrf](/docs/readme_screenshots/desktop_403_csrf.webp)

**500 Page**

`
As a Developer I can implement a 500 error page so that I can alert users when an internal server error occurs
`

A 500 error page has been displayed to alert users when an internal server error occurs. The message relays to users that the problem is on our end, not theirs.

![Error 500](/docs/readme_screenshots/desktop_500.webp)


**Favicon**

A favicon has been added the website to enable users to easily locate the website in the browser when multiple tabs are open.


