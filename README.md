## Inspiration
Paper is a major environmental issue, making up approximately 26% of total waste in landfills around the world. Around 320 million books are discarded every single year, many of them being unread. Our mission was to create an application that not only reduces this waste but also provides a seamless, sustainable way for users to access and share the books they love.

## What it does
Our app empowers users to buy, sell, and exchange books within a vibrant community of book enthusiasts or donate them to institutions in need. By promoting reusability and reducing waste, we’re not just connecting book lovers, but are also paving the way for a sustainable future, one book at a time!

The users have the option to buy, sell, exchange, or donate their books. Everytime a user uploads a book that they intend to sell, the details of the book and the seller are fed into a database. If another user wishes to purchase a book, they simply have to search the book title or author, and they can see the different prices the book is being sold at and their conditions. After choosing a seller, they can contact them through the app chat message feature. The process is similar if two book users wish to exchange books with one another. If the user chooses to donate their book, the map feature in the app would allow them to see donation centers, charities, libraries, and schools that are currently accepting donations.

## How we built it
To build the application, we used Python and SQLite in the backend to have a database that can be used for the buying and selling of products. We used HTML, CSS, and Javascript to build one part of the frontend: the ISBN lookup. The user would input an ISBN number and the system would look up the book on the Google Books API to return the title, author and description. Finally, we used Figma for the UI/UX design and for overall user flow.

## Challenges we ran into
Learning SQLite for the first time and integrating it with our app to manage the book database was challenging. Additionally, we had no prior experience working with APIs so we had to learn how to send requests and handle responses, particularly to get book information from the Google Books API. Working with Figma was also new to some of us.

## Accomplishments that we're proud of
We successfully implemented Google Books API to accurately get book details from user-input ISBNs and ensure the interface handles any possible errors. We have a functioning database of books taken from seller inputs, including details such as book titles, authors, and descriptions obtained from the Google Books API. We are proud of creating an intuitive user interface that makes adding and searching for books simple and efficient.

## What we learned
We gained hands-on experience with integrating APIs, working with html/css/javascript to create a user-friendly interface, as well as learning SQlite. We improved our understanding of designing applications and gained valuable technical skills.

## What's next for ShelfSwap
Our next steps include integrating a seamless payment system within the app, enabling users to effortlessly buy, sell, and exchange books. We will also introduce user profiles where members can earn "Green Points" for every book they exchange or donate, rewarding eco-conscious actions. Additionally, we’ll offer subscription and membership options, with all proceeds going directly to support a local charity, allowing users to contribute to a meaningful cause through their book transactions.
