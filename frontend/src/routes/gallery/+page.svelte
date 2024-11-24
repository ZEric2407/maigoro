<script>
    import { onMount } from 'svelte';
    import { Gallery } from 'flowbite-svelte';

    let images = []; // Reactive variable for images

    const getTransactions = async () => {
        try {
            const response = await fetch('http://localhost:5000/api/gallery', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            if (response.ok) {
                const data = await response.json();
                console.log('Backend response:', data);

                // Update images with reactivity in mind
                images = data.transactions.map((transaction, i) => ({
                    alt: `Image ${i}`,
                    src: `http://localhost:5000/${transaction.image_url.replace("\\", "/")}`,
                }));

                console.log('Updated images:', images); // Debugging
                return data;
            } else {
                console.error('Error fetching images from backend:', response.statusText);
            }
        } catch (error) {
            console.error('Error during backend call:', error);
        }
    };

    onMount(async () => {
        await getTransactions();
    });
</script>

<Gallery items={images} class="gap-4 grid-cols-2 md:grid-cols-3" />
