# course-video-download
Download video lectures from a UiO course.

To use it, install packages with `pip install -r requirements.txt`, then run `scrape_for_courses.py` to find data on all courses. This takes roughly a minute.

Afterwards, run `main.py` with the courses you want to download lectures from as arguments. For example, like this: `python main.py STK1110 MAT3110`. It is barely tested, and probably has lots of errors. By default, it downloads videos from the fall of 2020, and in the folder `forelesningsvideoer`. This is the folder most lectures end up in. If you want to download from another semester you can add the semester name as a first command line argument, prepended by `semester=`. The semester name is on the format `<either 'h' or 'v' for fall or spring><last two digits of year>`. So, if you want to download videos from STK1100, which is a spring subject, use `python main.py semester=v20 STK1100`. If you want to download videos from another folder, write the folder name prepended by `folder=`. So, to download videos from MAT1140, which have put most of their regular lectures in the folder `forelesninger`, run `python main.py folder=forelesninger MAT1140`.
