from googleapiclient.discovery import build

import json

import os
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
VIDEO_ID = "gnidng0mxZI"


def video_comments(video_id):
    comments = []

    # creating YouTube resource object
    youtube = build('youtube', 'v3',
                    developerKey=YOUTUBE_API_KEY)

    # retrieve YouTube video results
    video_response = youtube.commentThreads().list(
        part='snippet,replies',
        videoId=video_id
    ).execute()

    # iterate video response
    while video_response:

        # extracting required info
        # from each result object
        for item in video_response['items']:
            # Extracting comments
            comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
            comment_author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']

            comments.append((comment_author, comment))

        # Again repeat
        if 'nextPageToken' in video_response:
            video_response = youtube.commentThreads().list(
                part='snippet,replies',
                videoId=video_id,
                pageToken=video_response['nextPageToken']
            ).execute()
        else:
            break

    return comments


def write_to_json_file(comments):
    json_string = json.dumps(comments)

    # Using a JSON string
    with open('comments.json', 'w') as outfile:
        outfile.write(json_string)


comments = video_comments(VIDEO_ID)
write_to_json_file(comments)

