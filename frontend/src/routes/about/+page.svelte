<script>
	import { A } from 'flowbite-svelte';
	import { Section, Faq, FaqItem } from 'flowbite-svelte-blocks';
	import { HeartSolid } from 'flowbite-svelte-icons';
</script>

<p class="about-text mx-20" style="margin-top: 25px;">
	Are you tired of accidentally eating repugnant food while visiting a foreign country or finding bugs in your 
	cheese? Are you constantly annoyed at having to decipher cryptic writting when you travel the 
	world? What about hard-to-read road signs that are too confusing? Don't worry, we got you! Maigoro is a handy app designed to make sure that you
    know exactly what you are looking at: Just take a picture and we'll provide you with descriptions, 
	translations to a language of your choice, as well as some cultural context 
	of whatever you may bite into! 
</p>

<Section name="faq" sectionClass="py-0 [&>div]:py-8 w-full">
	<h2 class="mb-8 text-4xl font-extrabold tracking-tight text-gray-900 dark:text-white">
		Frequently Asked Questions (FAQ)
	</h2>
	<Faq>
		<div>
			<FaqItem>
				<svelte:fragment slot="h3">What does "Maigoro" mean?</svelte:fragment>
				<p class="text-gray-500 dark:text-gray-400">
					Maigoro ( /ˈmaɪ-goʊ-roʊ/, also MY-go-roh ) is the 
					personal guru that spiritually guides one, connecting 
					one's mind with wisdom and offering help to one's inner 
					and outer journey by giving a deeper insight to the world. 
					Being able to help one in a moment of doubt, maigoro will 
					allow one to reach a deeper level of understanding of their environment.
				</p>
			</FaqItem>
			<FaqItem>
				<svelte:fragment slot="h3">What key features can Maigoro offer?</svelte:fragment>
				<p class="text-gray-500 dark:text-gray-400">
					Translation Services – Snap a photo or text to instantly translate into multiple languages.<br>
					Cultural Significance and Context – Get detailed insights about cultural artifacts, symbols, or phrases to enhance understanding.<br>
				</p>
			</FaqItem>
			<FaqItem>
				<svelte:fragment slot="h3"
					>Who can use Maigoro?</svelte:fragment
				>
				<p class="text-gray-500 dark:text-gray-400">
					Anyone with a smartphone or camera can use Maigoro to explore the world with enhanced insights and wisdom. With just a photo, you unlock a gateway to understanding your surroundings on a deeper level.
				</p>
			</FaqItem>
		</div>
		<div>
			<FaqItem>
				<svelte:fragment slot="h3">Can I upload pictures directly?</svelte:fragment>
				<p class="text-gray-500 dark:text-gray-400">
					Yes! Whether you capture an image using your camera or import a photo from your library, Maigoro makes it easy to explore and learn.
				</p>
			</FaqItem>
			<FaqItem>
				<svelte:fragment slot="h3"
					>What's to come?</svelte:fragment
				>
				<p class="text-gray-500 dark:text-gray-400">
					This project can be expanded by developping hardware that people with disabilities can use such as 
					wearable devices that will scan the surroundings of one's environment and communicate it
					to the user. These devices will scan and interpret the environment, providing auditory or tactile 
					feedback to users, enabling a more connected and accessible experience.	
				</p>
			</FaqItem>

		</div>
	</Faq>
</Section>

<style>
	.about-text {
		@apply text-gray-900 dark:text-gray-100;
	}
</style>