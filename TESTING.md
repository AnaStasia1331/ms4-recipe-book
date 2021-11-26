1. Anonymous user can access the Home page.    
    1.1. Expected: anonymous user can access the Home page where s/he sees only Home, Add a new recipe, Login/Sign Up navbar items and ADD A NEW RECIPE section.    
    1.1. Testing: Open a new browser tab, access the url https://ms4-recipe-book.herokuapp.com/ -> Home page is displayed as described in the expected result.
    ![Home page UI for anonymous user](static/img/readme/testing/home-page-anonym-user.png)    
    1.2. Expected: when anonymous user tries to create a new recipe he will be redirected to the Login/Sign Up page.    
    1.2. Testing: 1. Select the navbar item Add a new recipe -> Login/Sign Up page is opened. 2. Click on the pen icon in ADD A NEW RECIPE section -> Login/Sign Up page is opened.    
    1.3. Expected: anonymous user is properly informed what is the purpose of the website and what are the terms of using it.    
    1.3. Testing: Home page header displays the text informing that it's an online recipe book where user can collect and organize her/his favorite recipes on the website. ADD A NEW RECIPE section indicates that after creating 3 recipes, user will be asked to pay once.    
2. Unregistered user can create a new account.    
    2.1. Expected: user can access the Sign Up page by clicking the Sign Up button on the Login page.    
    2.1. Testing: From the Home page click on the Login/Sign Up link in the navbar -> user is redirected to the Sign In page. Press 'Sign Up' button on the Sign In form -> user is redirected to the Sign Up form.    
    ![Sign Up page](static/img/readme/testing/sign-up-page.png)   
    2.2. Expected: user can return to the Sign In/Login page from the Sign Up page.    
    2.2. Testing: 1. From the Sign Up page click the Back link -> the Sign In page is loaded. 2. On the Sign In page press the Sign Up button, then press back browser button -> the Sign In page is loaded.    
    2.3. Expected: user cannot create account with already existing email address.    
    2.3. Testing: On the Sign Up form fill in all fields with valid values, but the email address must exist in db, press the Sign Up button -> The account is not created. User still sees the Sign Up form reset and with the message 'A user is already registered with this e-mail address.'   
    2.4. Expected: user cannot create account with invalid email address.    
    2.4. Testing: On the Sign Up form type invalid email address, e.g. without @ symbol (test.com), validate the field -> user is notified that the entered email is invalid and @ is missing.    
    2.5. Expected: user cannot create account with empty email address/usename/password fields.    
    2.5. Testing: First, leave the email field empty, then add it and leave the username/password blank -> All form fields are mandatory and when not filled in, user is shown the message 'Please fill in this field.'    
    2.6. Expected: user cannot create account with the username lengh less than 5 charachters.    
    2.6. Testing: Enter a username consisting of 3 characters and validate -> The account is not created. User still sees the Sign Up form reset and with the message 'Ensure this value has at least 5 characters (it has 3).'    
    2.7. Expected: user cannot create an account when password entered twice mismatches.    
    2.7. Testing: Enter 1st password, then enter the 2nd password but it must be a different than the 1st one -> The account is not created. User still sees the Sign Up form reset and with the message 'You must type the same password each time.'   
    2.8. Expected: user can create a new account on My Recipe Book website if all entered fields were entered correctly.    
    2.8. Testing: 1. Add valid email/username, mathching passwords and press the Sign Up button. -> User is redirected to another page with the message telling to verify the email. 2. Open the email box and check if the Confirm email is received. -> The email is received with the subject 'Please Confirm Your Email Address'. 3. Click on the link from the email. -> User is redirected back to the website to the Confirm Email page. 4. Press the 'Confirm' button. -> User is redirected to the Login page where s/he can enter his credentials and successfully login (sees the Home page).    
    ![Verify email page](static/img/readme/testing/verify-email.png)   
    ![Confirm email address](static/img/readme/testing/confirm-email-address.png)   
    ![Confirm email page](static/img/readme/testing/confirm-email-page.png)   
3. Registered user can sign into her/his account.    
    3.1. Expected: anonymous can access the Login page.    
    3.1. Testing: From the Home page click on the Login/Sign Up link in the navbar. -> The Login/Sign In form is opened.    
    3.2. Expected: user cannot log in, if s/he uses wrong username or password.    
    3.2. Testing: 1. On the Sign In page enter unregistered username and valid password, press the Sign In button. -> User is not logged, instead s/he sees 'The username and/or password you specified are not correct.'. 2. Repeat the previous test only with wrong password -> The expected result should be the same.    
    3.3. Expected: username and password are mandatory fields to fill in.
    3.3. Testing: Leave username/password blank and try to log in. -> 'Please fill in this field' message is shown to the user.    
    3.4. Expected: user can login successfully when using valid credentials.        
    3.4. Testing: Enter valid username and password and click the Sign In button. -> User is sent to the Home page and in the navbar s/he can see 'Welcome, her/his username'.    
4. Existing user can reset password.    
    4.1. Expected: user can trigger password reset.    
    4.1. Testing: As logged out user navigate to the Login Page and click the Forgot Password? link -> The Reset form is shown to the user. The Back link is available on the form that leads back to the Login form.    
    ![Reset password form](static/img/readme/testing/reset-pw-form.png)  
    4.2. Expected: password cannot be reset if email address is empty.    
    4.2. Testing: Leave the email address field blank and press the Confirm button. -> Password wasn't reset and 'Please fill in this field' message is shown to the user.     
    4.3. Expected: password cannot be reset if email address is invalid.    
    4.3. Testing: Enter invalid email addresss (test"!@#@#@com) and press the Confirm button. -> 'Enter a valid email address.' message is shown to the user.     
    4.4. Expected: password cannot be reset if email address wasn't registered before.    
    4.4. Testing: Enter valid but unregistered email address and press Confirm. -> 'The e-mail address is not assigned to any user account' error message is displayed.    
    4.5. Expected: password can be reset successfully if valid and registered before email address is used.    
    4.5. Testing: 1. Enter valid but registered before email address and press Confirm. -> User is redirected to the Successful reset password page and asked to check her/his email box. 2. Check if the reset password email was received by the user. -> The new email with the subject 'Password Reset Email' arrived. 3. Click the reset password link from the email. -> The website is opened and displays the Change Password form. 4. Leave both password fields blank and submit the form. -> 'Please fill in this field' message is shown. 5. Enter mismatching passwords and submit the form. -> The password reset process wasn't completed and the form is reset. BUG: there is no errror message is displayed to the user, the form is just reset. 6. Enter matching password and submit. -> User is redirected to the next page informing that the password was changed successfully. 7. Click the Go back to Login page link and enter valid credentials with the updated password. -> The user can login successfully.    
    4.6. Expected: the reset password link cannot be used twice, after password was reset.    
    4.6. Testing: 1. Come back to the Password Reset email and try to reset the password second time. -> The new page is opened, however user sees the message that the password reset link was invalid, possibly because it has already been used. 2. Staying on the same page, click the link 'Please request a new password reset.' -> Reset Password form is loaded.    
    ![Successful reset password page](static/img/readme/testing/successful-reset-pw-page.png)    
    ![Change password page](static/img/readme/testing/change-pw-page.png)    
    ![Successfull password reset page](static/img/readme/testing/successful-change-pw-page.png)  
    ![Invalid password reset link](static/img/readme/testing/bad-token.png)    
5. User can log in using her/his Google account.    
    5.1. Expected: user can login to the website when he has an existing Google account but he is currently logged out of it.    
    5.1. Testing: 1. Make sure the user is logged out of her/his Google account, open the website Login page, press 'Sign In With Google' button. -> User is sent to the Google authentication page where he must choose the right account and enter password and depending on the account setup may be asked to go through 2-step verification 2. Sign into the google account. -> At the end user will be automatically redirected to the Home page of My Recipe Book with his username in the header.    
    5.2. Expected: user can login to the website when he has an existing Google account and he is currently logged into it.    
    5.2. Testing: Make sure the user is already log into her/his Google account, open the website Login page, press 'Sign In With Google' button. -> User is automatically redirected to the Home page of My Recipe Book with his username in the header.    
6. User can log out.    
    6.1. Expected: being logged into the website, google authenticated user can log out.    
    6.1. Testing: Sign into the website via Google authentication, click on the Welcome, (username) and select the Logout option. -> Home page is displayed with the updated navbar links: e.g. instead of Welcome, (username) there is Login/Sign Up link.     
    6.2. Expected: being logged into the website, authenticated user can log out.    
    6.2. Testing: Sign into the website in a regular way (by using username and password), click on the Welcome, (username) and select the Logout option. -> Home page is displayed with the updated navbar links: e.g. instead of Welcome, (username) there is Login/Sign Up link.   
7. Uset can add/edit/delete recipes when he is logged in.    