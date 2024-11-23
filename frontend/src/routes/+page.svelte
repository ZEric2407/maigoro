<script>
    import { Carousel, GradientButton } from 'flowbite-svelte';
    import { Section, HeroHeader } from 'flowbite-svelte-blocks';
	import { ArrowRightOutline } from 'flowbite-svelte-icons';

    const images = [
         { src: '/images/codejam1.jpg'},
         { src: '/images/codejam2.jpg'},
         { src: '/images/codejam3.jpg'},
         { src: '/images/codejam4.jpg'},
         { src: '/images/codejam5.jpg'},
    ]
</script>

<Section name="heroVisual" sectionClass="py-0">
	<div class="mb-8 mr-auto place-self-center lg:col-span-4">
		<HeroHeader
			h1Class="max-w-2xl mb-4 text-4xl font-extrabold tracking-tight leading-none md:text-5xl xl:text-6xl dark:text-white"
			pClass="max-w-2xl mb-6 font-light text-gray-500 lg:mb-8 md:text-lg lg:text-xl dark:text-gray-400"
		>
			<svelte:fragment slot="h1">
				Welcome to Maigoro!
			</svelte:fragment>
			<svelte:fragment slot="paragraph">
				Capture everything in a single frame bringing stories and senses together. <br> Enrich your mind 
                with wisdom and knowledge with the new cultural context feature!
                Seize the moment by capturing the cultural essence and share the story beyond a snapshot.

			</svelte:fragment>
			<GradientButton 
				color='pinkToOrange'
				size="xl"
				class="inline-flex items-center justify-center"	>
				<a href="/take-picture" class="inline-flex items-center justify-center">
                    Get Started <ArrowRightOutline size="md" class="-mr-1 ml-2" />
                </a>
			</GradientButton>
		</HeroHeader>
	</div>
	<div class="flex justify-center w-full lg:col-span-8 lg:mt-0 lg:flex">
		<div class="max-w-4xl w-full">
			<Carousel {images} duration="3000" let:Indicators>
				<Indicators />
			</Carousel>
		</div>
	</div>
</Section>

