# 🌋 LavaSR
<p align="center">
  <a href="https://huggingface.co/YatharthS/LavaSR">
    <img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-FFD21E" alt="Hugging Face Model">
  </a>
  &nbsp;
  <a href="https://huggingface.co/spaces/YatharthS/LavaSR">
    <img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-blue" alt="Hugging Face Space">
  </a>
  &nbsp;
  <a href="https://colab.research.google.com/drive/17wzpZ1nH_BrDsSfZ0JiZNdf4OH-zsfs2?usp=sharing">
    <img src="https://img.shields.io/badge/Colab-Notebook-F9AB00?logo=googlecolab&logoColor=white" alt="Colab Notebook">
  </a>
</p>


LavaSR is a lightweight and high quality speech enhancement model that enhances low quality audio with noise into clean crisp audio with speeds reaching roughly 5000x realtime on GPU and over 60x realtime on CPU.

**LavaSR v2 just released**: Massive increase in quality and speed, surpassing 6gb slow diffusion models. Check it out!

https://github.com/user-attachments/assets/1d11ae30-cb19-4c9b-ac46-52adbcac957f

## Main features
- Extremely fast: Reaches speeds over 5000x realtime on GPUs and 50x realtime on CPUs
- High quality: Quality surpasses diffusion models.
- Efficency: Just uses 500mb vram and potentially less.
- Universal input: Supports any input sampling rate from 8khz to 48khz.

### Why is this useful?
* Enhancing TTS: LavaSR can enhance TTS(text-to-speech) model quality considerably with nearly 0 computational cost.
* Real-time enhancement: LavaSR allows for on device enhancement of any low quality calls, audio, etc. while using little memory.
* Restoring datasets: LavaSR can enhance audio quality of any audio dataset.



LavaSR Audio Enhancer - Setup Guide for Windows


1. ACTIVATE VIRTUAL ENVIRONMENT
   ------------------------------
   cd C:\LavaSR
   
   .venv\Scripts\activate

   
3. INSTALL DEPENDENCIES
   ---------------------
   pip install git+https://github.com/ysharma3501/LavaSR.git
   
   pip install gradio soundfile


5. (OPTIONAL) ENABLE CUDA FOR NVIDIA GPU
   --------------------------------------
   Only if you have an NVIDIA GPU and want faster processing:

   a) Check CUDA availability:
      nvidia-smi

   b) Reinstall PyTorch with CUDA support:
      pip uninstall torch torchvision torchaudio -y
      pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

      (Replace cu124 with your CUDA version: cu118, cu121, cu124, etc.)


6. RUN THE INTERFACE
   ------------------
   python interface.py

   Then open your browser to: http://127.0.0.1:7860



USAGE


1. Upload an audio file (or record via microphone)
2. Select device: cpu, cuda (NVIDIA), or mps (Apple Silicon)
3. Adjust sample rate (8000-48000 Hz)
4. Toggle Denoise if audio has background noise
5. Toggle Batch Mode for very long audio files
6. Click "Enhance Audio"
7. Download the enhanced output



TROUBLESHOOTING


- "Torch not compiled with CUDA enabled" 
  -> Install PyTorch with CUDA (see step 3)

- ModuleNotFoundError: No module named 'gradio'
  -> Run: pip install gradio



Stars/Likes would be appreciated, thank you.
  
