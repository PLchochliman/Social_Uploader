from socials.X_caller import x_former_tweet
from socials.FB_caller import FB_uploader

#import sheluder


#text = "Shotgun is most versitile weapon. It may use buckshots, slugs, and make different damage on 100m. In real life shooting them is fun and exiting, that's why in TriggerDiscipline, by changing ammo, you change a lot of rules, from to hit, to wounds."
#filepath = "/home/pl_chochlikman/Pulpit główny/Kickstarterowe/strzelba.jpg"

text = "It doesn't metter which specialisation you've chosen, you'll need a equipment. Bullet from any gun is much faster than first fist of the world. And your body is not bulletproof. But vests has some minuses, so choose wisely. As bigger it gets, more minuses come into play."
directory_of_image = "/home/pl_chochlikman/Pulpit główny/Kickstarterowe/sprzęt.jpg"


FB_uploader(text,directory_of_image)
x_former_tweet(text,directory_of_image)

