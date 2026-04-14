# Q.2. Createac lass with the following attributes:
#     1. Title
#     2. Author
#     3.list of reviews

# ADD METHOD TO:
# ADD A NEW REVIEW TO THE BOOK
# COUNT REVIEWS
# DISPLAY THE BOOK DETAILS


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def count_reviews(self):
        return len(self.reviews)

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Number of Reviews: {self.count_reviews()}")
        print("Reviews:")
        for review in self.reviews:
            print(f"- {review}")

# Create an instance of Book
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
# Add reviewsto the book
book1.add_review("A masterpiece of American literature.")
book1.add_review("A timeless classic that explores themes of wealth and society.")
# Display book details
book1.display_details()

# Create another instance of Book
book2 = Book("To Kill a Mockingbird", "Harper Lee")
# Add reviews to the book
book2.add_review("A powerful novel about racial injustice.")
book2.add_review("A compelling story with unforgettable characters.")
book2.add_review("A must-read for everyone.")
# Display book details
book2.display_details()
