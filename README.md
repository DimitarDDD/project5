Ecommerce_2
Ecommerce_2 is a-commerce app - Stream 4 Project

This is a fictional ecommerce site, for the nature of this project, for a customers where they can buy or look for a bikes and pay the parcticular bike they want, and customers can lieve their own reviews. 

UX
This site is intended for users  to buy  bikes for the season. By paying online, it makes it easier for users and the app owner to keep track of what is paid and what they ordered, rather than having to keep track of checks or multiple spreadsheets.

Template from the Lms videos was used to build this site. There were some specific UX designs that were taken into consideration when styling this site. The navbar was on the top off the desktop view to present a cleaner, more minimalistic approach to the design,and every page has a background photo. 
If the user wants to buy a bike must log in and creat an account, but still if the user is not log in can check the sale products in the app.

When you click to see detail on a product, you'll be able to also see all of the other reviews and pictures for that product.If the user is loged in ,can add,edit or deelete their own reviews.The navbar is with the same background cover,logo and html file order in every single page.
The user as well can use the recommend button to recommend a product they want when they arre writing a review. 

Technologies
Django (2.0)
Heroku
Postgres Database (mySQL)
Stripe Payment
JavaScript/jQuery
HTML
CSS
Bootstrap (3.3.7)
Development Process
The backend was done first, with the styling added after. As the styling was progressing, and after it was mostly finished, there were some back-end additions that needed to be made.

Once the styling was looking the way I wanted.

Manual Testing:
Manual testing was done for all edit/add/delete/appearance functions in review apps. This was to ensure that what was supposed to be deleting was deleting, and that only designated users (review of the owner or the superuser) was able to delete/edit the content selected. I also verified that the correct author showed up for the posts and comments. All links and forms are verified to be working correctly via manual testing.


The Stripe payment function has been verified with a test card and all transactions show up on the Stripe dashboard.

Stripe Test Cart Payment

Features
Only the owner has access to the admin page. Since it is their property site, it makes it easier for them to monitor all account activity and content. They are the only ones who will be allowed to make master changes to the site. This site has ecommerce. Payments are processed through Stripe, and since it is a fictional site, it only processes 'test card payments.

The cart section allows bike to pay their dues and purchase equipment for. 



Features Left to Implement
I would like to make a blog for mountain bike season program,championships,events and tracks. Furthermore, I would like to add a profile picture ,telephone number and other info for each account not to be hard coded. This functionality would allow the owner of the app to chose between multiple connections for a feedback or just to have an information where the product to be delivered and sharing important informaion for the product if it is needed.

For products, I would also like to implement an option to choose a size, so that team members can purchase their team suits through the site individually specifying their size, along with other apparel that is size-specific. The issue I ran into here, is that swim suits are in numeric sizes (28, 30, 32, etc), while jackets, t-shirts, and other apparel follow the small/medium/large format. Also, certain products, like team dues and equipment, will not have a size. I would like to make it so that some products have a size option (that can vary depending on the product) and some don't.

I hope to implement this website for commercial use by setting up the payment functionality to process real credit cards and add multipe options for the payment for example Ideal or PayPal.


Credits
Content
All content in the product details sections ia taken from the official websites of the brands.

Media
The product photos were taken from  the official websites of the brands.

Acknowledgments
For the reviews, I followed the tutorials in the lms however, it was significantly modified to fit my project, and the ability to edit and delete reviews was added.