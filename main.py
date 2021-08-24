"""Command line interface for downloading video lectures from courses.
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import wget
import sys
import os

from scrape_for_courses import make_soup

def make_soup(url):
    """Makes bs4.BeautifulSoup instance of content of url.

    :param url: url to make bs4.BeautifulSoup instance from.
    
    :return: bs4.BeautifulSoup instance of content of url.
    """
    coursepage = requests.get(url)
    coursecontent = coursepage.content
    return BeautifulSoup(coursecontent, 'html.parser')

def main(courses):
    course_df = pd.read_pickle('courses.pkl')
    course_df.set_index('coursecode', drop=False, inplace=True)

    for course in courses:
        if course not in course_df.index:
            print(f"WARNING: `{course}` is not a valid course.")
            continue

        print(f"Finding videos in `{course}`...")

        url = "https://www.uio.no/studier/emner/" + \
              course_df.at[course, 'faculty'] + "/" + \
              course_df.at[course, 'institute'] + "/" + course + "/" + \
              "/h20/forelesningsvideoer/"
        soup = make_soup(url)

        container = soup.find("div", attrs={"class", "vrtx-image-listing-container"})
        video_a_tags = container.find_all("a", attrs={"class", "vrtx-title"})

        print(f"Found {len(video_a_tags)} videos, downloading them now...")

        try:
            os.mkdir(course)
        except FileExistsError:
            print("Have already downloaded videos from this course, "
                  "overwriting old downloads.")

        for tag in video_a_tags:
            url = tag.get("href").replace("?vrtx=view-as-webpage", "")
            if ".mp4" not in url:
                print(f"WARNING: {tag.string} is not a .mp4 file")
                continue
            path = f"{course}/{tag.string}.mp4"

            wget.download(url, path)

if __name__ == "__main__":
    courses = sys.argv[1:]
    main(courses)
