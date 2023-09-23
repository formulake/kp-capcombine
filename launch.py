import gradio as gr
import os

def combine_files(blip_path, wd14_path):
    # Ensure both directories exist
    if not os.path.exists(blip_path) or not os.path.exists(wd14_path):
        return "One or both directories do not exist."

    # Create Captions directory if it doesn't exist
    captions_dir = os.path.join(os.path.dirname(blip_path), "Captions")
    if not os.path.exists(captions_dir):
        os.makedirs(captions_dir)

    # Iterate through files in BLIP directory
    for filename in os.listdir(blip_path):
        if filename.endswith(".txt"):
            blip_file_path = os.path.join(blip_path, filename)
            wd14_file_path = os.path.join(wd14_path, filename)

            # Ensure the file exists in both directories
            if os.path.exists(wd14_file_path):
                with open(blip_file_path, 'r') as blip_file, open(wd14_file_path, 'r') as wd14_file:
                    blip_content = blip_file.read()
                    wd14_content = wd14_file.read()

                    blip_content = blip_content.rstrip()  # Remove any trailing whitespace or newlines

                    # Check if BLIP content ends with a comma or full stop
                    if not blip_content[-1] in [",", "."]:
                        blip_content += ","

                    combined_content = blip_content + " " + wd14_content


                # Save combined content to Captions directory
                with open(os.path.join(captions_dir, filename), 'w') as combined_file:
                    combined_file.write(combined_content)

    return "Files combined successfully!"


def main():
    interface = gr.Interface(
        fn=combine_files,
        inputs=[gr.Textbox(label="BLIP Folder Path"), gr.Textbox(label="WD14 Folder Path")],
        outputs="text",
        live=False
    )
    interface.launch(server_port=7875)

if __name__ == "__main__":
    main()
