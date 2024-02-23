import json
import requests


# Helpers

# Get a page from playlist (one page contains items aka videos in playlist. There can be many pages to fill out a playlist)
def get_playlist_items_page(google_api_key, youtube_playlist_id, page_token=None):
    response = requests.get("https://www.googleapis.com/youtube/v3/playlistItems", params={
        "key": google_api_key,
        "playlistId": youtube_playlist_id,
        "part": "contentDetails",
        "pageToken": page_token
    }) 
    playlistPage = json.loads(response.text)
    return playlistPage

# Get a page of videos
def get_videos_page(google_api_key, youtube_video_id, page_token=None):
    response = requests.get("https://www.googleapis.com/youtube/v3/videos", params={
        "key": google_api_key,
        "id": youtube_video_id,
        "part": "snippet,statistics",
        "pageToken": page_token
    }) 
    videoPage = json.loads(response.text)
    return videoPage

# For debugging
def summarize_video(video):
    summary = {
        "video_id": video.get("id"),
        "title": video.get("snippet", {}).get("title"),
        "views": int(video.get("statistics", {}).get("viewCount")),
        "likes": int(video.get("statistics", {}).get("likeCount")),
        "comments": int(video.get("statistics", {}).get("commentCount")),
    }
    return summary


# Exports

# Gets ALL items from ALL page in playlist
# Using Python generator (yield from) turns this function into an iterable
def get_playlist_items(google_api_key, youtube_playlist_id, page_token=None):

    page = get_playlist_items_page(google_api_key, youtube_playlist_id, page_token)
    yield from page["items"]

    next_page_token = page.get("nextPageToken") 
    if next_page_token is not None:
        yield from get_playlist_items(google_api_key, youtube_playlist_id, page_token=next_page_token)

# Gets ALL videos from ALL page 
# Using Python generator (yield from) turns this function into an iterable
def get_videos(google_api_key, youtube_video_id, page_token=None):

    page = get_videos_page(google_api_key, youtube_video_id, page_token)
    yield from page["items"]

    next_page_token = page.get("nextPageToken") 
    if next_page_token is not None:
        yield from get_videos_page(google_api_key, youtube_video_id, page_token=next_page_token)








