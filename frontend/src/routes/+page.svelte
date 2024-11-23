<script>
    import { Carousel } from 'flowbite-svelte';
    
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


