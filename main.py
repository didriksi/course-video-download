"""Command line interface for downloading video lectures from courses.
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import wget
import sys
import os

from scrape_for_courses import make_soup

DEFAULT_SEMESTER = "h20"
DEFAULT_VIDEO_FOLDER = "forelesningsvideoer"

def download_lectures(semester, courses):
    """Download lecture videos for courses in the courses list.

    :param semester: String, of the format `h|v[0-9]{2}`
    :param courses: String, matching courses offered at UiO.
    """
    course_df = pd.read_pickle('courses.pkl')
    course_df.set_index('coursecode', drop=False, inplace=True)

    semester = semester.lower()

    for course in courses:
        course = course.upper()
        if course not in course_df.index:
            print(f"WARNING: `{course}` does not exist.")
            continue

        print(f"Finding videos in course `{course}`...")

        url = "https://www.uio.no/studier/emner/" + \
              course_df.at[course, 'faculty'] + "/" + \
              course_df.at[course, 'institute'] + "/" + course + "/" + \
              "/" + semester + "/forelesningsvideoer/"
        soup = make_soup(url)

        container = soup.find("div",
                              attrs={"class", "vrtx-image-listing-container"})
        if container is None:
            print(f"WARNING: Course {course} exists, but has no "
                   "lectures in this semester.")
            continue

        video_a_tags = container.find_all("a", attrs={"class", "vrtx-title"})

        print(f"Found {len(video_a_tags)} videos, downloading them now...")

        try:
            os.mkdir(course)
        except FileExistsError:
            print("Have already downloaded videos from this course, "
                  "overwriting old downloads.")

        for i, tag in enumerate(video_a_tags):
            url = tag.get("href").replace("?vrtx=view-as-webpage", "")
            if ".mp4" not in url:
                print(f"WARNING: {tag.string} is not a .mp4 file")
                continue
            path = f"{course}/{tag.string}.mp4"

            print(f"Downloading video number {i + 1}/{len(video_a_tags)}: ")

            wget.download(url, path)

            print("")

def main():
    for arg in sys.argv[1:]:
        courses = []
        video_folder = DEFAULT_VIDEO_FOLDER
        semester = DEFAULT_SEMESTER

        if arg.startswith("folder="):
            video_folder = arg[7:]
        elif arg.startswith("semester="):
            semester = arg[9:]
        else:
            courses.append(arg)

    download_lectures(semester, courses)

if __name__ == "__main__":
    main()
