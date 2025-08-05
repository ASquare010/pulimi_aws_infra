import gradio as gr
import requests

API_URL = "http://management_api:5000/items"

def add_and_refresh(item):
    # Add item
    requests.post(API_URL, json={"item": item})
    # Get updated list
    r = requests.get(API_URL)
    return r.json()

with gr.Blocks() as demo:
    gr.Markdown("# Web App (Gradio Frontend)")
    inp = gr.Textbox(label="Enter item")
    btn = gr.Button("Add")
    out = gr.JSON(label="Current items")

    btn.click(fn=add_and_refresh, inputs=inp, outputs=out)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
