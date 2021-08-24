# course-video-download
Download video lectures from a UiO course.

To use it, install packages with `pip install -r requirements.txt`, then run `scrape_for_courses.py` to find data on all courses. This takes roughly a minute.

Afterwards, run `main.py` with the courses you want to download lectures from as arguments. For example, like this: `python main.py STK1110 MAT3110`. It is barely tested, and probably has lots of errors. By default, it downloads videos from the fall of 2020, but if you want to download from another semester you can add the semester name as a first command line argument. The semester name is on the format `<either 'h' or 'v' for fall or spring><last two digits of year>`. So, if you want to download videos from STK1100, which is a spring subject, use `python main.py v20 STK1100`.
