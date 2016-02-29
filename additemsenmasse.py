
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)


session = DBSession()

# Create dummy user
#User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             #picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
#session.add(User1)
#session.commit()

# add 1st category 
category1 = Category(user_id=1, name="Soccer")

session.add(category1)
session.commit()

# add soccer items
Item1= Item(user_id=1, name="Shinguards", description="""The shin guard was \
inspired by the concept of a greave. A greave is a piece of armor used to \
protect the shin. It is a Middle English term, derived from an Old  \
French word, greve (pronounced griv), meaning shin or shin armor.\
1. The etymology of this word not only describes the use and purpose of shin \
guards, but also contributes to dating the technology""",category=category1)

session.add(Item1)
session.commit()

Item2= Item(user_id=1, name="Strip", description=""" The terms 'kit', 'strip', \
and in North American English "uniform" are used interchangeably. The sport's\
Laws of the Game specify the minimum kit which a player must use, and also \
prohibit the use of anything that is dangerous to either the player or another \
participant. Individual competitions may stipulate further restrictions, \
such as regulating the size of logos displayed on shirts and stating that, \
in the event of a match between teams with identical or similar colours, \
the away team must change to different coloured attire.""",category=category1)

session.add(Item2)
session.commit()

Item3= Item(user_id=1, name="Soccer boots", description=""" Football boots, \
called cleats or soccer shoes in North America, are an item of footwear worn \
when playing football. Those designed for grass pitches have studs on the \
outsole to aid grip. From simple and humble beginnings football boots have \
come a long way and today find themselves subject to much research, \
development, sponsorship and marketing at the heart of a multi-national \
global industry. Modern "boots" are not truly boots in that they do not \
cover the ankle.""",category=category1)

session.add(Item3)
session.commit()

# add 2nd category 
category2 = Category(user_id=1, name="Basketball")

session.add(category2)
session.commit()

#add basketball items
Item4= Item(user_id=1, name="Backboard", description="""A backboard is a piece \
of basketball equipment. It is a raised vertical board with a basket attached. \
It is made of a flat, rigid piece of material, often Plexiglas. It is usually \
rectangular as used in NBA, NCAA and international basketball. But many \
backboards may be oval or a fan-shape, particularly in non-professional games. \
Today most professional backboards are made of a glass backboard so that it \
will not obstruct the audience's view, although most non-professional \
backboards are made from something that may obstruct the audience's view, \
such as goals at parks or on streets.""",category=category2)

session.add(Item4)
session.commit()

Item5= Item(user_id=1, name="Court", description="""Basketball courts come in \
different sizes and colors. In the NBA, the court is 94 feet (29 m) by 50 feet \
(15 m). Under International Basketball Federation (FIBA) rules,[1] the court \
is minutely smaller, measuring exactly 28 metres (92 ft) by 15 metres (49 ft). \
A high school court is slightly smaller, at 84 feet (26 m) by 50 feet (15 m). \
In amateur basketball, court sizes vary widely. The baskets are always 10 feet \
(3.0 m) above the floor (except possibly in youth competition). \
Basketball courts have a three-point arc at both baskets. A basket made from \
behind this arc is worth three points; a basket made from within this line, or \
with a player's foot touching the line is worth two points. The free-throw \
line, where one stands while taking a foul shot, is located within the \
three-point arc""",category=category2)

session.add(Item5)
session.commit()

# add 3rd category item 
category3 = Category(user_id=1, name="Baseball")

session.add(category3)
session.commit()

# add baseball items
Item6= Item(user_id=1, name="Bat", description="""A baseball bat is a smooth \
wooden or metal club used in the sport of baseball to hit the ball after it is \
thrown by the pitcher. By regulation it may be no more than 2.75 inches in \
diameter at the thickest part and no more than 42 inches (1,100 mm) long. \
Although historically bats approaching 3 pounds (1.4 kg) were swung,[1] today \
bats of 33 ounces (0.94 kg) are common""",category=category3)

session.add(Item6)
session.commit()

Item7= Item(user_id=1, name="Glove", description="""A baseball glove or mitt \
is a large leather glove worn by baseball players of the defending team which \
assist players in catching and fielding balls hit by a batter or thrown by a \
teammate. By convention, the type of glove that fits on the left hand is \
called a "right-handed" or "RH" glove. Some websites and catalogs refer to \
these gloves as "Right-Hand Throw" gloves, meaning the glove is worn on the \
left hand. Conversely, a "left-handed" glove is worn on the right hand, \
allowing the player to throw the ball with their left hand""",\
category=category3)

session.add(Item7)
session.commit()

# add 4th category item 
category4 = Category(user_id=1, name="Frisbee")

session.add(category4)
session.commit()

#add frisbee items

Item8= Item(user_id=1, name="Ulimtate", description="""Ultimate, originally \
known as ultimate frisbee, is a non-contact team field sport played with a \
flying disc. Points are scored by passing the disc to a teammate in the \
opposing end zone. Other basic rules are that players must not take steps \
while holding the disc, and interceptions, incomplete passes, and passes out \
of bounds are turnovers. Rain, wind, or occasionally other adversities can \
make for a testing match with rapid turnovers, heightening the \
pressure of play.""",category=category4)

session.add(Item8)
session.commit()

Item9= Item(user_id=1, name="Frisbee history", description="""Team flying disc \
games using pie tins and cake pan lids were part of Amherst College student \
culture for decades before plastic discs were available. A similar two-hand \
touch football-based game was played at Kenyon College in Ohio starting in 
1942.From 1965 or 1966 Jared Kass and fellow Amherst students Bob Fein, \
Richard Jacobson, Robert Marblestone, Steve Ward, Fred Hoxie, Gordon Murray,\
and others evolved a team frisbee game based on concepts from American /
football, basketball, and soccer. This game had some of the basics of modern \
ultimate including scoring by passing over a goal line, advancing the disc by 
passing, no travelling with the disc, and turnovers on interception or 
incomplete pass. Jared, an instructor and dorm advisor, taught this game to \
high school student Joel Silver during the summer of 1967 or 1968 at Mount \
Hermon Prep school summer camp""",category=category4)

session.add(Item9)
session.commit()

# add 5th category item 
category5 = Category(user_id=1, name="Snowboarding")

session.add(category5)
session.commit()

Item10= Item(user_id=1, name="The Snowboard", description="""Snowboards are \
boards that are usually the width of one's foot longways, with the ability to \
glide on snow.[1] Snowboards are differentiated from monoskis by the stance of \
the user. In monoskiing, the user stands with feet inline with direction of \
travel (facing tip of monoski/downhill) (parallel to long axis of board), \
whereas in snowboarding, users stand with feet transverse (more or less) to \
the longitude of the board. Users of such equipment may be referred to as \
snowboarders. Commercial snowboards generally require extra equipment such \
as bindings and special boots which help secure both feet of a snowboarder, \
who generally rides in an upright position.[1] These types of boards are \
commonly used by people at ski hills or resorts for leisure, entertainment, \
and competitive purposes in the activity called snowboarding.""",
category=category5)

session.add(Item10)
session.commit()

Item11= Item(user_id=1, name="Bindings", description="""Bindings are separate \
components from the snowboard deck and are very important parts of the total \
snowboard interface. The bindings' main function is to hold the rider's boot \
in place tightly to transfer their energy to the board. Most bindings are \
attached to the board with three or four screws that are placed in the center \
of the binding. Although a rather new technology from Burton called Infinite \
channel system[13] uses two screws, both on the outsides of the binding.\
There are several types of bindings. Strap-in, step-in, and hybrid bindings \
are used by most recreational riders and all freestyle riders.""",
category=category5)

session.add(Item11)
session.commit()


# add 6th category item 
category6 = Category(user_id=1, name="Rock Climbing")

session.add(category6)
session.commit()

#add rocking climbing items 

Item12= Item(user_id=1, name="Harness", description="""A climbing harness is \
an item of climbing equipment for rock-climbing, abseiling, or other \
activities requiring the use of ropes to provide access or safety such as \
industrial rope access, working at heights, etc. A harness secures a person \
to a rope or an anchor point.In its simplest form, a harness can be made from \
a length of rope or a nylon webbing tied round the waist. More sophisticated\
harnesses exist in many patterns, designed to give greater comfort and \
security, and more options for carrying equipment. While harnesses can be \
improvised, it is more common to use commercially produced harnesses, which \
often include padding and amenities such as gear loops. Most commercial \
climbing harnesses meet the guidelines and manufacturing standards of \
organizations such as the Union Internationale des Associations d'Alpinisme \
or European Committee for Standardization. More expensive harnesses are not \
necessarily better, as different types of harnesses are better suited to \
different body types and activities, regardless of price range..""",
category=category6)

session.add(Item12)
session.commit()

Item13= Item(user_id=1, name="Belay gloves", description="""A belay glove is a \
glove constructed from either leather or a synthetic substitute, is used to \
protect the hands when belaying, and is especially useful if using a classic \
or body belay. They are also very useful for controlling the belay with \
single, lead ropes that are 9.5mm or smaller.[9] Ultimately, belay gloves can \
lessen the possibility of rope burn and the subsequent involuntary release\
of the rope.""",category=category6)

session.add(Item13)
session.commit()



print "added Category items!"
