from moviepy.editor import VideoFileClip, ImageSequenceClip

video_path = "K:/INTERNSHIP PROJECTS/LET'S GROW MORE/TASK-1 GIF CREATOR/video.mp4"  # Replace with your actual path
output_path = "K:/INTERNSHIP PROJECTS/LET'S GROW MORE/TASK-1 GIF CREATOR/output.gif"  # Customize the output filename

start_time = 1  # Set the starting time in seconds (optional)
end_time = 20  # Set the ending time in seconds (optional)
fps = 10  # Set the desired frame rate

try:
    clip = VideoFileClip(video_path)
    if start_time and end_time:
        clip = clip.subclip(start_time, end_time)
    clip = clip.set_fps(fps)
    clip.write_gif(output_path)
    print(f"GIF created successfully at {output_path}")
except Exception as e:
    print(f"Error creating GIF: {e}")
