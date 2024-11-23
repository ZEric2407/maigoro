<script>
    import { Carousel, Button } from 'flowbite-svelte';
    
    const images = [
         { src: '/images/codejam1.jpg'},
         { src: '/images/codejam2.jpg'},
         { src: '/images/codejam3.jpg'},
         { src: '/images/codejam4.jpg'},
         { src: '/images/codejam5.jpg'},
    ]
</script>

<div class="flex justify-center w-full mt-20">
    <div class="max-w-4xl w-full">
        <Carousel {images} duration="3000" let:Indicators>
            <Indicators />
        </Carousel>
    </div>
</div>

<div class="text-center mt-12 px-4">
    <h2 class="text-3xl font-semibold text-gray-800 dark:text-white mb-4">Welcome to Maigoro</h2>
    <p class="text-lg text-gray-600 dark:text-gray-300 mb-6">
        Understanding Taste, Tradition, and Culture
    </p>
    <p class="text-lg text-gray-600 dark:text-gray-300">
        /* write here */
    </p>

    <div class="flex justify-center mt-6">
        <div class="flex flex-wrap gap-2">
            <Button outline color="purple">Get Started</Button>
        </div>
    </div>

</div>

