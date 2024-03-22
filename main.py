from moviepy.editor import VideoFileClip
import os
import uuid

def extract_frames(movie, interval, imgdir):
    if not os.path.exists(imgdir):
        os.makedirs(imgdir)

    clip = VideoFileClip(movie)
    duration = clip.duration
    times = [t for t in range(0, int(duration), interval)]
    for t in times:
        unique_id = str(uuid.uuid4())[:8]  # Generate a random unique ID
        imgpath = os.path.join(imgdir, '{}.png'.format(unique_id))
        clip.save_frame(imgpath, t)


movie = r"C:\Users\sinan\Desktop\videos\VID-20240321-WA0001.mp4" # Use raw string or escape backslashes
imgdir = r"C:\Users\sinan\Desktop\frames"
interval = 1  # Interval in seconds
extract_frames(movie, interval, imgdir)
