from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#from sqlalchemy_utils import database_exists, drop_database, create_database

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
user1 = User(name="Jitesh RU", email="jitesh@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(user1)
session.commit()

# Items for Hindi music
category1 = Category(name="Hindi", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Dilbaro", user_id=1, description="Artists: Shankar Mahadevan, Harshdeep Kaur, Vibha Saraf", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="High rated Gabru", user_id=1,  description="Album: Fit & Fab - Workout With Bollywood Songs Artist: Guru Randhawa", category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Nachidi Phira", user_id=1, description="Artist: Meghna Mishra ,Movie: Secret Superstar.", category=category1)

session.add(item3)
session.commit()

# Items for English music
category2 = Category(name="English", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="Havana", user_id=1, description="Artist: Camila Cabello ,Featured artist: Young Thug", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Star Boy", user_id=1,  description="Artist: The Weeknd ,Featured artist: Daft Punk", category=category2)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Waka Waka", user_id=1, description="Artist: Shakira , Featured artist: Freshlyground", category=category2)

session.add(item3)
session.commit()

# Items for Kannada
category3 = Category(name="Kannada", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="Chendutiya Pakkadali", user_id=1, description="Artist: Sonu Nigam ,Movie: Drama", category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Upavasa", user_id=1, description="Artists: Sonu Nigam, Shreya Ghoshal ,Movie: Mr. and Mrs. Ramachari", category=category3)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Kannale", user_id=1, description="Artists: Sonu Nigam, Shreya Ghoshal Movie: Ambareesha", category=category3)

session.add(item3)
session.commit()

# Items for Punjabi
category4 = Category(name="Punjabi", user_id=1)

session.add(category4)
session.commit()


categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name