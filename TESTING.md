### Visit the site deployed on Heroku: [Book-store](https://book-store-49b1de6a7e87.herokuapp.com/).

## AUTOMATED TESTING

### W3C Validator

[HTML W3C](https://validator.w3.org/) was used to validate the HTML code.

![HTML VALIDATOR IMAGE](/static/readmeimg/htmlvalidator.png)

- [Home Page](https://book-store-49b1de6a7e87.herokuapp.com/) - 0 errors
- [Offers](https://book-store-49b1de6a7e87.herokuapp.com/products/?category=most_recommended) - 0 errors
- [About](https://book-store-49b1de6a7e87.herokuapp.com/about/) - 0 errors
- [Contact](https://book-store-49b1de6a7e87.herokuapp.com/contact/) - 0 errors

[CSS W3C](https://jigsaw.w3.org/css-validator/) was used to validate the CSS code.

- style.css file - 0 errors
  ![CSS Validator](/static/readmeimg/cssvalidator.png)

### LightHouse

I have used developer tools Lighthouse to test my website on mobile and desktop versions.

#### Desktop Version

![.](/static/readmeimg/lighthouse.png)

#### Mobile Version

![.](/static/readmeimg/lighthousemobile.png)

## User Stories Testing

#### As a Shopper, I want to view individual book details so that I can identify the price, description, author, and other details.

![.](/static/readmeimg/viewbookdetail.png)

#### As a Shopper, I want to view a list of books so that I can select some to purchase.

![.](/static/readmeimg/viewlistofbooks.png)

#### As a Shopper, I want to view books by specific genres or categories so that I can quickly find books I’m interested in without searching through all books.

![.](/static/readmeimg/viewbooksbytitleorauthor.png)

#### As a Shopper, I want to easily view the total of my cart at any time so that I can manage my budget.

![.](/static/readmeimg/viewtotalcart.png)

#### As a Shopper, I want to quickly identify discounted books or special offers so that I can take advantage of savings.

![.](/static/readmeimg/viewbookdeals.png)

#### As a Site User, I want to easily register for an account so that I can have a personalized profile and track my orders.

![.](/static/readmeimg/register.png)

#### As a Site User, I want to easily log in or log out so that I can access my personal account information.

![.](/static/readmeimg/loginlogout.png)

#### As a Site User, I want to have a personalized user profile so that I can view my order history and save payment and delivery information for future purchases.

![.](/static/readmeimg/personalizedprofile.png)

#### As a Shopper, I want to sort the list of available books so that I can easily identify bestsellers or books with the highest ratings.

![.](/static/readmeimg/sortbooks.png)

#### As a Customer, I want to add books to my wishlist so that I can save them for future purchases

![.](/static/readmeimg/addwishlist.png)

#### As a registered user, I want to earn loyalty points for each purchase so that I can redeem them for discounts on future orders

![.](/static/readmeimg/earnpoints.png)

#### As a registered user, I want to view my current loyalty points balance so that I know how many points I have available

![.](/static/readmeimg/viewpoints.png)

#### As a registered user, I want to apply my loyalty points at checkout so that I can reduce my order total

![.](/static/readmeimg/applypoints.png)

####As a registered user, I want to receive a confirmation message when I successfully apply loyalty points so that I know they have been deducted.

![.](/static/readmeimg/successpoints.png)

#### As a registered user, I want to view my wishlist so that I can easily find the products I have saved

#### As a registered user, I want to remove items from my wishlist so that I can manage my saved products effectively

![.](/static/readmeimg/mywishlist.png)

## Manual Testing

### Navigation Test:

1. Click on each navigation link (Home, Products, Categories, Contact Us, Profile) in the header navigation bar.
2. Verify that each link redirects to the correct page without any errors.
3. Ensure that the active link is visually highlighted to indicate the current page.

### Product Detail Test:

1. Navigate to the Products page and select a book.
2. Verify that the product detail page displays all relevant information (e.g., title, description, price, and rating).
3. Add the product to the cart and ensure it reflects correctly in the cart summary.

### Cart Functionality Test:

1. Add multiple products to the cart from the product listings or detail pages.
2. Go to the Cart page and verify that all selected products, quantities, and total prices are displayed correctly.
3. Test updating the quantity of an item in the cart and ensure the total price updates accordingly.
4. Remove an item from the cart and verify that it disappears from the cart summary.

### Profile Test:

1. Navigate to the Profile page.
2. Update delivery information (e.g., address, phone number) and verify that changes are saved successfully.
3. Check the order history section to ensure all orders are displayed correctly, including details such as products, prices, and dates.

### Contact Form Test:

1. Go to the Contact Us page.
2. Submit a message with valid inputs (name, email, subject, message) and verify that the form submits successfully.
3. Test submitting the form with invalid inputs to ensure validation works correctly.
4. Verify that submitted messages are stored in the admin panel for review.

### Newsletter Subscription Test:

1. Enter an email address in the newsletter subscription form on the homepage.
2. Submit the form and verify that it accepts the email and displays a success message.
3. Test submitting with an invalid email format and ensure proper validation errors are shown.

### Checkout Process Test:

1. Add products to the cart and proceed to checkout.
2. Complete the checkout process by entering valid details and verify that the order is successfully placed.
3. Ensure the order appears in the user's order history on the Profile page.
4. Test the checkout process with invalid inputs to ensure validation errors are displayed.

### My Wishlist Test:

1. Add a product to the wishlist and verify that it appears in the wishlist section
2. Remove a product from the wishlist and ensure it no longer appears in the list
3. Test the wishlist functionality on different devices and browsers to ensure compatibility
4. Check that wishlist data remains intact after logging out and logging back in
5. Ensure that the "Add to Wishlist" button is only visible for logged-in users
6. Verify that wishlist items do not expire unless manually removed by the user

### Loyality Points Test:

1. Earning Points:

   - Place an order and verify that the correct number of loyalty points are awarded based on the purchase amount( for each 10$, the user gets 1 point)
   - Ensure that points are only credited after the order is successfully completed

2. Redeeming Points:

   - Apply loyalty points at checkout and verify that the discount is correctly calculated
   - Ensure that the remaining balance after applying points meets the minimum order total requirement
   - Test using more points than allowed and verify that an appropriate error message is displayed

3. Points Balance:
   - Verify that users can view their total loyalty points in their profile

### Links Test:

1. Check if all links open in a new tab/window.
2. Ensure all links function correctly on various devices and screen sizes.
