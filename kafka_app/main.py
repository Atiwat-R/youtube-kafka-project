import sys
from config import config
from youtube_api import get_playlist_items, get_videos
from kafka_producer import get_producer, on_delivery
    

def main():
    google_api_key = config["google_api_key"]
    youtube_playlist_id = config["youtube_playlist_id"]
    producer = get_producer()

    for item in get_playlist_items(google_api_key, youtube_playlist_id):
        video_id = item["contentDetails"]["videoId"]
        for video in get_videos(google_api_key, video_id, page_token=None):

            # print(pprint.pformat(summarize_video(video)))

            # Produce (upload) to Confluent Kafka topic
            producer.produce(
                topic = "youtube_videos",
                key = video_id,
                value = {
                    "TITLE": video.get("snippet", {}).get("title"),
                    "VIEWS": int(video.get("statistics", {}).get("viewCount")),
                    "LIKES": int(video.get("statistics", {}).get("likeCount")),
                    "COMMENTS": int(video.get("statistics", {}).get("commentCount")),
                },
                on_delivery = on_delivery
            )
    producer.flush()        


if __name__ == "__main__":
    sys.exit(main())



# poetry shell
# poetry run python3 main.py
