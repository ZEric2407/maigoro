<script>
	import { A } from 'flowbite-svelte';
	import { Section, Faq, FaqItem } from 'flowbite-svelte-blocks';
	import { HeartSolid } from 'flowbite-svelte-icons';
</script>

<p class="about-text">
	Are you tired of accidentally eating dog meat while visiting a foreign country or finding bugs in your 
	cheese? Are you constantly annoyed at having to decipher hieroglyphs-like writting when you travel the 
	world? Don't worry, we got you! Maigoro is a handy app designed to make sure that you
    know exactly what you are looking at: Just take a picture and we'll provide you with descriptions, 
	translations to a language of your choice, as well as some cultural context 
	of whatever you may bite into! 
</p>

<Section name="faq" sectionClass="py-0 [&>div]:py-8">
	<h2 class="mb-8 text-4x1 font-extrabold tracking-tight text-gray-900 dark:text-white">
		Frequently Asked Questions (FAQ)
	</h2>
	<Faq>
		<div>
			<FaqItem>
				<svelte:fragment slot="h3">What does "Maigorou" mean?</svelte:fragment>
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
					Maigoro offers translation services, cultural significance and context information, and more!
				</p>
			</FaqItem>
			<FaqItem>
				<svelte:fragment slot="h3">Who can use Maigoro?</svelte:fragment>
				<p class="text-gray-500 dark:text-gray-400">
					Anyone with a camera can use Maigoro!
				</p>
			</FaqItem>
			<FaqItem>
				<svelte:fragment slot="h3">Can I upload pictures directly from my app?</svelte:fragment>
				<p class="text-gray-500 dark:text-gray-400">
					Yes, you may also import a picture of your choice.
				</p>
			</FaqItem>
			<FaqItem>
				<svelte:fragment slot="h3">What's to come?</svelte:fragment>
				<p class="text-gray-500 dark:text-gray-400">
					We are currently researching and developing hardware that people with disabilities can use such as 
					wearable devices that will scan the surroundings of one's environment and communicate it
					to the user.	
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