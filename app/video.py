# import os
# import google.generativeai as genai
# import moviepy.editor as mp
# # from .utils import save_generated_file
# import sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from app.utils import save_generated_file


# def generate_video(product_image, offer, theme, color_palette, size, duration):
#     genai.configure(api_key='YOUR_GEMINI_API_KEY')

#     prompt = f"Create a promotional video concept for {product_image} with the offer: {offer}. Theme: {theme}. Use the color palette: {', '.join(color_palette)}. The video size should be {size[0]}x{size[1]} pixels and duration {duration} seconds."

#     model = genai.GenerativeModel('gemini-pro-vision')
#     response = model.generate_content(prompt)

#     # Here you would interpret the AI's response and create a video
#     # This is a placeholder implementation
#     clip = mp.ColorClip(size, color=color_palette[0], duration=duration)
#     text_clip = mp.TextClip(offer, fontsize=36, color=color_palette[1], size=size)
#     text_clip = text_clip.set_pos('center').set_duration(duration)

#     video = mp.CompositeVideoClip([clip, text_clip])
#     video_filename = f"video_{os.path.basename(product_image)}.mp4"
#     video_path = save_generated_file(video.write_videofile, video_filename, 'video')

#     return video_path
