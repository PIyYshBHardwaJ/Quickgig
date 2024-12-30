# QuickGig

#### Video Demo: <URL https://youtube.com/shorts/vDLh9xpt2A8>

#### Description:
QuickGig is a comprehensive web-based application designed to streamline the freelancing process for both clients and freelancers. It offers an intuitive interface with essential features tailored to meet the needs of the freelancing community. The platform allows clients to hire freelancers and freelancers to find suitable projects to work on. Below, you'll find a detailed breakdown of the application, its functionality, and the rationale behind its design.

### Features and Pages

1. **Login, Logout, and Register**
   - **Login**: Provides access to the application with two primary user roles: "Hire a Freelancer" and "Earn as a Freelancer."
   - **Logout**: Ensures secure user sessions by logging out of the platform.
   - **Register**: Enables new users to create an account to access the platform.

2. **Hire a Freelancer**
   - Displays a table of available freelancers with key details:
     - **Name**: The freelancer's name.
     - **Bio (Skills)**: A short description of the freelancer's skills.
     - **Experience**: The freelancer's years or type of experience.
     - **Contact**: Means to get in touch with the freelancer.
   - **Publish Project**:
     - Users can fill out details like:
       - **Project Title**
       - **Description**
       - **Budget**
       - **Deadline**
       - **Contact Information**
     - Once submitted via the "Post" button, these projects are made available to freelancers.
   - **My Projects**:
     - Allows users to view projects they have published.
     - Provides an option to delete projects via the "Delete" button.

3. **Earn as a Freelancer**
   - Displays a table of available projects posted by clients.
   - Features two primary functionalities:
     - **Create Profile**:
       - Freelancers can create a profile by entering:
         - **Name**
         - **Bio**
         - **Experience**
         - **Contact Information**
       - Profiles can be submitted via the "Create" button and are visible to clients.
     - **View Profile**:
       - Freelancers can review their profiles under "My Profile."
       - Offers an option to delete the profile.

### Files and Their Functions

1. **home.html**
   - Serves as the landing page with navigation links to login, register, and explore features.

2. **login.html & register.html**
   - Forms for user authentication and account creation.
   - Validates user inputs to ensure secure access.

3. **Hire.html**
   - Displays the "Hire a Freelancer" interface.
   - Includes tables to list freelancers and project publishing forms.

4. **earn.html**
   - Houses the "Earn as a Freelancer" interface.
   - Includes sections for viewing and creating freelancer profiles as well as project lists.

5. **styles.css**
   - Provides styling to ensure the platform is visually appealing and user-friendly.

6. **app.py** (or equivalent backend framework)
   - Handles user authentication, database interactions, and API endpoints.
   - Ensures secure data transfer between the frontend and backend.

7. **quickgig.sql**
   - Includes schema definitions for user accounts, freelancer profiles, and projects.
   - Supports CRUD operations for seamless data management.

### Design Decisions

1. **User Roles**:
   - The decision to segment users into "Hire a Freelancer" and "Earn as a Freelancer" ensures clarity and purpose for each user's journey on the platform.

2. **Table Design**:
   - Utilizing tables for displaying freelancers and projects provides a clear and organized view, enhancing user experience.

3. **Profile and Project Management**:
   - Including the ability to create, view, and delete profiles/projects ensures flexibility and control for users.

4. **Simplified Forms**:
   - Ensuring forms are straightforward yet comprehensive reduces friction for users, promoting engagement.

### Conclusion
QuickGig is designed to address the needs of the freelancing ecosystem by providing a user-friendly and functional platform. By balancing simplicity and robust functionality, it facilitates connections between clients and freelancers effectively. With its clear structure and thoughtful design, QuickGig aims to be a valuable tool in the freelancing community.
