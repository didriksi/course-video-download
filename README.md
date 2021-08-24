# course-video-download
Download video lectures from a UiO course.

To use it, install packages with `pip install -r requirements.txt`, then run `scrape_for_courses.py` to find data on all courses. This can take some time. Afterwards, run `main.py` with the courses you want to download lectures from as arguments. For example, like this: `python main.py STK1110 MAT3110`. It is barely tested, and probably has lots of errors. It also only downloads videos from the fall of 2020, but this can be easily changed.