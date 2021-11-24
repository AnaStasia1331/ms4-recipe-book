DRAFT
1. Home page.  
    * Expected: user clicks the nav and social media links from the Home page and is redirected to the right pages/sections.
    * Testing:
        * click on the Home nav item -> the Home page is refreshed;
        * click on the logo -> the Home page is refreshed;
        * click on the Add A New Recipe nav item -> Add A New Recipe form is opened with 2 buttons: Cancel and Save;
        * click on the Courses nav item -> the Courses section is opened with multiple courses types;
        * click on the My Recipes nav item -> All Recipes page is opened either with recipe cards or 'No recipes have been added yet' text;
        * click on the Add A New Recipe pencil icon -> Add A New Recipe form is opened with 2 buttons: Cancel and Save;
        * click on each Course picture in the Course section -> page is loaded for the specific Course type, e.g. breakfast or dinner. The page displays recipes in the selected category or 'No recipes have been added yet' text;
        * click on the facebook/instagram/twitter icons -> facebook/instagram/twitter page is opened in a separate tab.
2. Add a New Recipe form (covers the user story #1).
    * Expected: when user forgets to add a title to a recipe, the new recipe can't be created.
    * Testing:
        * leave the Recipe Name field empty and try to save the recipe -> user is asked to fill in the field and the recipe wasn't saved.
    * Expected: when user forgets to select a course from the dropdown, the new recipe can't be created.
    * Testing:
        * fill in the Recipe Name, but leave the default text selected in the Couse dropdown and try to save the recipe -> user is asked to select a course and the recipe wasn't saved.
    * Expected: user can save a recipe with a recipe name with no more than 50 characters.
    * Testing:
        * try to add recipe name containing more than 50 char  -> after 50th character typing is not possible.
    * Expected: user can select any course type from the Courses dropdown.
    * Testing:
        * click the dropdown -> all 6 course types are visible in the dropdown;
        * select a value from the dropdown -> the correct value is selected.
    * Expected: user can paste/type large amount of text in Ingredients and Steps textarea.
    * Testing:
        * paste a long text (more than 2000 characters) -> the long text is accepted.
    * Expected: user can set preparation time.
    * Testing:
        * select a half an hour or an hour as cooking time -> the correct time is set.
    * Expected: user can cancel the recipe creation.
    * Testing:
        * click the Cancel button -> from Add a New Recipe form the user is redirected back the page visited earlier.
    * Expected: user can save a new recipe successfully.
    * Testing:
        * fill in all required and optional fields in the form and click the Save button -> user is redirected to the All Recipes page, he can find his recipe on the page based on title. When he opens the recipe, he can see that it contains all text/selection filled in earlier.
3. All Recipes page (covers the user story #3).
    * Expected: the links on the page work. 
    * Testing:
        * test all nav item and footer links -> each link redirects to the desired page/section.
        * preconditon: at least 1 recipe must be created:
            * on the recipe card click the View icon -> View Recipe page is opened;
            * on the recipe card click the Edit icon -> Edit Recipe page is opened;
            * on the recipe card click the Delete icon -> the delete modal window for the selected recipe pops up.
    * Expected: when many recipes were created on the page, the cards layout displays without major issues.
    * Testing:
        * create more than 4 recipes (for desktop) -> the recipes are displayed in 4 columns. They have the same size: height and width regardless difference in title length. Long titles are shown with ellipsis;
        * create many recipes to check the list is scrollable -> user can scroll without issues.
    * Expected: all created recipes can be found on the All Recipes page.
    * Testing:
        * create several recipes with different course types -> regardless the course assigned to the recipes, they all display on the All Recipes page.
4. Edit Recipe form (covers the user story #5).
    * Expected: user is able to update any field of the edit form.
    * Testing:
        * find an existing recipe, press the Edit icon and try to edit Recipe Name, Courses, Ingredients, Steps, Preparation Time -> all mentioned places are editable.
    * Expected: user is able to update the edit form successfully.
    * Testing:
        * edit Recipe Name, Courses, Ingredients, Steps, Preparation Time and click the Save button -> user is redirected to All Recipes page, can find his recipe and when press the View or Edit icons can see that the previously made changes were applied.
    * Expected: user is able to cancel form editing.
    * Testing:
        * edit an existing recipe and click the Cancel button -> user is redirected to the previously visited page, when he reopens the recipe he can't see the change he made before pressing the Cancel button.
5. View Recipe form (covers the user story #4).
    * Expected: user is able to view an existing recipe but can't update the recipe in the view mode.
    * Testing:
        * find an existing recipe, press the View icon try to edit Recipe Name, Courses, Ingredients, Steps, Preparation Time -> all mentioned places are for read only and can't be updated.
    * Expected: user is able to view an existing recipe and proceed to the edit mode.
    * Testing:
        * open a recipe in the view mode and press the Edit button -> user is redirected to the Edit Recipe page for the same recipe.  
    * Expected: user is able to view an existing recipe and close the view mode.
    * Testing:
        * open a recipe in the view mode and press the Back button -> user is redirected back to the previously visited page.
6. Delete recipe (covers the user story #6).
    * Expected: user can select a recipe on All Recipes page or a specific course page and click the Delete icon.
    * Testing:
        * find an existing recipe, press the Delete icon -> the Confirm delete popup opens for the selected recipe.
    * Expected: user can delete an existing recipe
    * Testing:
        * find an existing recipe, press the Delete icon, confirm the action -> the popup is closed, the recipe has been deleted. It cannot be found on the related course page or All Recipes page.
    * Expected: user can cancel the delete action from the Confirm delete popup.
    * Testing:
        * find an existing recipe, press the Delete icon, cancel the action -> the popup is closed, the recipe has not been removed neither from the related course page nor from the All Recipes page.
7. Course page (covers the user story #2)
    * Expected: user should be able to find his recipes quicker, based on course type.
        * Testing:
            * precondition: add recipe in e.g. breakfast category. From the Home page click 'Breakfast' in the Course section -> the created recipes is displayed on the Breakfast page.
8. No recipes created.
    * Expected: user should be informed when no recipes were created yet on a particular course page or All Recipes page.
    * Testing:
        * find a course type when no recipes were added -> user sees the message 'No recipes have been added yet.'
9. Page not found.
    * Expected: user should be informed when no recipes were created yet on a particular course page or All Recipes page.
    * Testing:
        * hit a non-exisitng url, e.g. https://ms3-my-recipe-book.herokuapp.com/course_non-existing/other_courses -> user sees the 404 page.
10. Testing on mobile device (covers the user story #7).
    * Expected: every page of the website should display without issues; user should be able to easily navigate through My Recipe Book; creation/viewing/editing/deletion must be possible to do from the mobile device.
    * Testing:
        * open the Home page -> the page is opened, the navigation links are hidden but instead there is the Menu button. When clicked, all links are present in the expanded menu.
        * scroll down the Home page -> Add a new recipe section and Courses section are visible. Courses cards/links are displayed in 1 column.
        * open the All recipes page with multiple recipes created -> all recipes are displayed in 1 column.
        * create/view/edit/delete a recipe -> each action can be performed successfully.