function populateRecipes() {


$.getJSON( "/recipes/get_json/", function( recipes ) {
    recipes = $.parseJSON(recipes)
    console.log(recipes);
    recipes.forEach(recipe => {
        const card = $('#card-template').clone()
        card.attr("id", recipe.fields.pk);
        card.find('.recipe-name').val(recipe.fields.recipe_name)
        card.appendTo("#recipes")
        card.show();
    });
 });

    // $.getJSON({
    //     url: "/recipes/get_json/",
    //     success: function (recipes) {
    //         console.log(recipes);
    //         recipes.forEach(recipe => {
    //             const card = $('#card-template').clone()
    //             card.attr("id", recipe.fields.pk);
    //             card.find('.recipe-name').Val(recipe.fields.recipe_name)
    //             card.appendTo("#recipes")
    //         });
    //     },
    //     // iterate over all recipes in data result
    //     // newCard = $(card-template).clone();
    //     // newCard.setTitle = data.title
    //     failure: function (data) {
    //         alert('Got an error dude');
    //     }
    // })
}

window.addEventListener('DOMContentLoaded', event => {
    //called on page load and checkbox event change
    populateRecipes()
});
