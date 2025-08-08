import requests
import gradio as gr
from src.utils.common import API_URL, PORT 
from shared_lib.logger import logger


def add_and_refresh(item):
    requests.post(f"{API_URL}/items", json={"item": item})
    r = requests.get(f"{API_URL}/items")
    return r.json()


with gr.Blocks() as app:
    gr.Markdown("# Web App (Gradio Frontend)")
    inp = gr.Textbox(label="Enter item")
    btn = gr.Button("Add")
    out = gr.JSON(label="Current items")

    btn.click(fn=add_and_refresh, inputs=inp, outputs=out)


if __name__ == "__main__":
    logger.info(f"Starting Gradio app on port {PORT}")
    app.launch(server_name="0.0.0.0", server_port=PORT)
