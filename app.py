import gradio as gr
from PIL import Image


def process_image(image: Image.Image | None, grayscale: bool, rotation: int) -> Image.Image | None:
    if image is None:
        return None

    processed_image = image
    if grayscale:
        processed_image = processed_image.convert("L")
    if rotation:
        processed_image = processed_image.rotate(rotation, expand=True)

    return processed_image


with gr.Blocks(title="Quick Image Studio") as demo:
    gr.Markdown("# Quick Image Studio")

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(label="Upload an image", type="pil")
            grayscale_input = gr.Checkbox(label="Convert to grayscale")
            rotation_input = gr.Slider(
                minimum=0,
                maximum=270,
                step=90,
                value=0,
                label="Rotation",
            )
            process_button = gr.Button("Process", variant="primary")
        with gr.Column():
            image_output = gr.Image(label="Processed image", type="pil")

    process_button.click(
        fn=process_image,
        inputs=[image_input, grayscale_input, rotation_input],
        outputs=image_output,
    )


if __name__ == "__main__":
    demo.launch()
