from manim import *
from Animation import *
from automate import PROJECT_NUMBER, HEADING

set_background_color(BG_COLOR)
set_media_directory()
set_num_cache_files()
resolution = set_resolution("1080p")


THUMBNAIL_PATH, TEASER_PATH, INTRODUCTION_PATH, SOLUTION_PATH, OUTRO_PATH = (
    get_path_to_save_location(resolution)
)


video_files = [
    "teaser.mp4",
    "introduction.mp4",
    "solution_01.mp4",
    "solution_02.mp4",
    "solution_03.mp4",
    "solution_04.mp4",
    "outro.mp4",
]


project_dir = create_new_project_directory(PROJECT_DIRECTORY, PROJECT_NUMBER)


choice = {
    "Thumbnail": (
        Thumbnail,
        [HEADING, MARKDOWN_01],
        THUMBNAIL_PATH,
        project_dir,
        "thumbnail.png",
    ),
    "Teaser": (Teaser, [MARKDOWN_01], TEASER_PATH, project_dir, "teaser.mp4"),
    "Introduction": (
        Introduction,
        [],
        INTRODUCTION_PATH,
        project_dir,
        "introduction.mp4",
    ),
    "Solution 1": (
        Solution,
        [MARKDOWN_01],
        SOLUTION_PATH,
        project_dir,
        "solution_01.mp4",
    ),
    "Solution 2": (
        Solution,
        [MARKDOWN_02],
        SOLUTION_PATH,
        project_dir,
        "solution_02.mp4",
    ),
    "Solution 3": (
        Solution,
        [MARKDOWN_03],
        SOLUTION_PATH,
        project_dir,
        "solution_03.mp4",
    ),
    "Solution 4": (
        Solution,
        [MARKDOWN_04],
        SOLUTION_PATH,
        project_dir,
        "solution_04.mp4",
    ),
    "Outro": (Outro, [], OUTRO_PATH, project_dir, "outro.mp4"),
}


def main(action):
    if action == "Thumbnail":
        render_scene(*choice["Thumbnail"])
    elif action == "Teaser":
        render_scene(*choice["Teaser"])
    elif action == "Introduction":
        render_scene(*choice["Introduction"])
    elif action == "Solution_1":
        render_scene(*choice["Solution 1"])
    elif action == "Solution_2":
        render_scene(*choice["Solution 2"])
    elif action == "Solution_3":
        render_scene(*choice["Solution 3"])
    elif action == "Solution_4":
        render_scene(*choice["Solution 4"])
    elif action == "Outro":
        render_scene(*choice["Outro"])
    elif action == "stitch":
        stitch_videos(video_files, project_dir, MUSIC_DIRECTORY)
    else:
        print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <action>")
        sys.exit(1)

    action = sys.argv[1]
    main(action)
