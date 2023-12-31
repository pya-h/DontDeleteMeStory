from reportlab.pdfgen import canvas

def read_story(story_filename):
    try:
        file = open(story_filename, 'r')
        return file.read()
    except:
        raise Exception("Error while trying to read the story. the process cannot continue.")


def generate_story(file_path, content):
    try:
        pdf = canvas.Canvas(file_path)
        x_middle = image_height = 200
        image_width = 400
        pdf.setFontSize(20)
        pdf.drawString(x_middle, 500, "Don't Delete Me")
        pdf.showPage()

        for (episode, image_path) in content:
            y = 700
            # write episode
            # seperating episode text lines and removing empty strings
            lines = list(filter(lambda x: x, [x for x in episode.split("\n")]))
            for line in lines:
                space_below = 15
                if "**" in line:  # episode title
                    pdf.setFontSize(14)
                    line = line.replace("**", "")
                    space_below = 25
                else:  # episode text
                    pdf.setFontSize(10)
                pdf.drawString(50, y, line)
                y -= space_below
            # positioning the image
            y -= image_height + 100
            # Draw episode image
            pdf.drawImage(image_path, x=100, y=y, width=image_width, height=image_height)
            y -= 15
            # Draw image description
            pdf.drawString(x_middle, y, lines[0].replace("**", ""))

            pdf.showPage()

        pdf.save()
    except Exception as ex:
        raise ex


if __name__ == '__main__':
    try:
        episodes = read_story('story.txt').split('--------------------')
        content = []
        # putting each episode and its image in a tupple
        for i, episode in enumerate(episodes, start=1):
            content.append((episode, f"./images/{i}.jpeg"))

        output = "story.pdf"
        generate_story(output, content)
        print(f"Done! Read the story in: {output}")
    except Exception as ex:
        print("Story cannot be generated because: ", str(ex))
