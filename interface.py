import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import gradio as gr
import soundfile as sf
import torch
from LavaSR.model import LavaEnhance2

## Global model reference
lava_model = None
current_device = None

def load_model(device):
    """Load or reload the model on specified device."""
    global lava_model, current_device
    if current_device != device or lava_model is None:
        lava_model = LavaEnhance2("YatharthS/LavaSR", device)
        current_device = device
    return lava_model

def enhance_audio(audio_file, input_sr, denoise, batch, device):
    """Process audio file and return enhanced version."""
    try:
        model = load_model(device)
        
        ## Load Audio
        input_audio, sr = model.load_audio(audio_file, input_sr=input_sr)
        
        ## Enhance Audio
        output_audio = model.enhance(
            input_audio, 
            denoise=denoise, 
            batch=batch
        ).cpu().numpy().squeeze()
        
        ## Save output
        output_path = "output.wav"
        sf.write(output_path, output_audio, 48000)
        
        return output_path, "Success!"
    except Exception as e:
        return None, f"Error: {str(e)}"

with gr.Blocks(title="LavaSR Audio Enhancer") as demo:
    gr.Markdown("# 🎵 LavaSR Audio Enhancer")
    gr.Markdown("Upload an audio file to enhance its quality using AI.")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Input")
            audio_input = gr.Audio(label="Upload Audio", type="filepath")
            device_dropdown = gr.Dropdown(
                choices=["cpu", "cuda", "mps"],
                value="cpu",
                label="Device"
            )
            input_sr = gr.Slider(
                minimum=8000, 
                maximum=48000, 
                value=16000, 
                step=1000,
                label="Input Sample Rate (Hz)"
            )
            denoise = gr.Checkbox(label="Denoise (filter noise)", value=False)
            batch = gr.Checkbox(label="Batch Mode (for long audio)", value=False)
            
            process_btn = gr.Button("🚀 Enhance Audio", variant="primary")
        
        with gr.Column():
            gr.Markdown("### Output")
            audio_output = gr.Audio(label="Enhanced Audio")
            status_text = gr.Textbox(label="Status")
    
    process_btn.click(
        fn=enhance_audio,
        inputs=[audio_input, input_sr, denoise, batch, device_dropdown],
        outputs=[audio_output, status_text]
    )

if __name__ == "__main__":
    demo.launch()
