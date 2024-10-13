# School Learning Management System

![Mock-up](media/home_page.png)

#### By Lauren Pechey

[Click here to view the live web application](https://school-lms-project-06a6aa171a7b.herokuapp.com/)

This is the documentation for a School Learning Management System (LMS) built as an Individual project for the Secure Software Development module at the University of Essex Online. It has been built using Django, Python, BootStrap, CSS3 & HTML5.

## Planning, Design & User Experience

I approached the planning & design of this project using the principles of User Experience, which include the 5 stages of strategy, scope, structure, skeleton & surface. This project has many important security considerations so it was important to make sure it remained on course, on time and the the best it could be whilst meeting all of the criteria for the MVP (Most Viable Product). 

### Project Aims

The main purpose of the project was to create a simple School LMS website, which allows parents, students and admin to view their timetables, grades and profiles through the site. The project was based off the initial group design document which also took security measures into consideration. 

## Skeleton

### Wireframes

#### Wireframes (see below)

Wireframes were developed using [Figma](https://www.figma.com/), including making all colour, typography and layout decisions at this stage. This was done to ensure that the focus would be on building the site, rather than designing it.

### Models

The site uses a relational database model using Postgres [NeonTech](https://neon.tech/). The app uses a number of models: User, StudentProfile, UploadedFile, Grade, Timetable, and Email. The User model is created by Django allauth and connects to a separate Email Address Model. 

#### Typography

The website uses 2 typefaces that I felt worked well together and complemented each other:
- Open Sans for headings, paragraphs & the site logo.
- Sans Serif as the default backup font.

## Features

This section shows details of all features on the site including details of their value to the user.

### Home Page

![Mock-up](media/home_page.png)

- All pages have title & description meta tags to improve their SEO performance. 

### Authentication Pages

![Sign In Page](media/login.png)

<details><summary>Authentication Pages (AllAuth)</summary>

- The project uses AllAuth to implement User login and authentication functionality. AllAuth comes with a whole load of backend functionality and front end templates that make the user, registration, sign in/out and user management easy and quick to create.
- AllAuth provides a series of templates for all the actions required to implement authentication. The site uses these with its own bespoke styling to make them feel part of the site.
- All the form have been styled using the [widget-tweak](https://pypi.org/project/django-widget-tweaks/) package to add styling classes to inputs, labels and error messages from within the form templates

<img src="media/login.png">
<img src="media/logout.png">
<img src="media/signup.png">

**Value to User**

A strong authentication system is vital to a school LMS, allowing users to log in, register, manage their profile, see their grades and timetables and store their data for the next time they want to visit the site. It improves user experience and make the process of visiting the site quicker and smoother. The styling of the forms matches the rest of site making it feel like it belongs and building confidence and trust in the site.

</details>

### Grades Page

![Mock-up](media/grades.png)

### Timetable Page

![Mock-up](media/timetable.png)

### Profile Page

![Mock-up](media/myprofile.png)



