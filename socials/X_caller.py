import tweepy
import os
from dotenv import load_dotenv
load_dotenv()



def text_breaker(text, max_length=276): #general function to break text into chunks MADE BY AI TO CHECK!!!!!
    words = text.split()
    chunks = []
    current_chunk = "\\1 "

    for word in words:
        if len(current_chunk) + len(word) + 1 <= max_length:
            if current_chunk:
                current_chunk += " "
            current_chunk += word
        else:
            chunks.append(current_chunk)
            current_chunk = f"\\{len(chunks)+1} {word}"

    if current_chunk:
        chunks.append(current_chunk)
    return chunks


def x_former_tweet(text, image_directory=None):
    try:
        auth = tweepy.OAuthHandler(os.getenv('X_API_consumer_key'), os.getenv('X_API_consumer_secret'))
        auth.set_access_token(os.getenv('X_consumer_token'), os.getenv('X_consumer_token_secret'))
        api = tweepy.API(auth)
        if image_directory != None:
            media = api.media_upload(image_directory)
            image_directory = [media.media_id]


        client = tweepy.Client(consumer_key=os.getenv('X_API_consumer_key'),
                               consumer_secret=os.getenv('X_API_consumer_secret'),
                               access_token=os.getenv('X_consumer_token'),
                               access_token_secret=os.getenv('X_consumer_token_secret'))
        if len(text) >= 280:
            text_chunks = text_breaker(text)
            tweet = client.create_tweet(text=text_chunks[0],media_ids=image_directory)
            for number_of_messeage in range(1, len(text_chunks)):
                client.create_tweet(text=text_chunks[number_of_messeage],
                                    in_reply_to_tweet_id=tweet.data['id'])


            return tweet.data['id']
        else:
            tweet = client.create_tweet(text=text, media_ids=image_directory)
            return tweet.data['id']
        return None

    except tweepy.Unauthorized as error:
        print("Invalid or expired token. Please check your credentials.")
        print("X Posting Failed!")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("X Posting Failed!")


if __name__ == "__main__":
    text = "Shotguns are brutal and effective at close range. They can stop a threat quickly, by brutal 1 shot with multiple shots. But is not perfect, when hostages comes into play, unless we load with slugs. Slugs changes use of this weapon a lot, still maintaining the same manual, making a shotgun very versitalie weapon."
    image_directory = "/home/pl_chochlikman/Pulpit główny/Kickstarterowe/strzelba.jpg"
    x_former_tweet(text, image_directory)


