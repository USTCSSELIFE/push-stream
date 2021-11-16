import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--video-url", type=str, required=True, help="Video URL")
parser.add_argument("--rtmp-address", type=str,
                    required=True, help="RTMP Address")
parser.add_argument("--stream-loop", dest="loop",
                    help="Stream Loop", action="store_true")
parser.add_argument("--no-stream-loop", dest="loop",
                    help="No Stream Loop", action="store_false")


args = parser.parse_args()

loop = -1 if args.loop else 0

ffmpeg_command = f"ffmpeg -re -stream_loop {loop} -i {args.video_url} -vcodec libx264 -acodec aac -f flv {args.rtmp_address}"

os.system(ffmpeg_command)
