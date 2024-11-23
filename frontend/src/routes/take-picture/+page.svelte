<script>
    import { Dropzone, Button } from 'flowbite-svelte';
  
    let value = [];
    let videoSource;
    let canvas = null;
    let loading = false;
    let stream = null;
    let isCameraOpen = false; 
  
    const dropHandle = (event) => {
      value = [];
      event.preventDefault();
      if (event.dataTransfer.items) {
        [...event.dataTransfer.items].forEach((item) => {
          if (item.kind === 'file') {
            const file = item.getAsFile();
            value.push(file.name);
          }
        });
      } else {
        [...event.dataTransfer.files].forEach((file) => {
          value = file.name;
        });
      }
    };
  
    const handleChange = (event) => {
      const files = event.target.files;
      if (files.length > 0) {
        value.push(files[0].name);
      }
    };
  
    const showFiles = (files) => {
      if (files.length === 1) return files[0];
      let concat = '';
      files.map((file) => {
        concat += file;
        concat += ', ';
      });
      if (concat.length > 40) concat = concat.slice(0, 40);
      concat += '...';
      return concat;
    };
  
    const handleButtonClick = (event) => {
      event.stopPropagation();
      if (!isCameraOpen) {
        isCameraOpen = true;  
        obtenerVideoCamara();  
      } else {
        capturePhoto();  
      }
    };
  
    const obtenerVideoCamara = async () => {
      try {
        loading = true;
        stream = await navigator.mediaDevices.getUserMedia({ video: true });
        videoSource.srcObject = stream;
        videoSource.play();
        loading = false;
      } catch (error) {
        console.log(error);
      }
    };
  
    const capturePhoto = () => {
      canvas = document.createElement('canvas');
      const context = canvas.getContext('2d');
      canvas.width = videoSource.videoWidth;
      canvas.height = videoSource.videoHeight;
      context.drawImage(videoSource, 0, 0, canvas.width, canvas.height);
  
      const photoUrl = canvas.toDataURL('image/png');
      value = [photoUrl];  
      stopCamera();  
      isCameraOpen = false;  
    };
  
    const stopCamera = () => {
      if (stream) {
        const tracks = stream.getTracks();
        tracks.forEach((track) => track.stop());
      }
    };
  
    const closeCamera = () => {
      stopCamera();
      isCameraOpen = false;  
    };
  </script>
  
  <Dropzone
  id="dropzone"
  class="relative my-8 border-2 border-dashed border-gray-400 p-6 overflow-hidden w-full max-w-lg h-80 mx-auto" 
  on:drop={dropHandle}
  on:dragover={(event) => {
    event.preventDefault();
  }}
  on:change={handleChange}>
  
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

  {#if value.length === 0}
    <p class="mb-2 text-sm text-gray-500 dark:text-gray-400">
      <span class="font-semibold">Click to upload</span> or drag and drop
    </p>
    <p class="text-xs text-gray-500 dark:text-gray-400">
      SVG, PNG, JPG or GIF (MAX. 800x400px)
    </p>
  {:else}
    {#if value[0].startsWith('data:image')}
      <img src={value[0]} alt="Captured" class="w-full" />
    {:else}
      <p>{showFiles(value)}</p>
    {/if}
  {/if}

  <div class="flex justify-center mt-10 mb-6 z-10">
    <div class="flex flex-wrap gap-1">
      <Button outline color="purple" on:click={handleButtonClick}>
        {#if isCameraOpen}
          Capture Photo
        {:else}
          Take Photo
        {/if}
      </Button>
    </div>
  </div>
</Dropzone>

  {#if isCameraOpen}
    <div class="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white p-6 rounded-lg relative">
        <video bind:this={videoSource} class="w-96 h-96 object-cover" autoplay playsinline>
          <track kind="captions" src="" />
        </video>
        <div class="absolute top-0 right-0 p-2">
          <Button outline color="red" on:click={closeCamera}>Close</Button>
        </div>
        <div class="flex justify-center mt-4">
          <Button color="green" on:click={capturePhoto}>Capture</Button>
        </div>
      </div>
    </div>
  {/if}