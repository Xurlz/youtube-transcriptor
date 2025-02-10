#! /usr/bin/env python

from youtube_transcript_api import YouTubeTranscriptApi
from sys import stdin

def get_transcript(video_id,languages):
    transcript = YouTubeTranscriptApi.get_transcript(video_id,languages)
    text = ' '.join([d['text'] for d in transcript])
    return text

video_id = stdin.read()
languages = ["pt"]

print(get_transcript(video_id,languages))

