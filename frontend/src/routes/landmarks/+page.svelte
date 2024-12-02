<script>
    import { onMount } from 'svelte';
    import { GradientButton, Label, Select, Spinner } from 'flowbite-svelte';
    
    let source_lang_val = null;
    let target_lang_val = "en";
  
    let savedImage = null;
    let isCameraOpen = false;
    let isPhotoCaptured = false;
    let capturedPhoto = null;
    let stream = null;
    let videoSource;
    let loading = false;
    let hasData = false;
    let landmarkData = {
      cultural_significance : ""
    };
    const dropHandle = (event) => {
    event.preventDefault();
    const files = event.dataTransfer?.files || event.target?.files;
  
    if (files && files.length > 0) {
      const reader = new FileReader();
      reader.onload = async (e) => {
        savedImage = e.target.result;
  
        // Send the uploaded image to the backend
        await sendImageToBackend(savedImage);
      };
      reader.readAsDataURL(files[0]);
    }
  };
  
    const openCamera = async () => {
      try {
        isCameraOpen = true;
        isPhotoCaptured = false;
        capturedPhoto = null;
        stream = await navigator.mediaDevices.getUserMedia({ video: true });
        if (videoSource) {
          videoSource.srcObject = stream;
          videoSource.play();
        }
      } catch (error) {
        console.error('Camera access denied:', error);
      }
    };
  
    const capturePhoto = () => {
    if (!videoSource) return;
  
    const canvas = document.createElement('canvas');
    canvas.width = videoSource.videoWidth;
    canvas.height = videoSource.videoHeight;
  
    const ctx = canvas.getContext('2d');
    ctx.drawImage(videoSource, 0, 0, canvas.width, canvas.height);
  
    capturedPhoto = canvas.toDataURL('image/png');
    isPhotoCaptured = true;
  
    // Pause the video feed
    videoSource.pause();
  };
  
    const retakePhoto = () => {
      capturedPhoto = null;
      isPhotoCaptured = false;
      videoSource.play();
    };
  
    const submitPhoto = async () => {
    if (capturedPhoto) {
      savedImage = capturedPhoto;
      closeCamera();
  
      // Send the captured photo to the backend
      await sendImageToBackend(savedImage);
    }
  };
  
    const closeCamera = () => {
      if (stream) {
        stream.getTracks().forEach((track) => track.stop());
        stream = null;
      }
      isCameraOpen = false;
    };
  
    const removeImage = () => {
      savedImage = null;
      hasData = false;
    };
  
    const sendImageToBackend = async (imageData) => {
    loading = true; // Start spinner
    try {
      const response = await fetch('http://localhost:5000/api/landmark', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          image: imageData,       // Required field
        }),
      });
  
      if (response.ok) {
        const data = await response.json();
        console.log('Backend response:', data);
        landmarkData.cultural_significance = data.transaction.cultural_significance;
        hasData = true;
        return data;
      } else {
        console.error('Error sending image to backend:', response.statusText);
      }
    } catch (error) {
      console.error('Error during backend call:', error);
    } finally {
      loading = false; // Stop spinner
    }
  };
  
    onMount(() => {
      // Optional cleanup if necessary
      return () => {
        if (stream) {
          stream.getTracks().forEach((track) => track.stop());
        }
      };
    });
    
  </script>
  
  <div class='relative'>
    {#if loading}
      <!-- Global spinner overlay -->
      <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
        <Spinner color="purple" size={10} />
      </div>
    {/if}
    <h1 class="mb-8 text-4xl font-extrabold tracking-tight text-gray-900 dark:text-white" style="margin-top: 1%; margin-left:8%; margin-bottom:1%">Landmarks</h1>
    <div class="my-8 mx-auto w-5/6 h-3/4 p-6 border rounded-lg shadow overflow-y-auto">
      {#if savedImage}
      <!-- Show saved image -->
      <div class="flex">
        <!-- Image Section -->
        <div class="w-1/2 p-4 flex justify-center items-center border-r">
          <div class="relative">
            <button
              class="absolute top-2 right-2 bg-gray-200 rounded-full p-2 shadow hover:bg-gray-300"
              onclick={removeImage}>
              ✕
            </button>
            <img src={savedImage} alt="Saved" class="h-auto max-h-96 object-contain" />
          </div>
        </div>
  
        <!-- Text Section -->
        {#if hasData}
          <div class="w-1/2 p-6 flex flex-col justify-center">
            <p class="p-4 rounded shadow text-gray-900 dark:text-gray-100">
              <b>Culture Trivia:</b> {landmarkData.cultural_significance}
            </p>
          </div>
        {/if}
      </div>
      {:else}
        <!-- Show dropzone -->
        <div
          class="relative border-2 border-dashed border-gray-400 p-6 h-80 flex flex-col items-center justify-center"
          role="button"
          tabindex="0"
          ondrop={dropHandle}
          ondragover={(event) => event.preventDefault()}
          onclick={() => document.querySelector('input[type="file"]').click()}
          onkeydown={(event) => {
            if (event.key === 'Enter' || event.key === ' ') {
              event.preventDefault();
              document.querySelector('input[type="file"]').click();
            }
          }}>
          <svg
            aria-hidden="true"
            class="mb-3 w-10 h-10 text-gray-400"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
          </svg>
          <p class="text-gray-500 text-sm mb-2">Drag and drop or click to upload</p>
          <p class="text-xs text-gray-400">PNG, JPG, GIF</p>
          <input
            type="file"
            accept="image/png, image/jpeg, image/gif"
            class="absolute top-0 left-0 w-full h-full opacity-0 cursor-pointer"
            onchange={dropHandle}
          />
        </div>
      {/if}
    
      {#if isCameraOpen}
        <!-- Camera view -->
        <div class="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div class="bg-white p-6 rounded-lg relative">
            <video bind:this={videoSource} autoplay playsinline class="w-96 h-96 object-cover">
              <track kind="captions" src="" />
            </video>
            <div class="flex justify-center gap-4 mt-4">
              {#if isPhotoCaptured}
                <!-- Options after capturing a photo -->
                <GradientButton color="pinkToOrange" class="bg-yellow-500 text-white px-4 py-2 rounded" onclick={retakePhoto}>
                  Retake
                </GradientButton>
                <GradientButton color="greenToBlue" class="bg-green-500 text-white px-4 py-2 rounded" onclick={submitPhoto}>
                  Submit
                </GradientButton>
              {:else}
                <!-- Capture and Close options -->
                <GradientButton color="pinkToOrange" class="bg-blue-500 text-white px-4 py-2 rounded" onclick={closeCamera}>
                  Close Camera
                </GradientButton>
                <GradientButton color="greenToBlue" class="bg-red-500 text-white px-4 py-2 rounded" onclick={capturePhoto}>
                  Capture Photo
                </GradientButton>
              {/if}
            </div>
          </div>
        </div>
      {:else if !savedImage}
        <GradientButton color="purpleToBlue" class="mt-4 bg-purple-500 text-white px-4 py-2 rounded" onclick={openCamera}>
          Open Camera
        </GradientButton>
      {/if}
    </div>
  </div>
  
  
  